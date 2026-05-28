import Section from "@/components/ui/Section";
import SectionLabel from "@/components/ui/SectionLabel";
import { EDUCATION } from "@/lib/data";

export default function About() {
  return (
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

          <p style={{ color: "#718096", lineHeight: 1.9, fontSize: 14, marginBottom: 20 }}>
            I'm a motivated and detail-oriented Computer Science undergraduate
            specializing in Software Engineering at Edith Cowan University,
            currently in the final semester of my 3rd year.
          </p>

          <p style={{ color: "#718096", lineHeight: 1.9, fontSize: 14 }}>
            I possess strong foundational knowledge in software development,
            distributed systems, and full-stack development — demonstrated
            through multiple academic and personal projects.
          </p>

          <div style={{ display: "flex", gap: 16, marginTop: 32, flexWrap: "wrap" }}>
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
              <div style={{ fontSize: 13, fontWeight: 500, color: "#e2e8f0", marginBottom: 4, lineHeight: 1.4 }}>
                {item.degree}
              </div>
              <div style={{ fontSize: 12, color: "#4a5568", marginBottom: 2 }}>{item.school}</div>
              <div style={{ fontFamily: "'Space Mono', monospace", fontSize: 11, color: "#7c3aed" }}>
                {item.period}
              </div>
              {"note" in item && item.note && (
                <div style={{ fontSize: 11, color: "#00d4ff", marginTop: 4, fontStyle: "italic" }}>
                  {item.note}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </Section>
  );
}