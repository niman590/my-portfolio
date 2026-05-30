export const NAV_LINKS = ["Home", "About", "Skills", "Projects", "Contact"];

export const SKILLS_TECH = [
  { name: "Python", level: 88 },
  { name: "JavaScript", level: 78 },
  { name: "Java", level: 70 },
  { name: "C++", level: 72 },
  { name: "Dart", level: 70 },
  { name: "Flutter", level: 72 },
  { name: "TensorFlow / Keras", level: 68 },
  { name: "Ruby on Rails", level: 65 },
  { name: "MySQL / SQLite", level: 80 },
];

export const SKILLS_SOFT = [
  "Problem-solving",
  "Communication",
  "Teamwork",
  "Time management",
  "Adaptability",
  "Quick learning",
];

export const SKILLS_EXTRA = [
  "OOP",
  "REST APIs",
  "Networking",
  "Distributed Systems",
  "Software Testing",
  "Performance Testing",
  "Data Structures & Algorithms",
  "Image Classification",
  "CNN / ANN",
  "Model Evaluation",
];

export const TOOLS = [
  "Git", "GitHub", "Apache JMeter", "VS Code", "HTML5", "CSS3",
];

export const PROJECTS = [
  {
    title: "CIVIC PLAN — Land Management Portal",
    tags: ["Python", "SQLite", "HTML/CSS/JS", "ML"],
    color: "#00d4ff",
    icon: "🏙️",
    group: true,
    bullets: [
      "Web-based land management system with citizen registration and document submission",
      "Admin approval workflows, property search, GIS/street-view visualization",
      "ML-based land valuation model integrated into the platform",
      "Performance testing with Apache JMeter for scalability and reliability analysis",
    ],
  },
  {
    title: "Mineral Density Classification System",
    tags: ["Python", "TensorFlow", "Keras"],
    color: "#a855f7",
    icon: "🧠",
    group: false,
    bullets: [
      "CNN/ANN image classification models with high prediction accuracy",
      "Preprocessing pipelines, model tuning, and comprehensive evaluation",
    ],
  },
  {
    title: "Distributed Banking System",
    tags: ["Python", "gRPC", "SQLite"],
    color: "#00d4ff",
    icon: "🏦",
    group: false,
    bullets: [
      "3-tier architecture: Client, Application Server, Database Server",
      "RPC communication, secure authentication, and transaction validation",
      "SQLite-backed persistent data storage layer",
    ],
  },
  {
    title: "Flutter Tic Tac Toe Game",
    tags: ["Dart", "Flutter"],
    color: "#7c3aed",
    icon: "🎮",
    group: false,
    bullets: [
      "Cross-platform mobile game for Android and iOS",
      "Clean gameplay logic, responsive UI, and multiple difficulty levels",
    ],
  },
  {
    title: "Quotes Web Application",
    tags: ["Ruby on Rails", "SQL"],
    color: "#10b981",
    icon: "💬",
    group: false,
    bullets: [
      "Role-based access control and secure authentication",
      "Database-backed content management system",
    ],
  },
  {
    title: "Dictionary Search Program",
    tags: ["C++"],
    color: "#f59e0b",
    icon: "📖",
    group: false,
    bullets: [
      "Word management tool with search functionality and file handling",
      "Random word selection feature",
    ],
  },
];

export const EDUCATION = [
  {
    degree: "Bachelor of Computer Science (Software Engineering)",
    school: "Edith Cowan University, Rajagiriya",
    period: "Nov 2023 – Present",
    note: "Currently enrolled",
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
    name: "Available on request",
    role: "",
    phone: "",
    email: "",
  },
];

export const CONTACT_INFO = [
  { label: "Email", value: "nimannethmika@gmail.com", icon: "✉", href: "mailto:nimannethmika@gmail.com" },
  { label: "Phone", value: "+94 77 593 4822", icon: "☎", href: "tel:+94775934822" },
  { label: "LinkedIn", value: "Niman Nethmika", icon: "in", href: "#" },
  { label: "GitHub", value: "Niman Nethmika", icon: "⌥", href: "#" },
  { label: "Portfolio", value: "My Portfolio", icon: "◈", href: "#" },
];