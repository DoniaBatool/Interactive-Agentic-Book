import React, { useState } from 'react';

/**
 * ExplainLike10Block Component
 * 
 * A placeholder component for generating simplified explanations at age-appropriate level.
 * This component will use LLM to explain complex concepts in simple terms.
 * 
 * @param concept - Optional concept name to explain
 * @param chapterId - Optional chapter ID for context
 * 
 * @example
 * ```mdx
 * <ExplainLike10Block concept="autonomy" chapterId={1} />
 * ```
 * 
 * TODO: Integrate with API endpoint POST /api/ai/explain-like-10
 * TODO: Add LLM call with ELI10 (Explain Like I'm 10) prompt
 * TODO: Add concept context retrieval from chapter content
 */
interface ExplainLike10BlockProps {
  concept?: string;
  chapterId?: number;
}

export default function ExplainLike10Block({ 
  concept, 
  chapterId 
}: ExplainLike10BlockProps) {
  const [explanation, setExplanation] = useState<string | null>(null);

  const handleExplain = () => {
    console.log('ExplainLike10Block: Explanation requested', { 
      concept, 
      chapterId 
    });
    // TODO: Call API endpoint POST /api/ai/explain-like-10
    setExplanation('This is a placeholder explanation. Real simplified explanations will be available soon.');
  };

  return (
    <div style={{
      border: '1px solid #e0e0e0',
      borderRadius: '8px',
      padding: '16px',
      margin: '24px 0',
      backgroundColor: '#f0f7ff'
    }}>
      <h3 style={{ marginTop: 0, marginBottom: '12px' }}>
        Explain Like I'm 10
      </h3>
      {concept && (
        <p style={{ 
          marginBottom: '12px', 
          fontWeight: 'bold',
          color: '#3578e5'
        }}>
          Concept: {concept}
        </p>
      )}
      <button
        onClick={handleExplain}
        style={{
          padding: '8px 16px',
          backgroundColor: '#3578e5',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          cursor: 'pointer',
          fontSize: '14px',
          marginBottom: '12px'
        }}
      >
        Explain in Simple Terms
      </button>
      {explanation && (
        <div style={{
          padding: '12px',
          backgroundColor: 'white',
          borderRadius: '4px',
          border: '1px solid #ddd',
          marginTop: '12px'
        }}>
          <p style={{ margin: 0, lineHeight: '1.6' }}>
            {explanation}
          </p>
        </div>
      )}
      {!explanation && (
        <p style={{ 
          fontSize: '12px', 
          color: '#666',
          fontStyle: 'italic',
          margin: 0
        }}>
          Click the button to get a simplified explanation.
        </p>
      )}
    </div>
  );
}

