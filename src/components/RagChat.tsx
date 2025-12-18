import React, { useCallback, useRef, useState } from 'react';

type Role = 'user' | 'assistant';

interface Citation {
  path: string;
  chapter: string;
  section?: string | null;
  score?: number | null;
}

interface Message {
  id: string;
  role: Role;
  content: string;
  citations?: Citation[];
}

export interface RagChatProps {
  backendUrl?: string;
  chapterFilter?: string;
  useStreaming?: boolean;
}

const DEFAULT_BACKEND_URL = 'http://127.0.0.1:8000';

export const RagChat: React.FC<RagChatProps> = ({
  backendUrl = DEFAULT_BACKEND_URL,
  chapterFilter,
  useStreaming = true,
}) => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const assistantMessageIdRef = useRef<string | null>(null);

  const appendAssistantMessage = useCallback(
    (contentDelta: string, citations?: Citation[]) => {
      setMessages((prev) => {
        const id = assistantMessageIdRef.current ?? `assistant-${Date.now()}`;
        assistantMessageIdRef.current = id;

        const existingIndex = prev.findIndex((m) => m.id === id);
        if (existingIndex === -1) {
          return [
            ...prev,
            {
              id,
              role: 'assistant',
              content: contentDelta,
              citations: citations ?? [],
            },
          ];
        }

        const existing = prev[existingIndex];
        const updated: Message = {
          ...existing,
          content: existing.content + contentDelta,
          citations: citations ?? existing.citations,
        };
        const clone = [...prev];
        clone[existingIndex] = updated;
        return clone;
      });
    },
    [],
  );

  const resetAssistantMessageRef = () => {
    assistantMessageIdRef.current = null;
  };

  const sendMessage = useCallback(async () => {
    const question = input.trim();
    if (!question || loading) return;

    setError(null);
    setLoading(true);
    resetAssistantMessageRef();

    const userMessage: Message = {
      id: `user-${Date.now()}`,
      role: 'user',
      content: question,
    };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');

    try {
      const payload: any = {
        question,
        stream: useStreaming,
      };
      if (chapterFilter) {
        payload.filters = { chapter: chapterFilter };
      }

      const res = await fetch(`${backendUrl}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      if (!res.ok) {
        const text = await res.text();
        throw new Error(text || `HTTP ${res.status}`);
      }

      if (!useStreaming) {
        const data = await res.json();
        const assistantMessage: Message = {
          id: `assistant-${Date.now()}`,
          role: 'assistant',
          content: data.answer ?? '',
          citations: data.citations ?? [],
        };
        setMessages((prev) => [...prev, assistantMessage]);
      } else {
        if (!res.body) {
          throw new Error('Streaming response body is empty');
        }

        const reader = res.body.getReader();
        const decoder = new TextDecoder('utf-8');
        let buffer = '';

        const processChunk = (chunk: string) => {
          buffer += chunk;
          const events = buffer.split('\n\n');
          buffer = events.pop() ?? '';

          for (const rawEvent of events) {
            const lines = rawEvent.split('\n').filter(Boolean);
            let eventName = 'message';
            let dataStr = '';

            for (const line of lines) {
              if (line.startsWith('event:')) {
                eventName = line.replace('event:', '').trim();
              } else if (line.startsWith('data:')) {
                dataStr += line.replace('data:', '').trim();
              }
            }

            if (!dataStr) continue;

            try {
              const data = JSON.parse(dataStr);
              if (eventName === 'metadata' && Array.isArray(data.citations)) {
                appendAssistantMessage('', data.citations);
              } else if (eventName === 'token' && data.text) {
                appendAssistantMessage(data.text);
              } else if (eventName === 'error') {
                setError(data.message || 'Chat stream error');
              }
            } catch (e) {
              // Ignore malformed events
              // eslint-disable-next-line no-console
              console.warn('Failed to parse SSE event', e);
            }
          }
        };

        // eslint-disable-next-line no-constant-condition
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          const chunk = decoder.decode(value, { stream: true });
          processChunk(chunk);
        }
      }
    } catch (e: any) {
      console.error('Chat error', e);
      setError('Chat service error, please try again.');
    } finally {
      setLoading(false);
      resetAssistantMessageRef();
    }
  }, [appendAssistantMessage, backendUrl, chapterFilter, input, loading, useStreaming]);

  const handleKeyDown: React.KeyboardEventHandler<HTMLInputElement> = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      void sendMessage();
    }
  };

  return (
    <div className="rag-chat-card">
      <div className="rag-chat-header">
        <h3>Ask the AI about this chapter</h3>
        {chapterFilter && <span className="rag-chat-chip">Chapter: {chapterFilter}</span>}
      </div>

      <div className="rag-chat-messages">
        {messages.length === 0 && (
          <div className="rag-chat-empty">Start by asking a question about the content.</div>
        )}
        {messages.map((m) => (
          <div
            key={m.id}
            className={`rag-chat-message rag-chat-message-${m.role}`}
          >
            <div className="rag-chat-message-content">{m.content}</div>
            {m.role === 'assistant' && m.citations && m.citations.length > 0 && (
              <div className="rag-chat-citations">
                <div className="rag-chat-citations-title">Sources:</div>
                <ul>
                  {m.citations.map((c, idx) => (
                    <li key={idx}>
                      <code>{c.chapter}</code>
                      {c.section ? ` · ${c.section}` : ''} · <small>{c.path}</small>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}
      </div>

      {error && <div className="rag-chat-error">{error}</div>}

      <div className="rag-chat-input-row">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask a question about this chapter..."
          disabled={loading}
        />
        <button
          type="button"
          onClick={() => void sendMessage()}
          disabled={loading || !input.trim()}
        >
          {loading ? 'Thinking…' : 'Send'}
        </button>
      </div>
    </div>
  );
};

export default RagChat;


