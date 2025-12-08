/**
 * SelectionRAGBar Component
 * 
 * Component that appears when user highlights text in MDX chapters.
 * Allows user to ask questions about the selected text.
 * 
 * TODO: Real AI logic will be implemented in a future feature.
 * Currently displays placeholder UI and makes placeholder API calls.
 */

import React, { useState } from 'react';

interface SelectionRAGBarProps {
  selectedText: string;
  chapterId: number;
  onClose: () => void;
}

export default function SelectionRAGBar({
  selectedText,
  chapterId,
  onClose
}: SelectionRAGBarProps) {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState<string | null>(null);
  const [contextUsed, setContextUsed] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Truncate selected text for preview (max 200 chars)
  const previewText = selectedText.length > 200 
    ? selectedText.substring(0, 200) + '...' 
    : selectedText;

  const handleAsk = async () => {
    if (!question.trim()) {
      setError('Please enter a question');
      return;
    }

    setLoading(true);
    setError(null);
    setAnswer(null);
    setContextUsed(null);

    try {
      // TODO: Replace with actual API endpoint
      const response = await fetch('/api/rag/selection', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          selected_text: selectedText,
          question: question.trim(),
          chapter_id: chapterId,
        }),
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }

      const data = await response.json();
      setAnswer(data.answer || 'placeholder answer');
      setContextUsed(data.context_used || 'placeholder context');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to get answer');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      position: 'fixed',
      bottom: '20px',
      left: '50%',
      transform: 'translateX(-50%)',
      width: '90%',
      maxWidth: '600px',
      backgroundColor: '#fff',
      border: '1px solid #ddd',
      borderRadius: '8px',
      padding: '16px',
      boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
      zIndex: 1000,
    }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
        <h3 style={{ margin: 0, fontSize: '16px', fontWeight: '600' }}>Ask about selected text</h3>
        <button
          onClick={onClose}
          style={{
            background: 'none',
            border: 'none',
            fontSize: '20px',
            cursor: 'pointer',
            padding: '0',
            color: '#666',
          }}
        >
          ×
        </button>
      </div>

      {/* Selected text preview */}
      <div style={{
        backgroundColor: '#f5f5f5',
        padding: '12px',
        borderRadius: '4px',
        marginBottom: '12px',
        fontSize: '14px',
        color: '#333',
        maxHeight: '100px',
        overflow: 'auto',
      }}>
        <strong>Selected:</strong> {previewText}
      </div>

      {/* Question input */}
      <textarea
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Enter your question about the selected text..."
        style={{
          width: '100%',
          minHeight: '80px',
          padding: '8px',
          border: '1px solid #ddd',
          borderRadius: '4px',
          fontSize: '14px',
          fontFamily: 'inherit',
          resize: 'vertical',
          marginBottom: '12px',
        }}
      />

      {/* Ask button */}
      <button
        onClick={handleAsk}
        disabled={loading || !question.trim()}
        style={{
          width: '100%',
          padding: '10px',
          backgroundColor: loading ? '#ccc' : '#007bff',
          color: '#fff',
          border: 'none',
          borderRadius: '4px',
          fontSize: '14px',
          fontWeight: '600',
          cursor: loading ? 'not-allowed' : 'pointer',
          marginBottom: '12px',
        }}
      >
        {loading ? 'Asking...' : 'Ask'}
      </button>

      {/* Error message */}
      {error && (
        <div style={{
          padding: '8px',
          backgroundColor: '#fee',
          color: '#c33',
          borderRadius: '4px',
          fontSize: '14px',
          marginBottom: '12px',
        }}>
          {error}
        </div>
      )}

      {/* Answer display */}
      {answer && (
        <div style={{
          padding: '12px',
          backgroundColor: '#e8f5e9',
          borderRadius: '4px',
          fontSize: '14px',
          marginBottom: '12px',
        }}>
          <strong>Answer:</strong> {answer}
        </div>
      )}

      {/* Context used display */}
      {contextUsed && (
        <div style={{
          padding: '8px',
          backgroundColor: '#f5f5f5',
          borderRadius: '4px',
          fontSize: '12px',
          color: '#666',
        }}>
          <strong>Context:</strong> {contextUsed}
        </div>
      )}
    </div>
  );
}

