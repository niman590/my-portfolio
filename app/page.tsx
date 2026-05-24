"use client";

import { useEffect, useRef, useState } from "react";
import type { CSSProperties } from "react";

const NAV_LINKS = ["Home", "About", "Skills", "Projects", "Contact"];

const SKILLS_TECH = [
  { name: "Python", level: 85 },
  { name: "C++", level: 75 },
  { name: "Dart", level: 70 },
  { name: "Ruby", level: 65 },
  { name: "Flutter", level: 72 },
  { name: "Ruby on Rails", level: 65 },
  { name: "gRPC", level: 68 },
  { name: "SQLite / SQL", level: 80 },
];

const SKILLS_SOFT = [
  "Problem-solving",
  "Communication",
  "Teamwork",
  "Time management",
  "Adaptability",
  "Quick learning",
];

const PROJECTS = [
  {
    title: "Distributed Banking System",
    tags: ["Python", "gRPC", "SQLite"],
    color: "#00d4ff",
    icon: "🏦",
    bullets: [
      "3-tier architecture: Client, Application Server, Database Server",
      "Remote procedure calls (RPC) for inter-service communication",
      "Secure user authentication with token-based session management",
      "Transaction processing with validation and fee computation",
      "SQLite-backed persistent data storage layer",
    ],
  },
  {
    title: "Flutter Tic Tac Toe Game",
    tags: ["Dart", "Flutter"],
    color: "#7c3aed",
    icon: "🎮",
    bullets: [
      "Cross-platform mobile game for Android and iOS",
      "Full game logic, UI design, and multiple difficulty levels",
    ],
  },
  {
    title: "Quotes Web Application",
    tags: ["Ruby on Rails", "SQL"],
    color: "#10b981",
    icon: "💬",
    bullets: [
      "Role-based access control and secure authentication",
      "SQL database for quote storage and management",
    ],
  },
  {
    title: "C++ Dictionary Search",
    tags: ["C++"],
    color: "#f59e0b",
    icon: "📖",
    bullets: [
      "Word management system with types and definitions",
      "Search functionality, file handling, and random word selection",
    ],
  },
];

const EDUCATION = [
  {
    degree: "Bachelor of Computer Science (Software Engineering)",
    school: "Edith Cowan University, Rajagiriya",
    period: "Nov 2023 – Present",
    note: "Final semester of 3rd year",
  },
  {
    degree: "Foundation Certificate in Information Technology",
    school: "Edith Cowan University, Rajagiriya",
    period: "July 2022 – Nov 2023",
  },
  {
    degree: "GCE Ordinary Level",
    school: "Isipathana College, Colombo 05",
    period: "2021 (2022)",
  },
];

function Grid() {
  return (
    <div
      style={{
        position: "fixed",
        inset: 0,
        zIndex: 0,
        pointerEvents: "none",
        backgroundImage: `
          linear-gradient(rgba(0,212,255,0.03) 1px, transparent 1px),
          linear-gradient(90deg, rgba(0,212,255,0.03) 1px, transparent 1px)
        `,
        backgroundSize: "60px 60px",
      }}
    />
  );
}

function GlitchText({
  text,
  style,
}: {
  text: string;
  style?: CSSProperties;
}) {
  return (
    <span style={{ position: "relative", display: "inline-block", ...style }}>
      <style>{`
        @keyframes glitch1 {
          0%,100%{clip-path:inset(0 0 95% 0);transform:translate(-2px,0)}
          20%{clip-path:inset(30% 0 50% 0);transform:translate(2px,0)}
          40%{clip-path:inset(60% 0 20% 0);transform:translate(-1px,0)}
          60%{clip-path:inset(80% 0 5% 0);transform:translate(2px,0)}
          80%{clip-path:inset(10% 0 75% 0);transform:translate(-2px,0)}
        }

        @keyframes glitch2 {
          0%,100%{clip-path:inset(80% 0 5% 0);transform:translate(2px,0)}
          20%{clip-path:inset(10% 0 75% 0);transform:translate(-2px,0)}
          40%{clip-path:inset(0 0 95% 0);transform:translate(2px,0)}
          60%{clip-path:inset(30% 0 50% 0);transform:translate(-2px,0)}
          80%{clip-path:inset(60% 0 20% 0);transform:translate(1px,0)}
        }

        @keyframes fadeUp {
          from{opacity:0;transform:translateY(30px)}
          to{opacity:1;transform:translateY(0)}
        }

        @keyframes blink {
          0%,100%{opacity:1}
          50%{opacity:0}
        }

        @keyframes float {
          0%,100%{transform:translateY(0px)}
          50%{transform:translateY(-8px)}
        }
      `}</style>

      {text}

      <span
        aria-hidden
        style={{
          position: "absolute",
          inset: 0,
          color: "#00d4ff",
          animation: "glitch1 4s infinite",
        }}
      >
        {text}
      </span>

      <span
        aria-hidden
        style={{
          position: "absolute",
          inset: 0,
          color: "#7c3aed",
          animation: "glitch2 4s infinite 0.2s",
        }}
      >
        {text}
      </span>
    </span>
  );
}

function SkillBar({
  name,
  level,
  delay = 0,
}: {
  name: string;
  level: number;
  delay?: number;
}) {
  const [animate, setAnimate] = useState(false);
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const obs = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) setAnimate(true);
      },
      { threshold: 0.3 }
    );

    if (ref.current) obs.observe(ref.current);

    return () => obs.disconnect();
  }, []);

  return (
    <div ref={ref} style={{ marginBottom: 16 }}>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          marginBottom: 6,
        }}
      >
        <span
          style={{
            fontSize: 13,
            color: "#a0aec0",
            fontFamily: "'Space Mono', monospace",
          }}
        >
          {name}
        </span>

        <span
          style={{
            fontSize: 12,
            color: "#00d4ff",
            fontFamily: "'Space Mono', monospace",
          }}
        >
          {level}%
        </span>
      </div>

      <div
        style={{
          height: 4,
          background: "#1a1f2e",
          borderRadius: 2,
          overflow: "hidden",
        }}
      >
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

function ProjectCard({
  project,
  index,
}: {
  project: (typeof PROJECTS)[number];
  index: number;
}) {
  const [hovered, setHovered] = useState(false);
  const [visible, setVisible] = useState(false);
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const obs = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) setVisible(true);
      },
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
        border: `1px solid ${
          hovered ? project.color : "rgba(255,255,255,0.06)"
        }`,
        borderRadius: 12,
        padding: "28px 28px 24px",
        cursor: "default",
        boxShadow: hovered ? `0 0 30px ${project.color}22` : "none",
        transition: `all 0.3s ease, opacity 0.6s ease ${
          index * 0.1
        }s, transform 0.6s ease ${index * 0.1}s`,
      }}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
    >
      <div
        style={{
          display: "flex",
          alignItems: "flex-start",
          gap: 14,
          marginBottom: 16,
        }}
      >
        <span
          style={{
            fontSize: 28,
            animation: "float 3s ease-in-out infinite",
          }}
        >
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

          <div
            style={{
              display: "flex",
              flexWrap: "wrap",
              gap: 6,
              marginTop: 8,
            }}
          >
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
            style={{
              display: "flex",
              gap: 10,
              marginBottom: 8,
              fontSize: 13,
              color: "#718096",
              lineHeight: 1.5,
            }}
          >
            <span
              style={{
                color: project.color,
                flexShrink: 0,
                marginTop: 1,
              }}
            >
              ▸
            </span>
            <span>{bullet}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

function Section({
  id,
  children,
  style,
}: {
  id: string;
  children: React.ReactNode;
  style?: CSSProperties;
}) {
  const [visible, setVisible] = useState(false);
  const ref = useRef<HTMLElement | null>(null);

  useEffect(() => {
    const obs = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) setVisible(true);
      },
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

function SectionLabel({ children }: { children: React.ReactNode }) {
  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        gap: 16,
        marginBottom: 48,
      }}
    >
      <span
        style={{
          fontFamily: "'Space Mono', monospace",
          fontSize: 12,
          color: "#00d4ff",
          letterSpacing: 3,
        }}
      >
        {children}
      </span>

      <div
        style={{
          flex: 1,
          height: 1,
          background: "linear-gradient(90deg, rgba(0,212,255,0.4), transparent)",
        }}
      />
    </div>
  );
}

export default function Portfolio() {
  const [activeSection, setActiveSection] = useState("Home");
  const [cursorPos, setCursorPos] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const move = (event: MouseEvent) => {
      setCursorPos({ x: event.clientX, y: event.clientY });
    };

    window.addEventListener("mousemove", move);

    return () => window.removeEventListener("mousemove", move);
  }, []);

  useEffect(() => {
    const handleScroll = () => {
      const sections = NAV_LINKS.map((name) => document.getElementById(name));
      const scrollY = window.scrollY + 200;

      sections.forEach((section, index) => {
        if (
          section &&
          section.offsetTop <= scrollY &&
          section.offsetTop + section.offsetHeight > scrollY
        ) {
          setActiveSection(NAV_LINKS[index]);
        }
      });
    };

    window.addEventListener("scroll", handleScroll);
    handleScroll();

    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const scrollTo = (id: string) => {
    document.getElementById(id)?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <div
      style={{
        background: "#050810",
        minHeight: "100vh",
        color: "#e2e8f0",
        fontFamily: "'DM Sans', sans-serif",
        position: "relative",
        overflowX: "hidden",
      }}
    >
      <link
        href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500&display=swap"
        rel="stylesheet"
      />

      <div
        style={{
          position: "fixed",
          zIndex: 9999,
          pointerEvents: "none",
          left: cursorPos.x - 150,
          top: cursorPos.y - 150,
          width: 300,
          height: 300,
          borderRadius: "50%",
          background:
            "radial-gradient(circle, rgba(0,212,255,0.06) 0%, transparent 70%)",
          transition: "left 0.1s, top 0.1s",
        }}
      />

      <Grid />

      <nav
        style={{
          position: "fixed",
          top: 0,
          left: 0,
          right: 0,
          zIndex: 100,
          background: "rgba(5,8,16,0.85)",
          backdropFilter: "blur(12px)",
          borderBottom: "1px solid rgba(0,212,255,0.08)",
          padding: "0 32px",
          height: 64,
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <span
          style={{
            fontFamily: "'Space Mono', monospace",
            fontSize: 14,
            color: "#00d4ff",
            letterSpacing: 2,
          }}
        >
          NNR<span style={{ color: "#7c3aed" }}>_</span>
        </span>

        <div style={{ display: "flex", gap: 4 }}>
          {NAV_LINKS.map((link) => (
            <button
              key={link}
              onClick={() => scrollTo(link)}
              style={{
                background: "none",
                border: "none",
                cursor: "pointer",
                padding: "6px 14px",
                fontFamily: "'Space Mono', monospace",
                fontSize: 12,
                letterSpacing: 1,
                color: activeSection === link ? "#00d4ff" : "#718096",
                borderBottom:
                  activeSection === link
                    ? "1px solid #00d4ff"
                    : "1px solid transparent",
                transition: "all 0.2s",
              }}
            >
              {link}
            </button>
          ))}
        </div>
      </nav>

      <section
        id="Home"
        style={{
          minHeight: "100vh",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          position: "relative",
          padding: "0 24px",
          textAlign: "center",
        }}
      >
        <div
          style={{
            position: "absolute",
            top: "50%",
            left: "50%",
            transform: "translate(-50%,-50%)",
            width: 600,
            height: 600,
            background:
              "radial-gradient(circle, rgba(0,212,255,0.07) 0%, transparent 70%)",
            pointerEvents: "none",
          }}
        />

        <div
          style={{
            position: "relative",
            zIndex: 1,
            animation: "fadeUp 1s ease both",
          }}
        >
          <div
            style={{
              fontFamily: "'Space Mono', monospace",
              fontSize: 12,
              color: "#00d4ff",
              letterSpacing: 4,
              marginBottom: 24,
              opacity: 0.8,
            }}
          >
            &lt; FRONTEND DEVELOPER /&gt;
          </div>

          <h1
            style={{
              margin: "0 0 8px",
              fontFamily: "'Syne', sans-serif",
              fontSize: "clamp(42px, 8vw, 80px)",
              fontWeight: 800,
              lineHeight: 1.05,
              color: "#f7fafc",
            }}
          >
            <GlitchText text="NIMAN" />
            <br />
            <span style={{ color: "#00d4ff" }}>NETHMIKA</span>
          </h1>

          <div
            style={{
              fontFamily: "'Space Mono', monospace",
              fontSize: 14,
              color: "#718096",
              marginBottom: 32,
              marginTop: 12,
            }}
          >
            <span style={{ animation: "blink 1s infinite" }}>▮</span> Computer
            Science Undergraduate · Software Engineer
          </div>

          <p
            style={{
              maxWidth: 540,
              margin: "0 auto 48px",
              fontSize: 15,
              color: "#718096",
              lineHeight: 1.8,
              fontWeight: 300,
            }}
          >
            Motivated CS undergraduate specializing in Software Engineering.
            Passionate about building scalable, secure, and user-friendly
            applications.
          </p>

          <div
            style={{
              display: "flex",
              gap: 16,
              justifyContent: "center",
              flexWrap: "wrap",
            }}
          >
            <button
              onClick={() => scrollTo("Projects")}
              style={{
                padding: "12px 32px",
                borderRadius: 6,
                border: "none",
                cursor: "pointer",
                background: "linear-gradient(135deg, #00d4ff, #7c3aed)",
                color: "#fff",
                fontFamily: "'Space Mono', monospace",
                fontSize: 12,
                letterSpacing: 2,
                boxShadow: "0 0 20px rgba(0,212,255,0.3)",
                transition: "all 0.2s",
              }}
            >
              VIEW PROJECTS
            </button>

            <button
              onClick={() => scrollTo("Contact")}
              style={{
                padding: "12px 32px",
                borderRadius: 6,
                border: "1px solid rgba(0,212,255,0.3)",
                cursor: "pointer",
                background: "transparent",
                color: "#00d4ff",
                fontFamily: "'Space Mono', monospace",
                fontSize: 12,
                letterSpacing: 2,
                transition: "all 0.2s",
              }}
            >
              CONTACT ME
            </button>
          </div>

          <div
            style={{
              display: "flex",
              gap: 24,
              justifyContent: "center",
              marginTop: 56,
              opacity: 0.5,
              flexWrap: "wrap",
            }}
          >
            {[
              { label: "nimannethmika@gmail.com", icon: "✉" },
              { label: "+94 77 593 4822", icon: "☎" },
              { label: "Kaduwela, LK", icon: "◎" },
            ].map(({ label, icon }) => (
              <span
                key={label}
                style={{
                  fontFamily: "'Space Mono', monospace",
                  fontSize: 11,
                  color: "#718096",
                  display: "flex",
                  alignItems: "center",
                  gap: 6,
                }}
              >
                <span style={{ color: "#00d4ff" }}>{icon}</span>
                {label}
              </span>
            ))}
          </div>
        </div>
      </section>

      <Section id="About">
        <SectionLabel>01. ABOUT_ME</SectionLabel>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
            gap: 48,
            alignItems: "start",
          }}
        >
          <div>
            <h2
              style={{
                fontFamily: "'Syne', sans-serif",
                fontSize: 36,
                fontWeight: 700,
                margin: "0 0 24px",
                lineHeight: 1.2,
              }}
            >
              Building the web,
              <br />
              <span style={{ color: "#00d4ff" }}>one commit</span> at a time.
            </h2>

            <p
              style={{
                color: "#718096",
                lineHeight: 1.9,
                fontSize: 14,
                marginBottom: 20,
              }}
            >
              I'm a motivated and detail-oriented Computer Science undergraduate
              specializing in Software Engineering at Edith Cowan University,
              currently in the final semester of my 3rd year.
            </p>

            <p
              style={{
                color: "#718096",
                lineHeight: 1.9,
                fontSize: 14,
              }}
            >
              I possess strong foundational knowledge in software development,
              distributed systems, and full-stack development — demonstrated
              through multiple academic and personal projects.
            </p>

            <div
              style={{
                display: "flex",
                gap: 16,
                marginTop: 32,
                flexWrap: "wrap",
              }}
            >
              {[
                { label: "Languages", value: "Sinhala · English" },
                { label: "Focus", value: "Frontend Dev" },
              ].map(({ label, value }) => (
                <div
                  key={label}
                  style={{
                    flex: 1,
                    minWidth: 180,
                    background: "#0d1117",
                    border: "1px solid rgba(255,255,255,0.06)",
                    borderRadius: 8,
                    padding: "16px 20px",
                  }}
                >
                  <div
                    style={{
                      fontSize: 11,
                      color: "#00d4ff",
                      fontFamily: "'Space Mono', monospace",
                      letterSpacing: 2,
                      marginBottom: 6,
                    }}
                  >
                    {label}
                  </div>
                  <div style={{ fontSize: 13, color: "#a0aec0" }}>{value}</div>
                </div>
              ))}
            </div>
          </div>

          <div>
            <div
              style={{
                fontSize: 11,
                fontFamily: "'Space Mono', monospace",
                color: "#00d4ff",
                letterSpacing: 2,
                marginBottom: 20,
              }}
            >
              EDUCATION
            </div>

            {EDUCATION.map((item, index) => (
              <div
                key={index}
                style={{
                  position: "relative",
                  paddingLeft: 24,
                  marginBottom: 28,
                  borderLeft: "1px solid rgba(0,212,255,0.2)",
                }}
              >
                <div
                  style={{
                    position: "absolute",
                    left: -5,
                    top: 5,
                    width: 8,
                    height: 8,
                    borderRadius: "50%",
                    background: "#00d4ff",
                    boxShadow: "0 0 8px #00d4ff",
                  }}
                />

                <div
                  style={{
                    fontSize: 13,
                    fontWeight: 500,
                    color: "#e2e8f0",
                    marginBottom: 4,
                    lineHeight: 1.4,
                  }}
                >
                  {item.degree}
                </div>

                <div
                  style={{
                    fontSize: 12,
                    color: "#4a5568",
                    marginBottom: 2,
                  }}
                >
                  {item.school}
                </div>

                <div
                  style={{
                    fontFamily: "'Space Mono', monospace",
                    fontSize: 11,
                    color: "#7c3aed",
                  }}
                >
                  {item.period}
                </div>

                {"note" in item && item.note && (
                  <div
                    style={{
                      fontSize: 11,
                      color: "#00d4ff",
                      marginTop: 4,
                      fontStyle: "italic",
                    }}
                  >
                    {item.note}
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </Section>

      <Section id="Skills">
        <SectionLabel>02. SKILLS</SectionLabel>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
            gap: 48,
          }}
        >
          <div>
            <div
              style={{
                fontSize: 11,
                fontFamily: "'Space Mono', monospace",
                color: "#7c3aed",
                letterSpacing: 2,
                marginBottom: 28,
              }}
            >
              TECHNICAL
            </div>

            {SKILLS_TECH.map((skill, index) => (
              <SkillBar
                key={skill.name}
                name={skill.name}
                level={skill.level}
                delay={index * 80}
              />
            ))}

            <div style={{ marginTop: 24 }}>
              {[
                "OOP",
                "Data Structures & Algorithms",
                "API Design",
                "Distributed Systems",
              ].map((tag) => (
                <span
                  key={tag}
                  style={{
                    display: "inline-block",
                    margin: "4px 6px 4px 0",
                    fontSize: 11,
                    padding: "4px 12px",
                    borderRadius: 20,
                    background: "rgba(124,58,237,0.12)",
                    color: "#7c3aed",
                    border: "1px solid rgba(124,58,237,0.3)",
                    fontFamily: "'Space Mono', monospace",
                  }}
                >
                  {tag}
                </span>
              ))}
            </div>
          </div>

          <div>
            <div
              style={{
                fontSize: 11,
                fontFamily: "'Space Mono', monospace",
                color: "#00d4ff",
                letterSpacing: 2,
                marginBottom: 28,
              }}
            >
              SOFT SKILLS
            </div>

            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fit, minmax(150px, 1fr))",
                gap: 12,
              }}
            >
              {SKILLS_SOFT.map((skill) => (
                <div
                  key={skill}
                  style={{
                    background: "#0d1117",
                    border: "1px solid rgba(255,255,255,0.06)",
                    borderRadius: 8,
                    padding: "16px 18px",
                    display: "flex",
                    alignItems: "center",
                    gap: 10,
                  }}
                >
                  <span
                    style={{
                      width: 6,
                      height: 6,
                      borderRadius: "50%",
                      background: "#00d4ff",
                      boxShadow: "0 0 6px #00d4ff",
                      flexShrink: 0,
                    }}
                  />
                  <span style={{ fontSize: 13, color: "#a0aec0" }}>
                    {skill}
                  </span>
                </div>
              ))}
            </div>

            <div
              style={{
                marginTop: 32,
                background: "#0d1117",
                border: "1px solid rgba(0,212,255,0.1)",
                borderRadius: 12,
                padding: 24,
              }}
            >
              <div
                style={{
                  fontSize: 11,
                  fontFamily: "'Space Mono', monospace",
                  color: "#00d4ff",
                  letterSpacing: 2,
                  marginBottom: 16,
                }}
              >
                CURRENT FOCUS
              </div>

              <p
                style={{
                  fontSize: 13,
                  color: "#718096",
                  lineHeight: 1.8,
                  margin: 0,
                }}
              >
                Building a Next.js portfolio with Tailwind CSS, Framer Motion,
                and React Three Fiber — exploring the frontend ecosystem with a
                passion for UI/UX and performance.
              </p>
            </div>
          </div>
        </div>
      </Section>

      <Section id="Projects">
        <SectionLabel>03. PROJECTS</SectionLabel>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
            gap: 20,
          }}
        >
          {PROJECTS.map((project, index) => (
            <ProjectCard
              key={project.title}
              project={project}
              index={index}
            />
          ))}
        </div>
      </Section>

      <Section id="Contact">
        <SectionLabel>04. CONTACT</SectionLabel>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
            gap: 48,
            alignItems: "start",
          }}
        >
          <div>
            <h2
              style={{
                fontFamily: "'Syne', sans-serif",
                fontSize: 36,
                fontWeight: 700,
                margin: "0 0 20px",
                lineHeight: 1.2,
              }}
            >
              Let's <span style={{ color: "#00d4ff" }}>connect</span> and build
              something great.
            </h2>

            <p
              style={{
                color: "#718096",
                lineHeight: 1.8,
                fontSize: 14,
                marginBottom: 32,
              }}
            >
              I'm currently open to internships, freelance work, and full-time
              opportunities. Feel free to reach out!
            </p>

            {[
              {
                label: "Email",
                value: "nimannethmika@gmail.com",
                icon: "✉",
                href: "mailto:nimannethmika@gmail.com",
              },
              {
                label: "Phone",
                value: "+94 77 593 4822",
                icon: "☎",
                href: "tel:+94775934822",
              },
              {
                label: "Location",
                value: "264/26 Weliwita Road, Kaduwela",
                icon: "◎",
                href: null,
              },
              {
                label: "LinkedIn",
                value: "Niman Nethmika",
                icon: "in",
                href: "#",
              },
              {
                label: "GitHub",
                value: "Niman Nethmika",
                icon: "⌥",
                href: "#",
              },
            ].map(({ label, value, icon, href }) => (
              <div
                key={label}
                style={{
                  display: "flex",
                  gap: 16,
                  alignItems: "center",
                  marginBottom: 16,
                }}
              >
                <div
                  style={{
                    width: 36,
                    height: 36,
                    borderRadius: 8,
                    background: "rgba(0,212,255,0.08)",
                    border: "1px solid rgba(0,212,255,0.15)",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    fontSize: 14,
                    color: "#00d4ff",
                    flexShrink: 0,
                  }}
                >
                  {icon}
                </div>

                <div>
                  <div
                    style={{
                      fontSize: 11,
                      color: "#4a5568",
                      fontFamily: "'Space Mono', monospace",
                      letterSpacing: 1,
                    }}
                  >
                    {label}
                  </div>

                  {href ? (
                    <a
                      href={href}
                      style={{
                        fontSize: 13,
                        color: "#a0aec0",
                        textDecoration: "none",
                      }}
                    >
                      {value}
                    </a>
                  ) : (
                    <span style={{ fontSize: 13, color: "#a0aec0" }}>
                      {value}
                    </span>
                  )}
                </div>
              </div>
            ))}
          </div>

          <div
            style={{
              background: "#0d1117",
              border: "1px solid rgba(255,255,255,0.06)",
              borderRadius: 16,
              padding: 32,
            }}
          >
            <div
              style={{
                fontSize: 11,
                fontFamily: "'Space Mono', monospace",
                color: "#00d4ff",
                letterSpacing: 2,
                marginBottom: 24,
              }}
            >
              SEND A MESSAGE
            </div>

            {["Name", "Email"].map((field) => (
              <div key={field} style={{ marginBottom: 16 }}>
                <label
                  style={{
                    display: "block",
                    fontSize: 11,
                    color: "#4a5568",
                    fontFamily: "'Space Mono', monospace",
                    letterSpacing: 1,
                    marginBottom: 8,
                  }}
                >
                  {field.toUpperCase()}
                </label>

                <input
                  type={field === "Email" ? "email" : "text"}
                  placeholder={field === "Name" ? "Your name" : "your@email.com"}
                  style={{
                    width: "100%",
                    padding: "12px 16px",
                    borderRadius: 8,
                    border: "1px solid rgba(255,255,255,0.08)",
                    background: "#080c14",
                    color: "#e2e8f0",
                    fontSize: 14,
                    outline: "none",
                    fontFamily: "'DM Sans', sans-serif",
                    boxSizing: "border-box",
                  }}
                />
              </div>
            ))}

            <div style={{ marginBottom: 20 }}>
              <label
                style={{
                  display: "block",
                  fontSize: 11,
                  color: "#4a5568",
                  fontFamily: "'Space Mono', monospace",
                  letterSpacing: 1,
                  marginBottom: 8,
                }}
              >
                MESSAGE
              </label>

              <textarea
                rows={5}
                placeholder="Tell me about your project..."
                style={{
                  width: "100%",
                  padding: "12px 16px",
                  borderRadius: 8,
                  border: "1px solid rgba(255,255,255,0.08)",
                  background: "#080c14",
                  color: "#e2e8f0",
                  fontSize: 14,
                  resize: "vertical",
                  outline: "none",
                  fontFamily: "'DM Sans', sans-serif",
                  boxSizing: "border-box",
                }}
              />
            </div>

            <button
              style={{
                width: "100%",
                padding: "14px",
                borderRadius: 8,
                border: "none",
                cursor: "pointer",
                background: "linear-gradient(135deg, #00d4ff, #7c3aed)",
                color: "#fff",
                fontFamily: "'Space Mono', monospace",
                fontSize: 13,
                letterSpacing: 2,
                boxShadow: "0 0 20px rgba(0,212,255,0.25)",
              }}
            >
              SEND_MESSAGE →
            </button>
          </div>
        </div>
      </Section>

      <section
        style={{
          maxWidth: 900,
          margin: "0 auto",
          padding: "0 24px 80px",
        }}
      >
        <div
          style={{
            borderTop: "1px solid rgba(255,255,255,0.06)",
            paddingTop: 48,
          }}
        >
          <div
            style={{
              fontSize: 11,
              fontFamily: "'Space Mono', monospace",
              color: "#7c3aed",
              letterSpacing: 2,
              marginBottom: 24,
            }}
          >
            REFERENCES
          </div>

          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
              gap: 16,
            }}
          >
            {[
              {
                name: "Mr. Prasanna Rathnayake",
                role: "CEO – Silvertec Technologies",
                phone: "+94 77 768 8665",
                email: "prathnayake@hotmail.com",
              },
              {
                name: "Mr. M.M Anura Prasanna",
                role: "Director (Real Estate Development)",
                phone: "+94 76 207 2487",
                email: "anurapmu01@gmail.com",
              },
            ].map((ref) => (
              <div
                key={ref.name}
                style={{
                  background: "#0d1117",
                  border: "1px solid rgba(255,255,255,0.06)",
                  borderRadius: 10,
                  padding: "20px 24px",
                }}
              >
                <div
                  style={{
                    fontSize: 14,
                    fontWeight: 500,
                    color: "#e2e8f0",
                    marginBottom: 4,
                  }}
                >
                  {ref.name}
                </div>

                <div
                  style={{
                    fontSize: 12,
                    color: "#7c3aed",
                    marginBottom: 10,
                  }}
                >
                  {ref.role}
                </div>

                <div style={{ fontSize: 12, color: "#4a5568" }}>
                  {ref.phone}
                </div>

                <div style={{ fontSize: 12, color: "#4a5568" }}>
                  {ref.email}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <footer
        style={{
          textAlign: "center",
          padding: "32px",
          borderTop: "1px solid rgba(255,255,255,0.04)",
          fontFamily: "'Space Mono', monospace",
          fontSize: 11,
          color: "#2d3748",
        }}
      >
        &lt;/ Designed &amp; Built by Niman Nethmika Rathnayake &gt;
      </footer>
    </div>
  );
}