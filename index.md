---
layout: default
title: Home
---

<!-- Simple nav -->
<nav style="margin-bottom: 20px;">
  <a href="./index.html">Home</a> |
  <a href="./enhancement-one.md">Enhancement 1</a> |
  <a href="./enhancement-two.md">Enhancement 2</a> |
  <a href="./enhancement-three.md">Enhancement 3</a> |
   <a href="https://corner-grocer-alyshaspradlin.replit.app">Enhancement Demo</a> |
  </nav>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cascadia+Code:ital,wght@0,200..700;1,200..700&family=Cascadia+Mono:ital,wght@0,200..700;1,200..700&family=DotGothic16&family=Fira+Code:wght@300..700&family=Handjet:wght@100..900&family=Jersey+15&family=Jersey+20&family=Jersey+25&family=Pixelify+Sans:wght@400..700&family=Press+Start+2P&family=Share+Tech&family=Share+Tech+Mono&family=Silkscreen:wght@400;700&family=VT323&display=swap" rel="stylesheet">

<style> 
  .press-scope h1{
    font-family: "Press Start 2P", system-ui, monospace;
    text-align: center;
    font-weight: 400;        /* Press Start 2P only ships as 400 */
    letter-spacing: .5px;
    line-height: 1.25;
  }
  
</style>

 
<!-- Typed header -->
<center> <h1 id="typed-header">Welcome to my ePortfolio</h1></center>

# About Me
Hello! My name is Alysha Pursley, and I am currently finishing up a degree in Computer Science, with a focus on Software Development, at Southern New Hampshire University. I have a strong passion for creating engaging, user-friendly interfaces and developing websites and applications that are both functional and visually appealing. My goal is to become a skilled front-end or full-stack developer, where I can bring ideas to life through innovative design and efficient coding. Throughout my studies, I’ve gained valuable experience in various programming languages and development tools, which I am eager to apply in real-world projects. This portfolio reflects my dedication, growth, and the skills I’ve cultivated so far, and I look forward to contributing to exciting tech solutions in the future.



## What I’ve Learned

### Collaboration 

I learned to structure code so other people can step in quickly: clear names, small focused functions, and comments that explain why a choice was made, not just what it does. Group work and code reviews taught me to keep logic modular and leave helpful breadcrumbs for the next person. Those habits map directly to Outcome 1 on collaboration and supported by the planning I captured for my capstone. 
 

### Communication
I got comfortable switching between technical detail and plain English—README instructions, user-facing prompts, and short demos that focus on outcomes first. My e-commerce work reinforced this: translating platform, hosting, and security work into clear updates for customers or vendors, and documenting steps so non-engineers can follow along. 
 

### Data Structures and Algorithms Across courses, I practiced choosing simple, predictable structures—lists, maps/dicts, queues—then measuring when sorting or searching variants actually help. I also learned to weigh clarity vs. performance and to use language-idiomatic tools (e.g., Python’s defaultdict, safe lookups) to keep behavior predictable. 
 

Software engineering and databases. I’ve become much more intentional about separation of concerns, reusability, and writing code that’s easy to extend. On the data side, I learned schema basics and safe query habits, plus when to move from files to a real database for persistence and reliability. 
 
 

Security mindset. I now assume inputs can be wrong or hostile. I validate, handle errors, parameterize queries, and keep an eye on least privilege. Coursework and my security-oriented training/certifications made this a baseline expectation in everything I build. 

## Software Design and Engineering

Rewriting the application in Python pushed me to separate concerns cleanly and think in modules instead of one long script. I organized responsibilities into focused functions and files and kept I/O, core logic, and data access from bleeding into each other. This structure makes the program easier to reason about, simpler to test, and far less fragile when new features show up later. I also added consistent inline comments and top-level block comments to explain purpose, assumptions, and edge cases. The result is a codebase that reads like a guide to itself instead of a collection of guesses.

## Algorithms and Data Structures

The sorting and searching enhancement forced me to choose the right structures and to think about runtime costs in a practical way. I used dictionaries (maps) for frequency counts, lists for ordered output, and clear comparisons to support alphabetical and frequency-based sorting. I focused on stable, readable operations that still perform well for typical data sizes, avoiding “clever” code that hides time complexity. The search flow guides the user with predictable behavior and clear messages, which matters as much as the underlying algorithm. This balance of correctness, clarity, and user experience reflects how I now approach problem solving.

## Databases

Moving from in-memory data to SQLite created a proper boundary for persistence and opened the door for reliability improvements. I designed a simple schema, wrote parameterized queries to protect against injection, and added basic error handling to keep operations safe. The small data layer (db_handler style organization) keeps SQL concerns in one place, which reduces duplication and mistakes. I validated assumptions around file paths, empty databases, and initial seed data to keep the app predictable on first launch. The application now remembers state across runs and behaves like software a user could trust day-to-day.

<!-- Skills Showcase (paste into your Markdown page) -->
<section class="skills-showcase" aria-labelledby="skills-title">
  <h2 id="skills-title">Skills Demonstrated</h2>

  <style>
    /* Scoped styles for the Hacker theme */
    .skills-showcase { --accent:#39ff14; --card-bg: transparent; --chip-bg: rgba(57,255,20,0.08); }
    .skills-showcase { margin: 1.5rem 0 2rem; }
    .skills-showcase h2 { margin-bottom: 1rem; }
    .skills-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
    }
    .skill-card {
      border: 1px solid var(--accent);
      border-left-width: 6px;
      border-radius: 12px;
      padding: 1rem;
      background: var(--card-bg);
    }
    .skill-card h3 {
      margin: 0 0 .5rem;
      line-height: 1.2;
      font-size: 1.05rem;
      display: flex; align-items: center; gap: .5rem;
    }
    .skill-card h3 .icon { font-size: 1.2rem; }
    .skill-card p.sub {
      margin: 0 0 .75rem; font-size: .9rem; opacity: .85;
    }
    .chips { display: flex; flex-wrap: wrap; gap: .5rem; }
    .chip {
      display: inline-block;
      border: 1px solid var(--accent);
      background: var(--chip-bg);
      padding: .25rem .6rem;
      border-radius: 999px;
      font-size: .9rem;
      white-space: nowrap;
    }
    /* Optional: collapsible details look */
    .skill-card details { margin-top: .25rem; }
    .skill-card summary {
      cursor: pointer; user-select: none; outline: none;
      font-size: .9rem; opacity: .9; margin-bottom: .5rem;
    }
    .skill-card summary::-webkit-details-marker { display: none; }
    .skill-card summary:before { content: "▸ "; }
    .skill-card details[open] summary:before { content: "▾ "; }
    /* Tweak for narrow screens */
    @media (max-width: 420px){
      .chips { gap: .4rem; }
      .chip { font-size: .85rem; }
    }
  </style>

  <div class="skills-grid">
    <article class="skill-card">
      <h3>Programming Proficiency</h3>
      <p class="sub">Core languages and habits that make code easier to write, read, and change.</p>
      <details open>
        <summary>Show skills</summary>
      <div class="chips">
        <span class="chip">Language Portability: C++ → Python</span>
        <span class="chip">Programming Proficiency</span>
        <span class="chip">Python</span>
        <span class="chip">C++</span>
        <span class="chip">Problem-Solving</span>
        <span class="chip">Function Abstraction</span>
      </div>
      </details>
    </article>
    <article class="skill-card">
      <h3>Software Design & Architecture</h3>
      <p class="sub">Structure that keeps features maintainable and team-friendly.</p>
      <details open>
        <summary>Show skills</summary>
      <div class="chips">
        <span class="chip">Software Design Principles</span>
        <span class="chip">Modular Architecture & Design</span>
        <span class="chip">Separation of Concerns</span>
        <span class="chip">Code Reusability</span>
        <span class="chip">Basic Class Design</span>
        <span class="chip">Persistent Storage Design</span>
        <span class="chip">Basic Database Schema Design</span>
        <span class="chip">Expanded System Scalability</span>
        <span class="chip">Preserved Backward Compatibility</span>
      </div>
      </details>
    </article>
    <article class="skill-card">
      <h3>Data Handling & Structures</h3>
      <p class="sub">Moving, storing, and guarding data responsibly.</p>
      <details open>
        <summary>Show skills</summary>
      <div class="chips">
        <span class="chip">File I/O Handling</span>
        <span class="chip">Database Integration</span>
        <span class="chip">SQL Query Construction</span>
        <span class="chip">Safe Data Access Patterns</span>
        <span class="chip">Safe Dictionary Access</span>
        <span class="chip">Use of <code>defaultdict</code></span>
        <span class="chip">String Normalization</span>
        <span class="chip">Input Validation Implementation</span>
        <span class="chip">Input Handling Enhancements</span>
        <span class="chip">Error Handling in Data Operations</span>
      </div>
      </details>
    </article>
    <article class="skill-card">
      <h3>Data Processing & Output</h3>
      <p class="sub">Turning raw values into results people can use.</p>
      <details open>
        <summary>Show skills</summary>
      <div class="chips">
        <span class="chip">Data Sorting</span>
        <span class="chip">Alphabetical Sorting Logic</span>
        <span class="chip">Frequency-Based Sorting</span>
        <span class="chip">Data Retrieval and Display</span>
        <span class="chip">Histogram Output</span>
        <span class="chip">Search Functionality</span>
      </div>
      </details>
    </article>
    <article class="skill-card">
      <h3>Interface Design & Usability</h3>
      <p class="sub">Flows that are predictable and easy to navigate.</p>
      <details open>
        <summary>Show skills</summary>
      <div class="chips">
        <span class="chip">Menu Design</span>
        <span class="chip">Menu-Driven Interface</span>
        <span class="chip">Menu-Driven Interface Expansion</span>
        <span class="chip">Expanded Menu System</span>
        <span class="chip">User Experience Improvements</span>
      </div>
      </details>
    </article>
   <article class="skill-card">
      <h3>Documentation & Readability</h3>
      <p class="sub">Code that explains itself and is easy to hand off.</p>
      <details open>
        <summary>Show skills</summary>
     <div class="chips">
        <span class="chip">Code Documentation</span>
        <span class="chip">Commenting and Readability</span>
      </div>
      </details>
    </article>
  </div>


<!-- ===============================
  SECTION: Other Coursework Projects (Hacker Theme)
  HOW TO USE:
  1) Paste this whole block into your page (e.g., index.md via raw HTML, or default.html inside <main>).
  2) If your site has a global JS, you can move the <script> content there. Otherwise leave it inline.
  3) No external libs; works with Jekyll’s Hacker theme styles.
================================== -->

<section id="coursework-terminal" aria-labelledby="ocp-title">
  <h2 id="ocp-title">🧪 Other Coursework Projects</h2>
  <p class="ocp-subtle">These come from classes outside my capstone artifact and shaped my overall skillset.</p>

  <!-- Terminal-like command bar -->
  <div class="ocp-shell" role="region" aria-label="Coursework terminal">
    <div class="ocp-line">
      <span class="ocp-prompt">$</span>
      <span class="ocp-cmd">projects --list</span>
      <span class="ocp-result"># type to filter ↓ or click tags</span>
    </div>

    <div class="ocp-line ocp-input-wrap">
      <label for="ocp-search" class="ocp-prompt">$</label>
      <input id="ocp-search" class="ocp-input" type="search" placeholder="filter: security, api, c++, android, testing, mongodb, concurrency, graphics..." aria-label="Filter projects by keyword or skill">
      <button id="ocp-reset" class="ocp-btn" type="button" title="Clear filter">reset</button>
    </div>

    <div id="ocp-tags" class="ocp-tags" aria-live="polite"></div>

    <!-- Rendered projects -->
    <div id="ocp-feed" class="ocp-feed" aria-live="polite"></div>
  </div>

  <!-- No-JS fallback (always visible; JS hides it on init) -->
  <details class="ocp-fallback" open>
    <summary>Fallback list (static)</summary>
    <ul>
      <li><strong>CS-250 — Software Development Lifecycle</strong>: SDLC plan w/ risk analysis, use cases, maintenance strategy (Agile, UML)</li>
      <li><strong>CS-305 — Software Security</strong>: Banking-app threat modeling + countermeasures (CIA triad, OWASP mitigations)</li>
      <li><strong>CS-360 — Mobile Architecture & Programming</strong>: Android grocery list app (Java, SQLite, intents, JSON)</li>
      <li><strong>CS-340 — Client/Server Development</strong>: REST API + MongoDB (Node/Express, CRUD, Postman)</li>
      <li><strong>CS-320 — Software Testing</strong>: Test plan + unit tests (Python unittest, coverage, black/white box)</li>
      <li><strong>CS-260 — Data Structures & Algorithms</strong>: Merge/Quick/Bubble; DFS/BFS; basic hash table (C++, complexity, recursion)</li>
      <li><strong>CS-315 — Operating Systems</strong>: Process scheduling sim + multithreaded app (threading, concurrency, system calls)</li>
      <li><strong>CS-330 — Computer Graphics & Visualization</strong>: OpenGL 2D interface (render pipeline, transforms, coordinate spaces)</li>
    </ul>
  </details>
</section>

<style>
/* ===============================
   Minimal CSS tuned for Jekyll "Hacker" theme
   (dark bg, green accents, monospace). Keeps things lightweight and theme-friendly.
================================== */
#coursework-terminal {
  margin: 2rem 0;
}
#coursework-terminal .ocp-subtle {
  opacity: .9;
  margin-top: -0.25rem;
}
.ocp-shell {
  background: #0b0b0b;
  border: 1px solid #1a1a1a;
  border-radius: 8px;
  padding: 0.75rem;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  color: #c8facc; /* soft green */
}
.ocp-line {
  display: flex;
  align-items: center;
  gap: .5rem;
  padding: .25rem 0;
  white-space: nowrap;
  overflow: hidden;
}
.ocp-prompt {
  color: #00ff66; /* hacker green prompt */
  user-select: none;
}
.ocp-cmd {
  color: #7dfb9a;
}
.ocp-result {
  color: #84c09c;
  opacity: .9;
}
.ocp-input-wrap {
  gap: .65rem;
  flex-wrap: wrap;
}
.ocp-input {
  flex: 1 1 340px;
  min-width: 260px;
  background: #0f0f0f;
  color: #e6ffe9;
  border: 1px solid #1f1f1f;
  border-radius: 6px;
  padding: .45rem .6rem;
}
.ocp-input:focus {
  outline: 2px solid #00ff66;
  outline-offset: 2px;
}
.ocp-btn {
  background: transparent;
  color: #a8ffbf;
  border: 1px solid #2a2a2a;
  padding: .4rem .7rem;
  border-radius: 6px;
  cursor: pointer;
}
.ocp-btn:hover {
  background: #0f0f0f;
}

.ocp-tags {
  margin: .5rem 0 .25rem;
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
}
.ocp-tag {
  border: 1px solid #244;
  color: #afffca;
  background: #061a12;
  padding: .2rem .55rem;
  border-radius: 999px;
  font-size: .85rem;
  cursor: pointer;
}
.ocp-tag.is-active {
  border-color: #00ff66;
  box-shadow: 0 0 0 2px rgba(0,255,102,.1);
}

.ocp-feed {
  display: grid;
  gap: .75rem;
  margin-top: .5rem;
}
.ocp-entry {
  border: 1px solid #1b1b1b;
  border-radius: 8px;
  background: #0e0e0e;
}
.ocp-head {
  display:flex;
  align-items:center;
  justify-content: space-between;
  gap: .75rem;
  padding: .6rem .75rem;
  border-bottom: 1px solid #161616;
}
.ocp-title {
  color:#b8ffcc;
  font-weight:700;
}
.ocp-code {
  color:#77ff9a;
  opacity:.9;
  font-weight:600;
}
.ocp-body {
  padding: .65rem .8rem .75rem;
}
.ocp-project {
  margin: 0 0 .4rem 0;
  color: #d9ffe3;
}
.ocp-skills {
  display: flex;
  flex-wrap: wrap;
  gap: .35rem;
  margin: .35rem 0 0 0;
  padding: 0;
  list-style: none;
}
.ocp-skill {
  border: 1px dashed #1d3b2a;
  color: #a9ffbf;
  background: #0b1511;
  padding: .15rem .45rem;
  border-radius: 6px;
  font-size: .85rem;
}
.ocp-tags-line {
  display:flex;
  flex-wrap:wrap;
  gap:.35rem;
  margin-top:.45rem;
}
.ocp-tagline {
  border: 1px solid #1c2;
  color: #afffca;
  background: #07180f;
  padding: .15rem .45rem;
  border-radius: 999px;
  font-size: .8rem;
  cursor: pointer;
}
.ocp-fallback {
  margin-top: 1rem;
  border: 1px dashed #1a1a1a;
  padding: .5rem .75rem;
  border-radius: 8px;
  background: #0b0b0b;
  color: #c8facc;
}
</style>

<script>
/* ===============================
   Data model: Your project entries + tags
   (Use your exact wording from the prompt)
================================== */
const OCP_ENTRIES = [
  {
    code: "CS-250",
    title: "Software Development Lifecycle",
    project: "Developed a software development plan with risk analysis, use cases, and maintenance strategy for a hypothetical car rental system.",
    skills: ["SDLC Phases","Agile Process","Change Management","Maintenance Planning","UML"],
    tags: ["process","uml","planning","agile"]
  },
  {
    code: "CS-305",
    title: "Software Security",
    project: "Security risk analysis for an online banking application, including threat modeling and countermeasures.",
    skills: ["Vulnerability Identification","CIA Triad","OWASP Mitigations","Threat Modeling","Input Validation"],
    tags: ["security","owasp","cia","risk"]
  },
  {
    code: "CS-360",
    title: "Mobile Architecture & Programming",
    project: "Created a mobile app prototype using Java and Android Studio to track grocery lists with SQLite integration.",
    skills: ["Mobile Lifecycle","UI Design","Local Storage","Intent Handling","JSON Parsing","SQLite (Mobile)"],
    tags: ["mobile","android","sqlite","java","ui"]
  },
  {
    code: "CS-340",
    title: "Client/Server Development",
    project: "Designed a RESTful API and connected it to a MongoDB backend using Node.js and Express, with a functional CRUD frontend.",
    skills: ["API Routing","HTTP Methods","Middleware","Postman Testing","CRUD Operations","JSON"],
    tags: ["api","backend","mongodb","node","express","crud"]
  },
  {
    code: "CS-320",
    title: "Software Testing",
    project: "Built a test plan for a file handling program and implemented unit tests using Python’s unittest.",
    skills: ["Test Coverage","Test Case Design","Black/White Box","Test Automation","Python unittest"],
    tags: ["testing","qa","python"]
  },
  {
    code: "CS-260",
    title: "Data Structures & Algorithms",
    project: "Implemented sorting algorithms (Merge, Quick, Bubble), graph traversal (DFS, BFS), and a basic hash table in C++.",
    skills: ["Time Complexity Analysis","Memory Management","Recursion","Abstract Data Types","Graphs"],
    tags: ["algorithms","c++","ds","sorting","graphs","hash"]
  },
  {
    code: "CS-315",
    title: "Operating Systems",
    project: "Simulated process scheduling using C++, created a multi-threaded application.",
    skills: ["Threading","Concurrency","Scheduling Algorithms","System Calls","Memory Hierarchy"],
    tags: ["systems","concurrency","threads","c++"]
  },
  {
    code: "CS-330",
    title: "Computer Graphics & Visualization",
    project: "Used OpenGL to create a simple 2D game interface with interactive elements.",
    skills: ["Rendering Pipeline","Geometric Transformations","Coordinate Space Math","Buffers"],
    tags: ["graphics","opengl","rendering","transforms"]
  }
];

/* Build tag set from entries */
function computeAllTags() {
  const s = new Set();
  OCP_ENTRIES.forEach(e => {
    e.tags.forEach(t => s.add(t));
  });
  return Array.from(s).sort();
}

/* Render tag chips */
let ACTIVE = new Set();
function renderTagBar() {
  const el = document.getElementById('ocp-tags');
  const tags = computeAllTags();
  el.innerHTML = tags.map(t => `
    <button class="ocp-tag ${ACTIVE.has(t) ? 'is-active':''}" data-tag="${t}" type="button" aria-pressed="${ACTIVE.has(t)}">${t}</button>
  `).join('');
  el.querySelectorAll('.ocp-tag').forEach(btn => {
    btn.addEventListener('click', () => {
      const tag = btn.dataset.tag;
      if (ACTIVE.has(tag)) { ACTIVE.delete(tag); }
      else { ACTIVE.add(tag); }
      renderTagBar();
      renderFeed();
    });
  });
}

/* Template for one entry */
function entryHTML(e){
  return `
  <article class="ocp-entry" tabindex="0" aria-label="${e.code} ${e.title}">
    <header class="ocp-head">
      <div class="ocp-title">
        <span class="ocp-code">${e.code}</span> — ${e.title}
      </div>
    </header>
    <div class="ocp-body">
      <p class="ocp-project"><strong>Project:</strong> ${e.project}</p>
      <div>
        <strong>Skills:</strong>
        <ul class="ocp-skills">
          ${e.skills.map(s => `<li class="ocp-skill">${s}</li>`).join('')}
        </ul>
      </div>
      <div class="ocp-tags-line">
        ${e.tags.map(t => `<span class="ocp-tagline" data-t="${t}" title="Filter by ${t}">${t}</span>`).join('')}
      </div>
    </div>
  </article>`;
}

/* Render entries with filter/search */
function renderFeed(){
  const feed = document.getElementById('ocp-feed');
  const q = (document.getElementById('ocp-search').value || '').toLowerCase().trim();

  const filtered = OCP_ENTRIES.filter(e => {
    const matchesTags = ACTIVE.size === 0 || [...ACTIVE].some(t => e.tags.includes(t));
    const hay = (e.code + ' ' + e.title + ' ' + e.project + ' ' + e.skills.join(' ')).toLowerCase();
    const matchesQuery = !q || hay.includes(q);
    return matchesTags && matchesQuery;
  });

  feed.innerHTML = filtered.map(entryHTML).join('') || `<div role="status">no projects match your filter.</div>`;

  // Clickable taglines inside cards to filter
  feed.querySelectorAll('.ocp-tagline').forEach(span => {
    span.addEventListener('click', () => {
      const t = span.dataset.t;
      if (ACTIVE.has(t)) ACTIVE.delete(t); else ACTIVE.add(t);
      renderTagBar();
      renderFeed();
    });
  });
}

/* Init */
document.addEventListener('DOMContentLoaded', () => {
  const fb = document.querySelector('.ocp-fallback');
  if (fb) fb.hidden = true; // hide static fallback if JS is available

  renderTagBar();
  renderFeed();

  const input = document.getElementById('ocp-search');
  const reset = document.getElementById('ocp-reset');
  input.addEventListener('input', renderFeed);
  reset.addEventListener('click', () => {
    input.value = '';
    ACTIVE = new Set();
    renderTagBar();
    renderFeed();
  });
});
</script>




<script>
document.addEventListener("DOMContentLoaded", function () {
  const el = document.getElementById("typed-header");
  const text = el.textContent.trim();
  el.textContent = "";
  let i = 0;

  function type() {
    el.textContent = text.slice(0, i++);
    if (i <= text.length) {
      setTimeout(type, 50); // speed (ms per char)
    }
  }

  type();
});
</script>
