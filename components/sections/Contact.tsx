import Section from "@/components/ui/Section";
import SectionLabel from "@/components/ui/SectionLabel";
import { CONTACT_INFO, REFERENCES } from "@/lib/data";

export default function Contact() {
  return (
    <>
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

            <p style={{ color: "#718096", lineHeight: 1.8, fontSize: 14, marginBottom: 32 }}>
              I'm currently open to internships, freelance work, and full-time
              opportunities. Feel free to reach out!
            </p>

            {CONTACT_INFO.map(({ label, value, icon, href }) => (
              <div
                key={label}
                style={{ display: "flex", gap: 16, alignItems: "center", marginBottom: 16 }}
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
                    <a href={href} style={{ fontSize: 13, color: "#a0aec0", textDecoration: "none" }}>
                      {value}
                    </a>
                  ) : (
                    <span style={{ fontSize: 13, color: "#a0aec0" }}>{value}</span>
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

      {/* References */}
      <section style={{ maxWidth: 900, margin: "0 auto", padding: "0 24px 80px" }}>
        <div style={{ borderTop: "1px solid rgba(255,255,255,0.06)", paddingTop: 48 }}>
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
            {REFERENCES.map((ref) => (
              <div
                key={ref.name}
                style={{
                  background: "#0d1117",
                  border: "1px solid rgba(255,255,255,0.06)",
                  borderRadius: 10,
                  padding: "20px 24px",
                }}
              >
                <div style={{ fontSize: 14, fontWeight: 500, color: "#e2e8f0", marginBottom: 4 }}>
                  {ref.name}
                </div>
                <div style={{ fontSize: 12, color: "#7c3aed", marginBottom: 10 }}>{ref.role}</div>
                <div style={{ fontSize: 12, color: "#4a5568" }}>{ref.phone}</div>
                <div style={{ fontSize: 12, color: "#4a5568" }}>{ref.email}</div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}