"use client";

import { useEffect, useState } from "react";
import { NAV_LINKS } from "@/lib/data";
import Grid from "@/components/shared/Grid";
import Navbar from "@/components/shared/Navbar";
import Footer from "@/components/shared/Footer";
import Hero from "@/components/sections/Hero";
import About from "@/components/sections/About";
import Skills from "@/components/sections/Skills";
import Projects from "@/components/sections/Project";
import Contact from "@/components/sections/Contact";

export default function Page() {
  const [activeSection, setActiveSection] = useState("Home");
  const [cursorPos, setCursorPos] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const move = (e: MouseEvent) => setCursorPos({ x: e.clientX, y: e.clientY });
    window.addEventListener("mousemove", move);
    return () => window.removeEventListener("mousemove", move);
  }, []);

  useEffect(() => {
    const handleScroll = () => {
      const sections = NAV_LINKS.map((name) => document.getElementById(name));
      const scrollY = window.scrollY + 200;
      sections.forEach((section, index) => {
        if (section && section.offsetTop <= scrollY && section.offsetTop + section.offsetHeight > scrollY) {
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

      {/* Cursor glow */}
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
          background: "radial-gradient(circle, rgba(0,212,255,0.06) 0%, transparent 70%)",
          transition: "left 0.1s, top 0.1s",
        }}
      />

      <Grid />
      <Navbar activeSection={activeSection} scrollTo={scrollTo} />
      <Hero scrollTo={scrollTo} />
      <About />
      <Skills />
      <Projects />
      <Contact />
      <Footer />
    </div>
  );
}