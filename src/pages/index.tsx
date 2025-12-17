import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import RobotHero from '../../static/img/robot-hero.svg';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className="hero hero--primary hero--tech">
      <div className="container hero__grid">
        <div>
          <Heading as="h1" className="hero__title">
            {siteConfig.title}
          </Heading>
          <p className="hero__subtitle">{siteConfig.tagline}</p>
          <div className="button-group">
            <Link className="button button--secondary button--lg" to="/docs/course-overview">
              Start the Course
            </Link>
            <Link className="button button--outline button--lg" to="/docs/modules/vla-capstone">
              See the Capstone
            </Link>
          </div>
        </div>
        <div className="hero__metrics">
          <div className="metric-card">
            <span className="metric-label">Stack</span>
            <span className="metric-value">ROS 2 • Gazebo • Isaac • VLA</span>
          </div>
          <div className="metric-card">
            <span className="metric-label">Focus</span>
            <span className="metric-value">Embodied AI & Humanoid Robotics</span>
          </div>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  return (
    <Layout description="Physical AI & Humanoid Robotics textbook built with Docusaurus">
      <HomepageHeader />
      <main className="hero-visual">
        <div className="hero-visual__card">
          <div className="hero-visual__header">Embodied Architecture</div>
          <ul>
            <li>ROS 2 control plane with nodes, topics, and services</li>
            <li>Gazebo/Unity digital twin for physics + visualization</li>
            <li>NVIDIA Isaac for perception, VSLAM, and navigation</li>
            <li>Vision-Language-Action: voice-to-action and planning</li>
          </ul>
        </div>
        <div className="hero-visual__image">
          <RobotHero className="hero-visual__svg" role="img" aria-label="Humanoid robotics architecture illustration" />
        </div>
      </main>
    </Layout>
  );
}

