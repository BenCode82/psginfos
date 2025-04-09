import React, { useState, useEffect } from 'react';
import './ScrollToTopButton.css';

const ScrollToTopButton = () => {
  const [showScroll, setShowScroll] = useState(false);

  const checkScroll = () => {
    setShowScroll(window.scrollY > 500);
  };

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  useEffect(() => {
    window.addEventListener("scroll", checkScroll);
    return () => window.removeEventListener("scroll", checkScroll);
  }, []);

  return (
    showScroll && (
      <button onClick={scrollToTop} className="scroll-top-btn">⬆</button>
    )
  );
};

export default ScrollToTopButton;
