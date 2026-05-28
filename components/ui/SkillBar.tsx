"use client";

import { useEffect, useRef, useState } from "react";

interface SkillBarProps {
  name: string;
  level: number;
  delay?: number;
}

export default function SkillBar({ name, level, delay = 0 }: SkillBarProps) {
  const [animate, setAnimate] = useState(false);
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const obs = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) setAnimate(true); },
      { threshold: 0.3 }
    );
    if (ref.current) obs.observe(ref.current);
    return () => obs.disconnect();
  }, []);

  return (
    <div ref={ref} style={{ marginBottom: 16 }}>
      <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
        <span style={{ fontSize: 13, color: "#a0aec0", fontFamily: "'Space Mono', monospace" }}>
          {name}
        </span>
        <span style={{ fontSize: 12, color: "#00d4ff", fontFamily: "'Space Mono', monospace" }}>
          {level}%
        </span>
      </div>
      <div style={{ height: 4, background: "#1a1f2e", borderRadius: 2, overflow: "hidden" }}>
        <div
          style={{
            height: "100%",
            width: animate ? `${level}%` : "0%",
            background: "linear-gradient(90deg, #00d4ff, #7c3aed)",
            borderRadius: 2,
            transition: `width 1s ease ${delay}ms`,
            boxShadow: "0 0 8px rgba(0,212,255,0.5)",
          }}
        />
      </div>
    </div>
  );
}