import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // Main textbook sidebar
  tutorialSidebar: [
    // Introduction
    {
      type: 'doc',
      id: 'chapters/introduction',
      label: 'Introduction',
    },
    
    // Course Modules
    {
      type: 'category',
      label: 'Course Modules',
      collapsible: true,
      collapsed: false,
      items: [
        {
          type: 'doc',
          id: 'chapters/module-1-ros2',
          label: 'Module 1: ROS 2',
        },
        {
          type: 'doc',
          id: 'chapters/module-2-simulation',
          label: 'Module 2: Simulation',
        },
        {
          type: 'doc',
          id: 'chapters/module-3-isaac',
          label: 'Module 3: NVIDIA Isaac',
        },
        {
          type: 'doc',
          id: 'chapters/module-4-vla',
          label: 'Module 4: VLA',
        },
      ],
    },
    
    // Hardware Requirements
    {
      type: 'doc',
      id: 'chapters/hardware-requirements',
      label: 'Hardware Requirements',
    },
  ],
};

export default sidebars;
