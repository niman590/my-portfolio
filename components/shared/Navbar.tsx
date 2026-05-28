"use client";

import { NAV_LINKS } from "@/lib/data";

interface NavbarProps {
  activeSection: string;
  scrollTo: (id: string) => void;
}

export default function Navbar({ activeSection, scrollTo }: NavbarProps) {
  return (
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
  );
}