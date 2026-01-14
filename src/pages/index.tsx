import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import RobotHero from '../../static/img/robot-hero.svg';
import ScrollAnimate from '../components/ScrollAnimate';
import { useTranslation } from '../lib/i18n';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  const { t } = useTranslation();
  return (
    <header className="hero hero--primary hero--tech">
      <div className="container hero__grid">
        <ScrollAnimate animation="fade-up" className="hero-animate">
          <div>
            <Heading as="h1" className="hero__title">
              {siteConfig.title}
            </Heading>
            <p className="hero__subtitle">{t('home.tagline')}</p>
            <div className="button-group">
              <Link className="button button--secondary button--lg" to="/docs/course-overview">
                {t('home.startCourse')}
              </Link>
              <Link className="button button--outline button--lg" to="/docs/modules/vla-capstone">
                {t('home.seeCapstone')}
              </Link>
            </div>
          </div>
        </ScrollAnimate>
        <div className="hero__metrics">
          <ScrollAnimate animation="fade-left" delay={200}>
            <div className="metric-card animated-card">
              <span className="metric-label">{t('home.stackLabel')}</span>
              <span className="metric-value">{t('home.stackValue')}</span>
            </div>
          </ScrollAnimate>
          <ScrollAnimate animation="fade-right" delay={300}>
            <div className="metric-card animated-card">
              <span className="metric-label">{t('home.focusLabel')}</span>
              <span className="metric-value">{t('home.focusValue')}</span>
            </div>
          </ScrollAnimate>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const { t } = useTranslation();

  return (
    <Layout description="Physical AI & Humanoid Robotics textbook built with Docusaurus">
      <HomepageHeader />
      <main className="hero-visual">
        <ScrollAnimate animation="fade-left" delay={400}>
          <div className="hero-visual__card animated-card">
            <div className="hero-visual__header">{t('home.embodiedArchitectureTitle')}</div>
            <ul>
              <li>{t('home.embodiedArchitectureItem1')}</li>
              <li>{t('home.embodiedArchitectureItem2')}</li>
              <li>{t('home.embodiedArchitectureItem3')}</li>
              <li>{t('home.embodiedArchitectureItem4')}</li>
            </ul>
          </div>
        </ScrollAnimate>
        <ScrollAnimate animation="fade-right" delay={500}>
          <div className="hero-visual__image">
            <RobotHero className="hero-visual__svg" role="img" aria-label="Humanoid robotics architecture illustration" />
          </div>
        </ScrollAnimate>
      </main>
    </Layout>
  );
}
