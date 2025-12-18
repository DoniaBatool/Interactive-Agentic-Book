import React from 'react';
import RagChat from './RagChat';

export interface RagChatPanelProps {
  chapter?: string;
}

export const RagChatPanel: React.FC<RagChatPanelProps> = ({ chapter }) => {
  return (
    <div style={{ marginTop: '2rem', marginBottom: '2rem' }}>
      <RagChat chapterFilter={chapter} useStreaming />
    </div>
  );
};

export default RagChatPanel;


