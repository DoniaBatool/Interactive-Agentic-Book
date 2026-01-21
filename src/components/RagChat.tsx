import React, { useCallback, useEffect, useRef, useState } from 'react';

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
  showGreeting?: boolean;
  mode?: 'rag' | 'agent'; // 'rag' = basic RAG, 'agent' = Agents/ChatKit with function calling
  hideHeader?: boolean; // Hide the header when used inside sidebar
}

import { BACKEND_URL } from '../config/env';

// Backend URL: use env var if available, otherwise default to localhost
// Note: process.env is not available in browser, so we use a fallback
const getBackendUrl = (): string => {
  if (typeof window !== 'undefined') {
    // Check for window-level config first
    if ((window as any).__BACKEND_URL__) {
      return (window as any).__BACKEND_URL__;
    }
  }
  // Use BACKEND_URL from env config (automatically detects production vs development)
  return BACKEND_URL;
};

const DEFAULT_BACKEND_URL = getBackendUrl();

// Session ID management for chat history persistence
const SESSION_ID_KEY = 'rag-chat-session-id';

const getSessionId = (): string => {
  if (typeof window === 'undefined') return '';
  
  let sessionId = localStorage.getItem(SESSION_ID_KEY);
  if (!sessionId) {
    // Generate UUID
    sessionId = crypto.randomUUID();
    localStorage.setItem(SESSION_ID_KEY, sessionId);
  }
  return sessionId;
};

const GREETING_MESSAGE: Message = {
  id: 'greeting',
  role: 'assistant',
  content: 'Hello! I\'m your AI textbook assistant. I can help you understand concepts from the Physical AI & Humanoid Robotics course. Ask me anything about the content!',
  citations: [],
};

export const RagChat: React.FC<RagChatProps> = ({
  backendUrl = DEFAULT_BACKEND_URL,
  chapterFilter,
  useStreaming = true,
  showGreeting = false,
  mode = 'rag', // Default to basic RAG for backward compatibility
  hideHeader = false, // Hide header when used in sidebar
}) => {
  const [messages, setMessages] = useState<Message[]>(showGreeting ? [GREETING_MESSAGE] : []);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [sessionId, setSessionId] = useState<string>('');
  const [historyLoaded, setHistoryLoaded] = useState(false);
  
  // Initialize session ID on mount
  useEffect(() => {
    setSessionId(getSessionId());
  }, []);
  
  // Load history when chapter changes or component mounts
  useEffect(() => {
    const loadHistory = async () => {
      if (!sessionId) return;
      
      try {
        const params = new URLSearchParams({
          session_id: sessionId,
        });
        if (chapterFilter) {
          params.append('chapter', chapterFilter);
        }
        
        const response = await fetch(`${backendUrl}/chat/history?${params}`, {
          method: 'GET',
          headers: {
            'X-Session-ID': sessionId,
          },
        });
        
        if (response.ok) {
          const data = await response.json();
          if (data.messages && data.messages.length > 0) {
            // Convert history to Message format
            const historyMessages: Message[] = data.messages.map((msg: any) => ({
              id: `history-${msg.id}`,
              role: msg.role as Role,
              content: msg.content,
              citations: msg.citations || [],
            }));
            setMessages(historyMessages);
          } else if (showGreeting) {
            setMessages([GREETING_MESSAGE]);
          } else {
            setMessages([]);
          }
        } else {
          // History not available, start fresh
          if (showGreeting) {
            setMessages([GREETING_MESSAGE]);
          } else {
            setMessages([]);
          }
        }
      } catch (err) {
        // History loading failed, start fresh (this is expected if DB is not configured)
        console.debug('Chat history not available:', err);
        if (showGreeting) {
          setMessages([GREETING_MESSAGE]);
        } else {
          setMessages([]);
        }
      }
      setHistoryLoaded(true);
    };
    
    loadHistory();
  }, [sessionId, chapterFilter, backendUrl, showGreeting]);

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
      // For better context, if user asks about "this page / current page"
      // and we know the chapter, rewrite the question we send to backend
      // while preserving the original text in the UI.
      let backendQuestion = question;
      const lower = question.toLowerCase();
      if (
        chapterFilter &&
        (lower.includes('page i am currently on') ||
          lower.includes('page i am presently on') ||
          lower.includes('current page') ||
          lower.includes('this page'))
      ) {
        backendQuestion = `I am currently viewing the chapter/page titled "${chapterFilter}". ${question}`;
      }

      const payload: any = {
        question: backendQuestion,
        stream: useStreaming,
      };
      if (chapterFilter) {
        payload.filters = { chapter: chapterFilter };
      }

      // Add timeout and better error handling
      const controller = new AbortController();
      // Render (especially free plans) can cold-start; OpenAI calls can also take time.
      // Use a longer timeout to avoid false "timeout" errors during wake-up.
      const timeoutId = setTimeout(() => controller.abort(), 120000); // 120 second timeout
      
      // Use /chat/agent for agent mode, /chat for basic RAG mode
      const endpoint = mode === 'agent' ? '/chat/agent' : '/chat';
      const headers: HeadersInit = {
        'Content-Type': 'application/json',
      };
      // Add session ID for history persistence
      if (sessionId) {
        headers['X-Session-ID'] = sessionId;
      }
      
      const res = await fetch(`${backendUrl}${endpoint}`, {
        method: 'POST',
        headers,
        body: JSON.stringify(payload),
        credentials: 'include', // Include cookies for CORS
        signal: controller.signal,
      });
      
      clearTimeout(timeoutId);

      if (!res.ok) {
        const text = await res.text();
        let errorMsg = `Chat service error (${res.status})`;
        try {
          const errorData = JSON.parse(text);
          errorMsg = errorData.detail || errorMsg;
        } catch {
          if (text) errorMsg = text;
        }
        throw new Error(errorMsg);
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
      // Enhanced error logging for debugging
      console.error('Chat error details:', {
        name: e.name,
        message: e.message,
        stack: e.stack,
        backendUrl,
        timestamp: new Date().toISOString(),
      });
      
      let errorMsg = e.message || 'Chat service error, please try again.';
      
      // Check for specific error types
      if (e.name === 'AbortError') {
        errorMsg =
          'Request timed out. The backend may be waking up (Render cold start) or temporarily slow. Please try again in 10–30 seconds.';
      } else if (
        e.message?.includes('429') ||
        e.message?.toLowerCase?.().includes('insufficient_quota') ||
        e.message?.toLowerCase?.().includes('quota exceeded')
      ) {
        errorMsg =
          'AI chat is temporarily unavailable (API quota exceeded). Please update your OpenAI billing/API key and try again.';
      } else if (e.name === 'TypeError' && (e.message?.includes('Failed to fetch') || e.message?.includes('ERR_EMPTY_RESPONSE'))) {
        errorMsg = `Cannot connect to backend at ${backendUrl}. Please check:\n1. Backend is running (curl ${backendUrl}/health)\n2. CORS is configured\n3. No firewall blocking the connection\n\nError: ${e.message}`;
      } else if (e.message?.includes('NetworkError') || e.message?.includes('Network request failed')) {
        errorMsg = `Network error. Check if backend is running at ${backendUrl}\n\nError: ${e.message}`;
      } else if (e.message?.includes('CORS')) {
        errorMsg = `CORS error. Backend needs to allow origin: ${window.location.origin}\n\nError: ${e.message}`;
      }
      
      setError(errorMsg);
    } finally {
      setLoading(false);
      resetAssistantMessageRef();
    }
  }, [appendAssistantMessage, backendUrl, chapterFilter, input, loading, useStreaming, mode, sessionId]);

  const handleKeyDown: React.KeyboardEventHandler<HTMLInputElement> = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      void sendMessage();
    }
  };

  return (
    <div className="rag-chat-card" style={hideHeader ? { margin: 0, border: 'none', borderRadius: 0, boxShadow: 'none', background: 'transparent', flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden', padding: 0 } : undefined}>
      {!hideHeader && (
        <div className="rag-chat-header">
          <h3>Ask the AI about this chapter</h3>
          {chapterFilter && <span className="rag-chat-chip">Chapter: {chapterFilter}</span>}
        </div>
      )}

      <div className="rag-chat-messages" style={hideHeader ? { flex: 1, margin: 0, maxHeight: 'none', minHeight: 0 } : undefined}>
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


