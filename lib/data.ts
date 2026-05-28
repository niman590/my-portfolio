export const NAV_LINKS = ["Home", "About", "Skills", "Projects", "Contact"];

export const SKILLS_TECH = [
  { name: "Python", level: 85 },
  { name: "C++", level: 75 },
  { name: "Dart", level: 70 },
  { name: "Ruby", level: 65 },
  { name: "Flutter", level: 72 },
  { name: "Ruby on Rails", level: 65 },
  { name: "gRPC", level: 68 },
  { name: "SQLite / SQL", level: 80 },
];

export const SKILLS_SOFT = [
  "Problem-solving",
  "Communication",
  "Teamwork",
  "Time management",
  "Adaptability",
  "Quick learning",
];

export const PROJECTS = [
  {
    title: "Distributed Banking System",
    tags: ["Python", "gRPC", "SQLite"],
    color: "#00d4ff",
    icon: "🏦",
    bullets: [
      "3-tier architecture: Client, Application Server, Database Server",
      "Remote procedure calls (RPC) for inter-service communication",
      "Secure user authentication with token-based session management",
      "Transaction processing with validation and fee computation",
      "SQLite-backed persistent data storage layer",
    ],
  },
  {
    title: "Flutter Tic Tac Toe Game",
    tags: ["Dart", "Flutter"],
    color: "#7c3aed",
    icon: "🎮",
    bullets: [
      "Cross-platform mobile game for Android and iOS",
      "Full game logic, UI design, and multiple difficulty levels",
    ],
  },
  {
    title: "Quotes Web Application",
    tags: ["Ruby on Rails", "SQL"],
    color: "#10b981",
    icon: "💬",
    bullets: [
      "Role-based access control and secure authentication",
      "SQL database for quote storage and management",
    ],
  },
  {
    title: "C++ Dictionary Search",
    tags: ["C++"],
    color: "#f59e0b",
    icon: "📖",
    bullets: [
      "Word management system with types and definitions",
      "Search functionality, file handling, and random word selection",
    ],
  },
];

export const EDUCATION = [
  {
    degree: "Bachelor of Computer Science (Software Engineering)",
    school: "Edith Cowan University, Rajagiriya",
    period: "Nov 2023 – Present",
    note: "Final semester of 3rd year",
  },
  {
    degree: "Foundation Certificate in Information Technology",
    school: "Edith Cowan University, Rajagiriya",
    period: "July 2022 – Nov 2023",
  },
  {
    degree: "GCE Ordinary Level",
    school: "Isipathana College, Colombo 05",
    period: "2021 (2022)",
  },
];

export const REFERENCES = [
  {
    name: "Mr. Prasanna Rathnayake",
    role: "CEO – Silvertec Technologies",
    phone: "+94 77 768 8665",
    email: "prathnayake@hotmail.com",
  },
  {
    name: "Mr. M.M Anura Prasanna",
    role: "Director (Real Estate Development)",
    phone: "+94 76 207 2487",
    email: "anurapmu01@gmail.com",
  },
];

export const CONTACT_INFO = [
  { label: "Email", value: "nimannethmika@gmail.com", icon: "✉", href: "mailto:nimannethmika@gmail.com" },
  { label: "Phone", value: "+94 77 593 4822", icon: "☎", href: "tel:+94775934822" },
  { label: "Location", value: "264/26 Weliwita Road, Kaduwela", icon: "◎", href: null },
  { label: "LinkedIn", value: "Niman Nethmika", icon: "in", href: "#" },
  { label: "GitHub", value: "Niman Nethmika", icon: "⌥", href: "#" },
];