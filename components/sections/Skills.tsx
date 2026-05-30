import Section from "@/components/ui/Section";
import SectionLabel from "@/components/ui/SectionLabel";
import SkillBar from "@/components/ui/SkillBar";
import { SKILLS_TECH, SKILLS_SOFT, SKILLS_EXTRA, TOOLS } from "@/lib/data";

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
        {/* Left — Technical skill bars */}
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

          {/* Tools */}
          <div
            style={{
              fontSize: 11,
              fontFamily: "'Space Mono', monospace",
              color: "#00d4ff",
              letterSpacing: 2,
              marginBottom: 14,
              marginTop: 28,
            }}
          >
            TOOLS & PLATFORMS
          </div>
          <div>
            {TOOLS.map((tool) => (
              <span
                key={tool}
                style={{
                  display: "inline-block",
                  margin: "4px 6px 4px 0",
                  fontSize: 11,
                  padding: "4px 12px",
                  borderRadius: 20,
                  background: "rgba(0,212,255,0.08)",
                  color: "#00d4ff",
                  border: "1px solid rgba(0,212,255,0.2)",
                  fontFamily: "'Space Mono', monospace",
                }}
              >
                {tool}
              </span>
            ))}
          </div>
        </div>

        {/* Right — Soft skills + concepts */}
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
              marginBottom: 32,
            }}
          >
            {SKILLS_SOFT.map((skill) => (
              <div
                key={skill}
                style={{
                  background: "#0d1117",
                  border: "1px solid rgba(255,255,255,0.06)",
                  borderRadius: 8,
                  padding: "14px 18px",
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

          {/* SE Concepts */}
          <div
            style={{
              fontSize: 11,
              fontFamily: "'Space Mono', monospace",
              color: "#7c3aed",
              letterSpacing: 2,
              marginBottom: 14,
            }}
          >
            SE CONCEPTS & ML
          </div>
          <div>
            {SKILLS_EXTRA.map((tag) => (
              <span
                key={tag}
                style={{
                  display: "inline-block",
                  margin: "4px 6px 4px 0",
                  fontSize: 11,
                  padding: "4px 12px",
                  borderRadius: 20,
                  background: "rgba(124,58,237,0.1)",
                  color: "#7c3aed",
                  border: "1px solid rgba(124,58,237,0.25)",
                  fontFamily: "'Space Mono', monospace",
                }}
              >
                {tag}
              </span>
            ))}
          </div>
        </div>
      </div>
    </Section>
  );
}