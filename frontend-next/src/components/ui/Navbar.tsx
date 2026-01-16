'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';

export function Navbar() {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 100);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <nav 
      className="nav" 
      id="nav"
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        padding: scrolled ? '15px 60px' : '20px 60px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        zIndex: 100,
        background: scrolled ? 'rgba(5, 5, 7, 0.9)' : 'transparent',
        backdropFilter: scrolled ? 'blur(20px)' : 'none',
        borderBottom: scrolled ? '1px solid rgba(99, 102, 241, 0.1)' : 'none',
        transition: 'all 0.3s ease'
      }}
    >
      <div style={{
        display: 'flex',
        alignItems: 'center',
        gap: '12px',
        fontFamily: 'var(--font-display)',
        fontWeight: 600,
        fontSize: '1.25rem'
      }}>
        <div style={{
          width: '40px',
          height: '40px',
          background: 'linear-gradient(135deg, var(--primary), var(--secondary))',
          borderRadius: '10px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          boxShadow: '0 0 20px var(--primary-glow)'
        }}>
          <svg viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2" style={{width: '22px', height: '22px'}}>
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
            <path d="M9 12l2 2 4-4" />
          </svg>
        </div>
        <span>Aptos Shield</span>
      </div>
      <div style={{
        display: 'flex',
        alignItems: 'center',
        gap: '40px'
      }}>
        <a href="#features" style={{
          color: 'var(--text-secondary)',
          textDecoration: 'none',
          fontSize: '0.95rem',
          transition: 'color 0.3s ease'
        }} onMouseEnter={(e) => e.currentTarget.style.color = 'var(--text-primary)'}
           onMouseLeave={(e) => e.currentTarget.style.color = 'var(--text-secondary)'}>Features</a>
        <a href="#demo" style={{
          color: 'var(--text-secondary)',
          textDecoration: 'none',
          fontSize: '0.95rem',
          transition: 'color 0.3s ease'
        }} onMouseEnter={(e) => e.currentTarget.style.color = 'var(--text-primary)'}
           onMouseLeave={(e) => e.currentTarget.style.color = 'var(--text-secondary)'}>Demo</a>
        <a href="#tech" style={{
          color: 'var(--text-secondary)',
          textDecoration: 'none',
          fontSize: '0.95rem',
          transition: 'color 0.3s ease'
        }} onMouseEnter={(e) => e.currentTarget.style.color = 'var(--text-primary)'}
           onMouseLeave={(e) => e.currentTarget.style.color = 'var(--text-secondary)'}>Technology</a>
        <Link href="/scanner" style={{
          color: 'var(--text-secondary)',
          textDecoration: 'none',
          fontSize: '0.95rem',
          transition: 'color 0.3s ease'
        }} onMouseEnter={(e) => e.currentTarget.style.color = 'var(--text-primary)'}
           onMouseLeave={(e) => e.currentTarget.style.color = 'var(--text-secondary)'}>Scanner</Link>
        <Link href="/dashboard" style={{
          padding: '10px 24px',
          background: 'var(--primary)',
          color: 'white',
          borderRadius: '8px',
          fontWeight: 500,
          textDecoration: 'none',
          transition: 'all 0.3s ease'
        }} onMouseEnter={(e) => {
          e.currentTarget.style.background = 'var(--secondary)';
          e.currentTarget.style.transform = 'translateY(-2px)';
          e.currentTarget.style.boxShadow = '0 4px 20px var(--primary-glow)';
        }} onMouseLeave={(e) => {
          e.currentTarget.style.background = 'var(--primary)';
          e.currentTarget.style.transform = 'translateY(0)';
          e.currentTarget.style.boxShadow = 'none';
        }}>Launch App</Link>
      </div>
    </nav>
  );
}
