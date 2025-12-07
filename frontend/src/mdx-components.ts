/**
 * MDX Components Mapping
 * 
 * Global component mapping for Docusaurus MDX files.
 * This file allows AI block components to be used directly in MDX without explicit imports.
 * 
 * Note: If this approach doesn't work with Docusaurus 3.x, use the swizzle approach:
 * 1. Run: npm run swizzle @docusaurus/theme-classic MDXComponents
 * 2. Update src/theme/MDXComponents.tsx to include these components
 */

import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';

/**
 * Default export for MDX component mapping.
 * 
 * Components can be used in MDX files like:
 * ```mdx
 * <AskQuestionBlock chapterId={1} sectionId="what-is-physical-ai" />
 * ```
 * 
 * Components support Chapter 1 (chapterId=1), Chapter 2 (chapterId=2), and Chapter 3 (chapterId=3).
 * Chapter 2 usage: <AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />
 * Chapter 3 usage: <AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />
 */
export default {
  AskQuestionBlock,
  ExplainLike10Block,
  InteractiveQuizBlock,
  GenerateDiagramBlock,
};

