import { useEffect, useRef, type ReactNode } from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import gsap from 'gsap';
import RobotImg1 from '../../static/img/robot_img1.png';
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
  const robotRef = useRef<HTMLImageElement | null>(null);

  useEffect(() => {
    if (typeof window === 'undefined') return;
    const el = robotRef.current;
    if (!el) return;

    const reduceMotion = window.matchMedia?.('(prefers-reduced-motion: reduce)')?.matches;
    if (reduceMotion) return;

    const ctx = gsap.context(() => {
      gsap.set(el, { transformOrigin: '50% 50%' });
      gsap.fromTo(
        el,
        { opacity: 0, y: 16, scale: 0.98 },
        { opacity: 1, y: 0, scale: 1, duration: 0.8, ease: 'power2.out' }
      );

      // Gentle float loop
      gsap.to(el, {
        y: -10,
        duration: 3.2,
        ease: 'sine.inOut',
        yoyo: true,
        repeat: -1,
      });
    });

    return () => ctx.revert();
  }, []);

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
            <img
              ref={robotRef}
              src={RobotImg1}
              className="hero-visual__svg"
              alt="Humanoid robotics illustration"
              loading="eager"
              decoding="async"
            />
          </div>
        </ScrollAnimate>
      </main>
    </Layout>
  );
}
