import type { CSSProperties } from "react";

interface GlitchTextProps {
  text: string;
  style?: CSSProperties;
}

export default function GlitchText({ text, style }: GlitchTextProps) {
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
          0%,100%{opacity:1} 50%{opacity:0}
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