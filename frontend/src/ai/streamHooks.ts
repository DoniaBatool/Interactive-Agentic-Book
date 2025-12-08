/**
 * Streaming Hooks
 * 
 * React hooks for consuming real-time AI streaming responses.
 */

import { useState, useEffect, useCallback } from 'react';
import { connectSSE, connectWebSocket, StreamingChunk, StreamingCallbacks } from './streamClient';

export interface UseAIStreamingResult {
  chunks: string[];
  isStreaming: boolean;
  error: Error | null;
  startStream: () => void;
  stopStream: () => void;
}

/**
 * Hook for general AI streaming.
 * 
 * @param endpoint Streaming endpoint URL
 * @returns Streaming state and controls
 * 
 * TODO: Implement real streaming hook
 * TODO: Manage EventSource/WebSocket connection
 * TODO: Update state with chunks
 * TODO: Handle errors and completion
 */
export function useAIStreaming(endpoint: string): UseAIStreamingResult {
  const [chunks, setChunks] = useState<string[]>([]);
  const [isStreaming, setIsStreaming] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const [eventSource, setEventSource] = useState<EventSource | null>(null);
  
  const startStream = useCallback(() => {
    // TODO: Implement real streaming
    setIsStreaming(true);
    setError(null);
    setChunks([]);
    
    const callbacks: StreamingCallbacks = {
      onChunk: (chunk: StreamingChunk) => {
        setChunks(prev => [...prev, chunk.token]);
      },
      onError: (err: Error) => {
        setError(err);
        setIsStreaming(false);
      },
      onComplete: () => {
        setIsStreaming(false);
      }
    };
    
    const es = connectSSE(endpoint, callbacks);
    setEventSource(es);
  }, [endpoint]);
  
  const stopStream = useCallback(() => {
    if (eventSource) {
      eventSource.close();
      setEventSource(null);
      setIsStreaming(false);
    }
  }, [eventSource]);
  
  useEffect(() => {
    return () => {
      if (eventSource) {
        eventSource.close();
      }
    };
  }, [eventSource]);
  
  return {
    chunks,
    isStreaming,
    error,
    startStream,
    stopStream
  };
}

/**
 * Hook for block-specific AI streaming.
 * 
 * @param blockType Type of AI block
 * @param chapterId Chapter ID
 * @param userInput Block-specific input data
 * @returns Streaming state and controls
 * 
 * TODO: Implement real block-specific streaming hook
 * TODO: Build endpoint URL based on block type
 * TODO: Pass user input as query parameters
 * TODO: Manage streaming connection
 */
export function useAIBlockStreaming(
  blockType: string,
  chapterId: number,
  userInput: Record<string, any>
): UseAIStreamingResult {
  // Build endpoint URL
  const baseUrl = process.env.NEXT_PUBLIC_BACKEND_API_URL || 'http://localhost:8000';
  const params = new URLSearchParams({
    chapter_id: chapterId.toString(),
    ...Object.fromEntries(
      Object.entries(userInput).map(([k, v]) => [k, String(v)])
    )
  });
  const endpoint = `${baseUrl}/api/stream/ai-block/${blockType}?${params.toString()}`;
  
  return useAIStreaming(endpoint);
}

