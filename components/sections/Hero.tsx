"use client";

import GlitchText from "@/components/ui/GlitchText";

interface HeroProps {
  scrollTo: (id: string) => void;
}

export default function Hero({ scrollTo }: HeroProps) {
  return (
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
          background: "radial-gradient(circle, rgba(0,212,255,0.07) 0%, transparent 70%)",
          pointerEvents: "none",
        }}
      />

      <div style={{ position: "relative", zIndex: 1, animation: "fadeUp 1s ease both" }}>
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
          &lt; CS UNDERGRADUATE · SOFTWARE ENGINEER /&gt;
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
          <span style={{ animation: "blink 1s infinite" }}>▮</span> Web Development · Machine Learning · Distributed Systems
        </div>

        <p
          style={{
            maxWidth: 560,
            margin: "0 auto 48px",
            fontSize: 15,
            color: "#718096",
            lineHeight: 1.8,
            fontWeight: 300,
          }}
        >
          Motivated CS undergraduate seeking internship or graduate opportunities
          in Software Development and QA Engineering. Passionate about building
          scalable, secure, and user-friendly applications.
        </p>

        <div style={{ display: "flex", gap: 16, justifyContent: "center", flexWrap: "wrap" }}>
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
            }}
          >
            CONTACT ME
          </button>

          <a
            href="/Niman_Nethmika_CV.pdf"
            target="_blank"
            rel="noopener noreferrer"
            download="Niman_Nethmika_CV.pdf"
            style={{
              padding: "12px 32px",
              borderRadius: 6,
              border: "1px solid rgba(16,185,129,0.4)",
              cursor: "pointer",
              background: "rgba(16,185,129,0.07)",
              color: "#10b981",
              fontFamily: "'Space Mono', monospace",
              fontSize: 12,
              letterSpacing: 2,
              textDecoration: "none",
              display: "inline-flex",
              alignItems: "center",
              gap: 8,
            }}
          >
            ↓ DOWNLOAD CV
          </a>
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
  );
}