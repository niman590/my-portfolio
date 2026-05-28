export default function SectionLabel({ children }: { children: React.ReactNode }) {
  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        gap: 16,
        marginBottom: 48,
      }}
    >
      <span
        style={{
          fontFamily: "'Space Mono', monospace",
          fontSize: 12,
          color: "#00d4ff",
          letterSpacing: 3,
        }}
      >
        {children}
      </span>
      <div
        style={{
          flex: 1,
          height: 1,
          background: "linear-gradient(90deg, rgba(0,212,255,0.4), transparent)",
        }}
      />
    </div>
  );
}