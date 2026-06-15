"use client";

import Section from "@/components/ui/Section";
import SectionLabel from "@/components/ui/SectionLabel";
import { CONTACT_INFO } from "@/lib/data";

const cvUrl = "/my-portfolio/Niman_Nethmika_CV.pdf";
const formspreeUrl = "https://formspree.io/f/xwvjynre";

export default function Contact() {
  return (
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
            Let&apos;s <span style={{ color: "#00d4ff" }}>connect</span> and
            build something great.
          </h2>

          <p
            style={{
              color: "#718096",
              lineHeight: 1.8,
              fontSize: 14,
              marginBottom: 32,
            }}
          >
            I&apos;m currently seeking internship and graduate opportunities in
            Software Development and QA Engineering. Feel free to reach out!
          </p>

          {CONTACT_INFO.map(({ label, value, icon, href }) => (
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
                    target="_blank"
                    rel="noopener noreferrer"
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

          <div
            style={{
              marginTop: 32,
              display: "flex",
              gap: 12,
              flexWrap: "wrap",
            }}
          >
            <a
              href={cvUrl}
              target="_blank"
              rel="noopener noreferrer"
              style={{
                padding: "11px 24px",
                borderRadius: 6,
                border: "1px solid rgba(16,185,129,0.4)",
                background: "rgba(16,185,129,0.07)",
                color: "#10b981",
                fontFamily: "'Space Mono', monospace",
                fontSize: 11,
                letterSpacing: 2,
                textDecoration: "none",
                display: "inline-flex",
                alignItems: "center",
                gap: 8,
              }}
            >
              ↗ VIEW CV
            </a>

            <a
              href={cvUrl}
              target="_blank"
              rel="noopener noreferrer"
              style={{
                padding: "11px 24px",
                borderRadius: 6,
                border: "1px solid rgba(0,212,255,0.3)",
                background: "rgba(0,212,255,0.05)",
                color: "#00d4ff",
                fontFamily: "'Space Mono', monospace",
                fontSize: 11,
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
        </div>

        <form
          action={formspreeUrl}
          method="POST"
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

          <div style={{ marginBottom: 16 }}>
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
              NAME
            </label>

            <input
              type="text"
              name="name"
              placeholder="Your name"
              required
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

          <div style={{ marginBottom: 16 }}>
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
              EMAIL
            </label>

            <input
              type="email"
              name="email"
              placeholder="your@email.com"
              required
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
              name="message"
              rows={5}
              placeholder="Tell me about your opportunity..."
              required
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
            type="submit"
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
        </form>
      </div>
    </Section>
  );
}