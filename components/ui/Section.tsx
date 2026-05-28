"use client";

import { useEffect, useRef, useState } from "react";
import type { CSSProperties } from "react";

interface SectionProps {
  id: string;
  children: React.ReactNode;
  style?: CSSProperties;
}

export default function Section({ id, children, style }: SectionProps) {
  const [visible, setVisible] = useState(false);
  const ref = useRef<HTMLElement | null>(null);

  useEffect(() => {
    const obs = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) setVisible(true); },
      { threshold: 0.05 }
    );
    if (ref.current) obs.observe(ref.current);
    return () => obs.disconnect();
  }, []);

  return (
    <section
      id={id}
      ref={ref}
      style={{
        maxWidth: 900,
        margin: "0 auto",
        padding: "100px 24px",
        opacity: visible ? 1 : 0,
        transform: visible ? "translateY(0)" : "translateY(20px)",
        transition: "opacity 0.7s ease, transform 0.7s ease",
        ...style,
      }}
    >
      {children}
    </section>
  );
}