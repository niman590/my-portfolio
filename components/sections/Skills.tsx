import Section from "@/components/ui/Section";
import SectionLabel from "@/components/ui/SectionLabel";
import SkillBar from "@/components/ui/SkillBar";
import { SKILLS_TECH, SKILLS_SOFT } from "@/lib/data";

export default function Skills() {
  return (
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
            <SkillBar key={skill.name} name={skill.name} level={skill.level} delay={index * 80} />
          ))}

          <div style={{ marginTop: 24 }}>
            {["OOP", "Data Structures & Algorithms", "API Design", "Distributed Systems"].map((tag) => (
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
                <span style={{ fontSize: 13, color: "#a0aec0" }}>{skill}</span>
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
            <p style={{ fontSize: 13, color: "#718096", lineHeight: 1.8, margin: 0 }}>
              Building a Next.js portfolio with Tailwind CSS, Framer Motion,
              and React Three Fiber — exploring the frontend ecosystem with a
              passion for UI/UX and performance.
            </p>
          </div>
        </div>
      </div>
    </Section>
  );
}