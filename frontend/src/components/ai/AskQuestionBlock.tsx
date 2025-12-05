import React, { useState } from 'react';

/**
 * AskQuestionBlock Component
 * 
 * A placeholder component for asking questions about chapter content.
 * This component will be integrated with RAG pipeline in future features.
 * 
 * @param chapterId - Optional chapter ID for context
 * @param sectionId - Optional section ID for context
 * 
 * @example
 * ```mdx
 * <AskQuestionBlock chapterId={1} sectionId="what-is-physical-ai" />
 * ```
 * 
 * TODO: Integrate with API endpoint POST /api/ai/ask-question
 * TODO: Add RAG pipeline for retrieving relevant chapter content
 * TODO: Add OpenAI API call for generating answers
 */
interface AskQuestionBlockProps {
  chapterId?: number;
  sectionId?: string;
}

export default function AskQuestionBlock({ 
  chapterId, 
  sectionId 
}: AskQuestionBlockProps) {
  const [question, setQuestion] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('AskQuestionBlock: Question submitted', { 
      question, 
      chapterId, 
      sectionId 
    });
    // TODO: Call API endpoint POST /api/ai/ask-question
    setQuestion('');
  };

  return (
    <div style={{
      border: '1px solid #e0e0e0',
      borderRadius: '8px',
      padding: '16px',
      margin: '24px 0',
      backgroundColor: '#f9f9f9'
    }}>
      <h3 style={{ marginTop: 0, marginBottom: '12px' }}>
        Ask a Question
      </h3>
      <form onSubmit={handleSubmit}>
        <textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask a question about this section..."
          style={{
            width: '100%',
            minHeight: '80px',
            padding: '8px',
            border: '1px solid #ccc',
            borderRadius: '4px',
            fontSize: '14px',
            fontFamily: 'inherit',
            resize: 'vertical',
            marginBottom: '8px'
          }}
        />
        <button
          type="submit"
          style={{
            padding: '8px 16px',
            backgroundColor: '#3578e5',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
            fontSize: '14px'
          }}
        >
          Submit Question
        </button>
      </form>
      <p style={{ 
        marginTop: '12px', 
        fontSize: '12px', 
        color: '#666',
        fontStyle: 'italic'
      }}>
        This is a placeholder. Real AI-powered question answering will be available soon.
      </p>
    </div>
  );
}

