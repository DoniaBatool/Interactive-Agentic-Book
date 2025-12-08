/**
 * Search Bar Component
 * 
 * Placeholder search bar component for global search across all chapters.
 * All search logic is placeholder—no real search implementation.
 * 
 * TODO: Real search logic will be implemented in a future feature.
 * Currently displays placeholder UI and makes placeholder API calls.
 */

import React, { useState } from 'react';

interface SearchResult {
  chapter_id: number;
  chapter_title: string;
  snippet: string;
  score: number;
  section_id: string;
}

interface SearchResponse {
  results: SearchResult[];
  query: string;
  total_results: number;
}

export default function SearchBar() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async () => {
    if (!query.trim()) {
      setError('Please enter a search query');
      return;
    }

    setLoading(true);
    setError(null);
    setResults([]);

    try {
      // TODO: Replace with actual API endpoint
      const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Search failed');
      }

      const data: SearchResponse = await response.json();
      setResults(data.results);
    } catch (err: any) {
      setError(err.message || 'An unexpected error occurred.');
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  return (
    <div style={{ 
      padding: '20px', 
      border: '1px solid #ccc', 
      borderRadius: '4px',
      marginBottom: '20px'
    }}>
      <h3>Search Across All Chapters</h3>
      <div style={{ display: 'flex', gap: '10px', marginBottom: '10px' }}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Search across all chapters..."
          style={{ 
            flex: 1, 
            padding: '8px', 
            border: '1px solid #ccc', 
            borderRadius: '4px' 
          }}
        />
        <button
          onClick={handleSearch}
          disabled={loading}
          style={{
            padding: '8px 16px',
            backgroundColor: '#007bff',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: loading ? 'not-allowed' : 'pointer'
          }}
        >
          {loading ? 'Searching...' : 'Search'}
        </button>
      </div>

      {error && (
        <div style={{ color: 'red', marginBottom: '10px' }}>
          Error: {error}
        </div>
      )}

      {results.length > 0 && (
        <div>
          <h4>Results ({results.length}):</h4>
          <ul style={{ listStyle: 'none', padding: 0 }}>
            {results.map((result, index) => (
              <li
                key={index}
                style={{
                  padding: '10px',
                  marginBottom: '10px',
                  border: '1px solid #eee',
                  borderRadius: '4px'
                }}
              >
                <div style={{ fontWeight: 'bold' }}>
                  {result.chapter_title} (Score: {result.score.toFixed(2)})
                </div>
                <div style={{ fontSize: '0.9em', color: '#666', marginTop: '5px' }}>
                  {result.snippet}
                </div>
                <div style={{ fontSize: '0.8em', color: '#999', marginTop: '5px' }}>
                  Section: {result.section_id}
                </div>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

