# Frontend - Docusaurus Documentation Site

This directory contains the **Docusaurus-powered frontend** for the AI-Native Physical AI & Robotics Textbook.

## Quick Start

### Development

```bash
# Install dependencies
npm install

# Start development server
npm start
# Open http://localhost:3000
```

### Building

```bash
# Build static site
npm run build

# Serve built site locally
npm run serve
# Open http://localhost:3000
```

## Structure

```
frontend/
├── docs/               # Documentation pages (MDX)
│   └── intro.md        # Homepage content
├── src/
│   ├── components/     # React components (placeholder)
│   ├── theme/          # Docusaurus theme customization (placeholder)
│   ├── styles/         # Global CSS/SCSS (placeholder)
│   ├── agents/         # Frontend AI agent helpers (placeholder)
│   └── css/            # Docusaurus default styles
├── static/             # Static assets (images, files)
│   └── img/            # Images
├── docusaurus.config.ts  # Docusaurus configuration
├── sidebars.ts         # Sidebar navigation configuration
└── package.json        # Dependencies and scripts
```

## Key Concepts

### Docusaurus

**Docusaurus** is a static site generator optimized for documentation:
- Built with React and MDX (Markdown + JSX)
- Fast, SEO-friendly, accessibility-focused
- Versioning, i18n, search built-in
- Easy customization with React components

### MDX

MDX combines **Markdown** with **JSX**:

```mdx
# My Page

This is markdown content.

import MyComponent from '@site/src/components/MyComponent';

<MyComponent />
```

### Configuration

**`docusaurus.config.ts`** contains all site configuration:
- Site metadata (title, tagline, URL)
- Theme configuration (navbar, footer, colors)
- Plugin configuration (docs, blog, search)
- i18n settings (prepared for English/Urdu)

## Adding Content

### Create a New Page

1. **Add MDX file** in `docs/`:
   ```bash
   # docs/chapter-1.md
   ---
   sidebar_position: 2
   ---
   
   # Chapter 1: Introduction
   
   Content here...
   ```

2. **Update sidebar** (auto-generated or manual in `sidebars.ts`)

3. **Hot reload** - changes appear immediately in dev server

### Add a React Component

1. **Create component** in `src/components/`:
   ```tsx
   // src/components/MyButton.tsx
   export default function MyButton({label}: {label: string}) {
     return <button>{label}</button>;
   }
   ```

2. **Use in MDX**:
   ```mdx
   import MyButton from '@site/src/components/MyButton';
   
   <MyButton label="Click Me" />
   ```

### Customize Theme

**Swizzle** Docusaurus components:

```bash
# Eject a component for customization
npm run swizzle @docusaurus/theme-classic ComponentName

# Example: Customize NavBar
npm run swizzle @docusaurus/theme-classic NavBar
```

Customized components go in `src/theme/`.

## Scripts

- **`npm start`**: Start development server (hot reload)
- **`npm run build`**: Build static site for production
- **`npm run serve`**: Serve built site locally
- **`npm run clear`**: Clear Docusaurus cache
- **`npm run deploy`**: Deploy to GitHub Pages

## Internationalization (i18n)

Prepared for **English ↔ Urdu** translation:

1. **Add locale** in `docusaurus.config.ts`:
   ```ts
   i18n: {
     defaultLocale: 'en',
     locales: ['en', 'ur'],
   }
   ```

2. **Translate content**:
   ```bash
   npm run write-translations -- --locale ur
   ```

3. **Run with locale**:
   ```bash
   npm run start -- --locale ur
   ```

See [Docusaurus i18n docs](https://docusaurus.io/docs/i18n/introduction) for details.

## Deployment

### GitHub Pages

1. **Configure** in `docusaurus.config.ts`:
   ```ts
   url: 'https://your-username.github.io',
   baseUrl: '/interactive-agentic-book/',
   organizationName: 'your-username',
   projectName: 'interactive-agentic-book',
   ```

2. **Deploy**:
   ```bash
   GIT_USER=your-username npm run deploy
   ```

### Vercel / Netlify

1. **Build command**: `npm run build`
2. **Publish directory**: `build`
3. **Node version**: 18+

## Best Practices

1. **Keep docs/ organized**: Use folders for chapters/sections
2. **Use frontmatter**: Control sidebar position, title, description
3. **Optimize images**: Compress images before adding to `static/img/`
4. **Test builds**: Run `npm run build` before deploying
5. **Follow MDX syntax**: Ensure proper JSX formatting
6. **Use TypeScript**: Type-check custom components

## Troubleshooting

### "Cannot resolve '@site/...'"

**Cause**: Invalid import path in MDX

**Solution**: Use `@site` prefix for src/ imports:
```mdx
import Component from '@site/src/components/Component';
```

### Build fails with "Cannot find module"

**Cause**: Missing dependency or typo in import

**Solution**:
```bash
# Clear cache and reinstall
npm run clear
rm -rf node_modules package-lock.json
npm install
```

### Styles not applying

**Cause**: CSS not loaded or conflicting styles

**Solution**: Import custom CSS in `docusaurus.config.ts`:
```ts
theme: {
  customCss: './src/css/custom.css',
}
```

### Hot reload not working

**Cause**: File watcher issues

**Solution**:
```bash
# Restart dev server
npm start
```

## Resources

- [Docusaurus Documentation](https://docusaurus.io/docs)
- [MDX Documentation](https://mdxjs.com/)
- [React Documentation](https://react.dev/)
- [Project Root README](../README.md)
- [Quickstart Guide](../specs/001-base-project-init/quickstart.md)

## Future Features

Prepared placeholders for:
- **AI Chatbot Integration**: Frontend UI for RAG chatbot
- **Translation Toggle**: Switch between English/Urdu
- **User Dashboard**: Personalized learning progress
- **Interactive Components**: Code sandboxes, quizzes, diagrams
- **Theme Customization**: Dark mode, colors, fonts
