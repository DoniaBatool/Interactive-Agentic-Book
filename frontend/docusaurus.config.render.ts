import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// Render Deployment Configuration
// Use this config when deploying to Render
// Copy this to docusaurus.config.ts before deploying to Render

const config: Config = {
  title: 'AI-Native Physical AI & Robotics Textbook',
  tagline: 'Interactive Learning Platform for Physical AI and Humanoid Robotics',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  // Render deployment URL (update with your actual Render URL)
  url: process.env.RENDER_URL || 'https://ai-robotics-textbook-frontend.onrender.com',
  
  // Base URL for Render (no subpath needed)
  baseUrl: '/',
  trailingSlash: false,

  onBrokenLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/',
          editUrl: 'https://github.com/DoniaBatool/Interactive-Agentic-Book/tree/main/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'AI Robotics Textbook',
      logo: {
        alt: 'AI Robotics Textbook Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Chapters',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Chapters',
          items: [
            {
              label: 'Chapter 1',
              to: '/docs/chapters/chapter-1',
            },
            {
              label: 'Chapter 2',
              to: '/docs/chapters/chapter-2',
            },
            {
              label: 'Chapter 3',
              to: '/docs/chapters/chapter-3',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} AI Robotics Textbook. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;

