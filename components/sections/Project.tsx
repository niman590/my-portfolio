import Section from "@/components/ui/Section";
import SectionLabel from "@/components/ui/SectionLabel";
import ProjectCard from "@/components/ui/ProjectCard";
import { PROJECTS } from "@/lib/data";

export default function Projects() {
  return (
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
          <ProjectCard key={project.title} project={project} index={index} />
        ))}
      </div>
    </Section>
  );
}