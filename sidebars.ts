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
  courseSidebar: [
    {
      type: 'doc',
      id: 'course-overview',
      label: 'Course Overview',
    },
    {
      type: 'category',
      label: 'Modules',
      items: [
        'modules/intro',
        'modules/ros2',
        'modules/gazebo-unity',
        'modules/nvidia-isaac',
        'modules/vla-capstone',
      ],
    },
  ],
};

export default sidebars;
