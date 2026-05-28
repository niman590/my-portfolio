"use client";

import { useEffect, useRef, useState } from "react";
import { PROJECTS } from "@/lib/data";

interface ProjectCardProps {
  project: (typeof PROJECTS)[number];
  index: number;
}

export default function ProjectCard({ project, index }: ProjectCardProps) {
  const [hovered, setHovered] = useState(false);
  const [visible, setVisible] = useState(false);
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const obs = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) setVisible(true); },
      { threshold: 0.1 }
    );
    if (ref.current) obs.observe(ref.current);
    return () => obs.disconnect();
  }, []);

  return (
    <div
      ref={ref}
      style={{
        opacity: visible ? 1 : 0,
        transform: visible ? "translateY(0)" : "translateY(40px)",
        background: hovered ? "#0d1117" : "#080c14",
        border: `1px solid ${hovered ? project.color : "rgba(255,255,255,0.06)"}`,
        borderRadius: 12,
        padding: "28px 28px 24px",
        cursor: "default",
        boxShadow: hovered ? `0 0 30px ${project.color}22` : "none",
        transition: `all 0.3s ease, opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`,
      }}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
    >
      <div style={{ display: "flex", alignItems: "flex-start", gap: 14, marginBottom: 16 }}>
        <span style={{ fontSize: 28, animation: "float 3s ease-in-out infinite" }}>
          {project.icon}
        </span>
        <div style={{ flex: 1 }}>
          <h3
            style={{
              margin: 0,
              fontSize: 17,
              fontWeight: 600,
              color: "#e2e8f0",
              fontFamily: "'Syne', sans-serif",
              lineHeight: 1.3,
            }}
          >
            {project.title}
          </h3>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 6, marginTop: 8 }}>
            {project.tags.map((tag) => (
              <span
                key={tag}
                style={{
                  fontSize: 11,
                  padding: "2px 10px",
                  borderRadius: 20,
                  background: `${project.color}18`,
                  color: project.color,
                  border: `1px solid ${project.color}40`,
                  fontFamily: "'Space Mono', monospace",
                }}
              >
                {tag}
              </span>
            ))}
          </div>
        </div>
      </div>

      <ul style={{ margin: 0, paddingLeft: 0, listStyle: "none" }}>
        {project.bullets.map((bullet, i) => (
          <li
            key={i}
            style={{ display: "flex", gap: 10, marginBottom: 8, fontSize: 13, color: "#718096", lineHeight: 1.5 }}
          >
            <span style={{ color: project.color, flexShrink: 0, marginTop: 1 }}>▸</span>
            <span>{bullet}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}