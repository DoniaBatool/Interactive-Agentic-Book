import fs from 'fs';
import path from 'path';

const projectRoot = process.cwd();
const errors = [];

const requiredDocs = [
  {
    file: 'docs/course-overview.md',
    requiredText: [
      'Physical AI & Humanoid Robotics',
      'Learning Outcomes',
      'Weekly Breakdown',
      'Hardware Requirements',
    ],
  },
  {file: 'docs/modules/intro.md'},
  {file: 'docs/modules/ros2.md'},
  {file: 'docs/modules/gazebo-unity.md'},
  {file: 'docs/modules/nvidia-isaac.md'},
  {file: 'docs/modules/vla-capstone.md'},
];

const sidebarFile = 'sidebars.ts';

function assertFileExists(relPath) {
  const abs = path.join(projectRoot, relPath);
  if (!fs.existsSync(abs)) {
    errors.push(`Missing file: ${relPath}`);
    return null;
  }
  return abs;
}

function assertFileContains(relPath, requiredSnippets) {
  const abs = assertFileExists(relPath);
  if (!abs) return;
  const content = fs.readFileSync(abs, 'utf8');
  requiredSnippets.forEach((snippet) => {
    if (!content.includes(snippet)) {
      errors.push(`File ${relPath} missing required text: "${snippet}"`);
    }
  });
}

requiredDocs.forEach((doc) => {
  if (doc.requiredText) {
    assertFileContains(doc.file, doc.requiredText);
  } else {
    assertFileExists(doc.file);
  }
});

assertFileContains(sidebarFile, [
  'course-overview',
  'modules/intro',
  'modules/ros2',
  'modules/gazebo-unity',
  'modules/nvidia-isaac',
  'modules/vla-capstone',
]);

if (errors.length > 0) {
  console.error('Course structure checks failed:\n- ' + errors.join('\n- '));
  process.exit(1);
} else {
  console.log('Course structure checks passed.');
}

