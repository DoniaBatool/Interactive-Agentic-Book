import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'AI-Native Physical AI & Robotics Textbook',
  tagline: 'Interactive Learning Platform for Physical AI and Humanoid Robotics',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  // IMPORTANT: Your GitHub Pages URL
  url: 'https://doniabatool.github.io',

  // IMPORTANT: Base URL = repo name with slashes
  baseUrl: '/Interactive-Agentic-Book/',
  trailingSlash: false, // Explicit trailingSlash config for GitHub Pages

  // GitHub pages deployment config
  organizationName: 'DoniaBatool',      // GitHub username
  projectName: 'Interactive-Agentic-Book', // Repo name

  onBrokenLinks: 'warn', // Changed to 'warn' to allow build with external links

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
          
          // Correct GitHub edit URL
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
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Physical AI Textbook',
      logo: {
        alt: 'Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Learn',
        },
        {
          href: 'https://github.com/DoniaBatool/Interactive-Agentic-Book',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} AI-Native Physical AI Textbook. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
