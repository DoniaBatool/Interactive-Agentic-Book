import React from 'react';
import { useLocation } from '@docusaurus/router';
import Content from '@theme-original/DocItem/Content';
import type ContentType from '@theme/DocItem/Content';
import type { WrapperProps } from '@docusaurus/types';
import PersonalizeContent from '../../../components/PersonalizeContent';
import TranslatableContent from '../../../components/TranslatableContent';
import ScrollAnimate from '../../../components/ScrollAnimate';

type Props = WrapperProps<typeof ContentType>;

export default function ContentWrapper(props: Props): React.JSX.Element {
  const location = useLocation();
  // Get chapter title and path from document
  const [chapterPath, setChapterPath] = React.useState<string>('/');
  const [title, setTitle] = React.useState<string | undefined>(undefined);
  
  // Update path and title when location changes
  React.useEffect(() => {
    if (typeof window !== 'undefined') {
      // Get path from URL
      const path = window.location.pathname;
      setChapterPath(path);
      
      // Get title from document with retry logic
      const getTitle = () => {
        const docTitle = document.title.split(' | ')[0] || 
                        document.querySelector('article h1, .markdown h1, h1')?.textContent?.trim() || 
                        undefined;
        return docTitle;
      };
      
      // Try immediately
      let docTitle = getTitle();
      
      // Retry after DOM settles
      if (!docTitle) {
        setTimeout(() => {
          docTitle = getTitle();
          setTitle(docTitle);
        }, 200);
      }
      
      setTitle(docTitle);
      console.log(`ContentWrapper: chapterPath=${path}, title=${docTitle}`);
    }
  }, [location.pathname, location.key]);

  return (
    <>
      <ScrollAnimate animation="fade-up">
        <PersonalizeContent chapterTitle={title} />
      </ScrollAnimate>
      <TranslatableContent chapterPath={chapterPath}>
        <ScrollAnimate animation="fade-up" delay={100}>
          <Content {...props} />
        </ScrollAnimate>
      </TranslatableContent>
    </>
  );
}

