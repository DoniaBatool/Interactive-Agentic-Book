import React, { useState } from 'react';

/**
 * InteractiveQuizBlock Component
 * 
 * A placeholder component for interactive quizzes based on chapter learning objectives.
 * This component will generate adaptive quizzes using LLM in future features.
 * 
 * @param chapterId - Optional chapter ID for quiz generation
 * @param numQuestions - Optional number of questions (default: 5)
 * 
 * @example
 * ```mdx
 * <InteractiveQuizBlock chapterId={1} numQuestions={5} />
 * ```
 * 
 * TODO: Integrate with API endpoint POST /api/ai/quiz
 * TODO: Generate quiz questions from chapter learning objectives using LLM
 * TODO: Add quiz state management and scoring
 */
interface InteractiveQuizBlockProps {
  chapterId?: number;
  numQuestions?: number;
}

export default function InteractiveQuizBlock({ 
  chapterId, 
  numQuestions = 5 
}: InteractiveQuizBlockProps) {
  const [quizStarted, setQuizStarted] = useState(false);

  const handleStartQuiz = () => {
    console.log('InteractiveQuizBlock: Quiz started', { 
      chapterId, 
      numQuestions 
    });
    // TODO: Call API endpoint POST /api/ai/quiz
    setQuizStarted(true);
  };

  return (
    <div style={{
      border: '1px solid #e0e0e0',
      borderRadius: '8px',
      padding: '16px',
      margin: '24px 0',
      backgroundColor: '#fff9e6'
    }}>
      <h3 style={{ marginTop: 0, marginBottom: '12px' }}>
        Interactive Quiz
      </h3>
      {!quizStarted ? (
        <>
          <p style={{ marginBottom: '12px', color: '#666' }}>
            Test your understanding with {numQuestions} questions about this chapter.
          </p>
          <button
            onClick={handleStartQuiz}
            style={{
              padding: '10px 20px',
              backgroundColor: '#3578e5',
              color: 'white',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer',
              fontSize: '14px',
              fontWeight: 'bold'
            }}
          >
            Start Quiz
          </button>
        </>
      ) : (
        <div>
          <p style={{ 
            marginBottom: '12px', 
            color: '#666',
            fontStyle: 'italic'
          }}>
            Quiz questions will appear here. This is a placeholder.
          </p>
          <div style={{
            padding: '12px',
            backgroundColor: 'white',
            borderRadius: '4px',
            border: '1px solid #ddd',
            minHeight: '100px'
          }}>
            <p style={{ 
              margin: 0, 
              color: '#999',
              textAlign: 'center'
            }}>
              Quiz questions will be generated here in future features.
            </p>
          </div>
        </div>
      )}
    </div>
  );
}

