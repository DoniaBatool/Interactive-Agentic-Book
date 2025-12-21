import React, { useEffect, useRef, useState, ReactNode } from 'react';

interface ScrollAnimateProps {
  children: ReactNode;
  animation?: 'fade-up' | 'fade-left' | 'fade-right' | 'scale' | 'rotate';
  delay?: number;
  className?: string;
  threshold?: number;
  rootMargin?: string;
}

export const ScrollAnimate: React.FC<ScrollAnimateProps> = ({
  children,
  animation = 'fade-up',
  delay = 0,
  className = '',
  threshold = 0.1,
  rootMargin = '0px 0px -100px 0px',
}) => {
  const [isVisible, setIsVisible] = useState(false);
  const elementRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            // Add delay if specified
            setTimeout(() => {
              setIsVisible(true);
            }, delay);
            // Unobserve after animation triggers
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold,
        rootMargin,
      }
    );

    const currentElement = elementRef.current;
    if (currentElement) {
      observer.observe(currentElement);
    }

    return () => {
      if (currentElement) {
        observer.unobserve(currentElement);
      }
    };
  }, [delay, threshold, rootMargin]);

  const animationClass = `animate-${animation}`;
  const delayClass = delay > 0 ? `delay-${Math.min(delay, 500)}` : '';

  return (
    <div
      ref={elementRef}
      className={`scroll-animate ${isVisible ? animationClass : ''} ${delayClass} ${className}`}
    >
      {children}
    </div>
  );
};

export default ScrollAnimate;

