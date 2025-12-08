/**
 * Progress Client
 * 
 * Client functions for progress tracking operations (updateProgress, getProgress).
 * All functions are placeholders that make API calls to backend endpoints.
 * 
 * TODO: Real progress tracking logic will be implemented in a future feature.
 * Currently returns placeholder responses.
 */

interface ProgressRecord {
  user_id: string;
  chapter_id: number;
  state: string;
  updated_at: string;
  message?: string;
}

interface ProgressListResponse {
  progress: ProgressRecord[];
}

/**
 * Update progress for a chapter.
 * 
 * @param chapterId Chapter number
 * @param state Progress state ("in_progress" or "completed")
 * @returns Promise with progress record
 */
export async function updateProgress(
  chapterId: number,
  state: string
): Promise<ProgressRecord> {
  // TODO: Replace with actual API endpoint
  // Determine endpoint based on state
  const endpoint = state === "completed" 
    ? `/api/progress/${chapterId}/complete`
    : `/api/progress/${chapterId}/start`;

  const response = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      // TODO: Add Authorization header with session token
    },
  });

  if (!response.ok) {
    throw new Error('Progress update failed (placeholder)');
  }

  const data: ProgressRecord = await response.json();
  return data;
}

/**
 * Get all progress records for the current user.
 * 
 * @returns Promise with list of progress records
 */
export async function getProgress(): Promise<ProgressRecord[]> {
  // TODO: Replace with actual API endpoint
  // TODO: Include session token in request
  try {
    const response = await fetch('/api/progress/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        // TODO: Add Authorization header with session token
      },
    });

    if (!response.ok) {
      return [];
    }

    const data: ProgressListResponse = await response.json();
    return data.progress;
  } catch (error) {
    return [];
  }
}

