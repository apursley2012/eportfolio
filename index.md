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

<!-- =========================================================
=  TECH & LANGUAGES  +  OTHER COURSEWORK PROJECTS (UNIFIED) =
=  Matches your existing card/chip green (#39ff14)          =
========================================================= -->

<section id="portfolio-extras">
  <!-- =========================
       TECH & LANGUAGES MATRIX
  ========================== -->
  <section class="tech-matrix" aria-labelledby="tech-title">
    <h2 id="tech-title">Tech &amp; Languages</h2>
    <style>
      /* --- scoped to .tech-matrix --- */
      .tech-matrix {
        /* match your existing card theme */
        --accent: #39ff14;
        --card-bg: transparent;
        --chip-bg: rgba(57,255,20,0.08);
        margin: 1.5rem 0 2rem;
      }
      .tech-matrix h2 { margin-bottom: 1rem; }
      /* hide default summary arrow so it doesn't overlap chips */
      .tech-matrix summary::-webkit-details-marker { display:none; }
      .tech-matrix summary { list-style:none; }
      .tm-group { margin: 1rem 0; }
      .tm-card {
        border: 1px solid var(--accent);
        border-left-width: 6px;
        border-radius: 12px;
        padding: 1rem;
        background: var(--card-bg);
      }
      .tm-card summary {
        cursor: pointer; user-select: none; outline: none;
        font-weight: 700; margin-bottom: .5rem;
        color: var(--accent);
      }
      .tm-card summary::before { content: "▸ "; }
      .tm-card[open] summary::before { content: "▾ "; }
      .tm-chips { display:flex; flex-wrap:wrap; gap:.5rem; }
      .tm-chip {
        display:inline-block; white-space:nowrap;
        border:1px solid var(--accent);
        background:var(--chip-bg);
        color: var(--accent);
        padding:.25rem .6rem; border-radius:999px; font-size:.9rem;
      }
      @media (max-width:420px){
        .tm-chips { gap:.4rem; }
        .tm-chip { font-size:.85rem; }
      }
    </style>
    <!-- 🧠 Languages -->
    <details class="tm-group tm-card" open>
      <summary>🧠 Languages</summary>
      <div class="tm-chips">
        <span class="tm-chip">Python</span>
        <span class="tm-chip">Java</span>
        <span class="tm-chip">C++</span>
        <span class="tm-chip">JavaScript</span>
        <span class="tm-chip">HTML</span>
        <span class="tm-chip">CSS</span>
        <span class="tm-chip">SQL</span>
        <span class="tm-chip">NoSQL (MongoDB)</span>
        <span class="tm-chip">Shell Scripting / Bash</span>
      </div>
    </details>
    <!-- 🌐 Front-End -->
    <details class="tm-group tm-card" open>
      <summary>🌐 Front-End</summary>
      <div class="tm-chips">
        <span class="tm-chip">Angular</span>
        <span class="tm-chip">Bootstrap</span>
        <span class="tm-chip">Pug (Jade)</span>
        <span class="tm-chip">Responsive Design</span>
        <span class="tm-chip">SPA Patterns</span>
      </div>
    </details>
    <!-- 🔌 Back-End & APIs -->
    <details class="tm-group tm-card" open>
      <summary>🔌 Back-End &amp; APIs</summary>
      <div class="tm-chips">
        <span class="tm-chip">Node.js</span>
        <span class="tm-chip">Express.js</span>
        <span class="tm-chip">Flask (basic)</span>
        <span class="tm-chip">REST APIs</span>
        <span class="tm-chip">JSON</span>
        <span class="tm-chip">Middleware</span>
        <span class="tm-chip">Auth Basics</span>
        <span class="tm-chip">Postman</span>
      </div>
    </details>
    <!-- 🗄️ Databases -->
    <details class="tm-group tm-card" open>
      <summary>🗄️ Databases</summary>
      <div class="tm-chips">
        <span class="tm-chip">SQLite</span>
        <span class="tm-chip">MongoDB</span>
        <span class="tm-chip">MySQL</span>
        <span class="tm-chip">SQL Server</span>
        <span class="tm-chip">Oracle</span>
        <span class="tm-chip">SQL Joins</span>
        <span class="tm-chip">Normalization (1NF–3NF)</span>
        <span class="tm-chip">Query Construction</span>
        <span class="tm-chip">JSON Data Handling</span>
      </div>
    </details>
    <!-- 🛠️ Dev Tools & Environments -->
    <details class="tm-group tm-card" open>
      <summary>🛠️ Dev Tools &amp; Environments</summary>
      <div class="tm-chips">
        <span class="tm-chip">Git</span>
        <span class="tm-chip">GitHub</span>
        <span class="tm-chip">GitLab</span>
        <span class="tm-chip">Replit</span>
        <span class="tm-chip">VS Code</span>
        <span class="tm-chip">Jupyter Notebook</span>
        <span class="tm-chip">npm</span>
        <span class="tm-chip">MongoDB Compass</span>
        <span class="tm-chip">SQLiteStudio</span>
        <span class="tm-chip">VirtualBox / VMware</span>
        <span class="tm-chip">Bash CLI</span>
      </div>
    </details>
    <!-- ☁️ Hosting & Deployment -->
    <details class="tm-group tm-card" open>
      <summary>☁️ Hosting &amp; Deployment</summary>
      <div class="tm-chips">
        <span class="tm-chip">GitHub Pages</span>
        <span class="tm-chip">PythonAnywhere</span>
        <span class="tm-chip">Replit Deploy</span>
      </div>
    </details>
    <!-- 🧪 Testing & QA -->
    <details class="tm-group tm-card" open>
      <summary>🧪 Testing &amp; QA</summary>
      <div class="tm-chips">
        <span class="tm-chip">Unit Testing (unittest / JUnit / PyTest)</span>
        <span class="tm-chip">Test Plans &amp; Coverage</span>
        <span class="tm-chip">Black-Box / White-Box</span>
        <span class="tm-chip">Regression Testing</span>
        <span class="tm-chip">API Response Validation</span>
        <span class="tm-chip">Logging &amp; Debugging</span>
      </div>
    </details>
    <!-- 🔐 Security -->
    <details class="tm-group tm-card" open>
      <summary>🔐 Security</summary>
      <div class="tm-chips">
        <span class="tm-chip">OWASP Top 10</span>
        <span class="tm-chip">CIA Triad</span>
        <span class="tm-chip">Threat Modeling</span>
        <span class="tm-chip">Input Validation</span>
        <span class="tm-chip">Parameterized SQL</span>
        <span class="tm-chip">SQL Injection Mitigation</span>
        <span class="tm-chip">XSS / CSRF Awareness</span>
        <span class="tm-chip">Secure Password Hashing</span>
        <span class="tm-chip">RBAC</span>
        <span class="tm-chip">Least Privilege</span>
        <span class="tm-chip">Encryption Basics</span>
        <span class="tm-chip">SSDLC</span>
      </div>
    </details>
    <!-- 🛍️ CMS & E-Commerce -->
    <details class="tm-group tm-card" open>
      <summary>🛍️ CMS &amp; E-Commerce</summary>
      <div class="tm-chips">
        <span class="tm-chip">WordPress</span>
        <span class="tm-chip">WooCommerce</span>
        <span class="tm-chip">SEO</span>
        <span class="tm-chip">SEM</span>
        <span class="tm-chip">Site Hardening</span>
      </div>
    </details>
    <!-- 💻 Platforms & OS -->
    <details class="tm-group tm-card" open>
      <summary>💻 Platforms &amp; OS</summary>
      <div class="tm-chips">
        <span class="tm-chip">Windows</span>
        <span class="tm-chip">Linux</span>
        <span class="tm-chip">macOS</span>
      </div>
    </details>
    <!-- 🌐 Networking & Admin -->
    <details class="tm-group tm-card" open>
      <summary>🌐 Networking &amp; Admin</summary>
      <div class="tm-chips">
        <span class="tm-chip">TCP/IP</span>
        <span class="tm-chip">DNS</span>
        <span class="tm-chip">DHCP</span>
        <span class="tm-chip">VPN</span>
        <span class="tm-chip">Firewalls</span>
        <span class="tm-chip">Active Directory</span>
        <span class="tm-chip">SCCM</span>
      </div>
    </details>
  </section>

  <!-- ====================================
       OTHER COURSEWORK PROJECTS (CARDS)
  ===================================== -->
  <section id="ocp" aria-labelledby="ocp-title">
    <h2 id="ocp-title">🧪 Other Coursework Projects</h2>
    <style>
      /* --- scoped to #ocp --- */
      #ocp {
        --accent:#39ff14;
        --card-bg: transparent;
        --chip-bg: rgba(57,255,20,0.08);
        margin: 1.5rem 0 2rem;
      }
      /* shared chip/card look to match your existing skills cards */
      #ocp .chip, #ocp .ocp-skill, #ocp .ocp-tag {
        display:inline-block; white-space:nowrap;
        border:1px solid var(--accent);
        background:var(--chip-bg);
        color:var(--accent);
        padding:.25rem .6rem; border-radius:999px; font-size:.9rem;
      }
      #ocp .chips { display:flex; flex-wrap:wrap; gap:.5rem; }
      #ocp .ocp-card {
        border:1px solid var(--accent);
        border-left-width:6px;
        border-radius:12px;
        padding:1rem;
        background:var(--card-bg);
      }
      #ocp .ocp-grid { display:grid; gap:1rem; }
      /* terminal-like header (subtle, but same green) */
      #ocp .ocp-shell {
        border:1px solid var(--accent);
        border-radius:12px;
        padding:.75rem;
        background: var(--card-bg);
        margin-bottom: .75rem;
      }
      #ocp .ocp-line { display:flex; gap:.5rem; flex-wrap:wrap; align-items:center; }
      #ocp .ocp-prompt { color: var(--accent); }
      #ocp .ocp-input {
        flex: 1 1 320px; min-width:240px;
        background: transparent;
        color: var(--accent);
        border:1px solid var(--accent);
        border-radius:999px; padding:.35rem .6rem;
      }
      #ocp .ocp-btn {
        border:1px solid var(--accent);
        color: var(--accent); background: var(--chip-bg);
        border-radius:999px; padding:.35rem .7rem; cursor:pointer;
      }
      /* card internals */
      #ocp .ocp-title { margin:0 0 .25rem; font-weight:700; color: var(--accent); }
      #ocp .ocp-sub { margin:.15rem 0 .6rem; opacity:.85; }
      #ocp .ocp-skill-list { display:flex; flex-wrap:wrap; gap:.5rem; margin-top:.35rem; }
      #ocp .ocp-tags { display:flex; flex-wrap:wrap; gap:.5rem; margin-top:.5rem; }
      /* remove any theme arrows from details elsewhere */
      #ocp details summary::-webkit-details-marker { display:none; }
      #ocp details summary { list-style:none; }
      @media (max-width: 420px){
        #ocp .ocp-input { min-width: 200px; }
        #ocp .ocp-skill, #ocp .ocp-tag { font-size:.85rem; }
      }
    </style>
    <!-- search + tags -->
    <div class="ocp-shell" role="region" aria-label="Coursework filter">
      <div class="ocp-line">
        <span class="ocp-prompt">$</span><span>projects --list</span>
        <span style="opacity:.8"># type to filter or click tags</span>
      </div>
      <div class="ocp-line">
        <label for="ocp-search" class="ocp-prompt" aria-hidden="true">$</label>
        <input id="ocp-search" class="ocp-input" type="search" placeholder="filter: security, api, c++, android, testing, mongodb..." aria-label="Filter projects">
        <button id="ocp-reset" class="ocp-btn" type="button">reset</button>
      </div>
      <div id="ocp-tagbar" class="ocp-tags"></div>
    </div>
    <!-- results -->
    <div id="ocp-grid" class="ocp-grid"></div>
    <!-- no-JS fallback -->
    <details open style="margin-top:.75rem">
      <summary>Fallback list (static)</summary>
      <ul>
        <li><strong>CS-250 — Software Development Lifecycle</strong>: SDLC plan (risk analysis, use cases, maintenance strategy)</li>
        <li><strong>CS-305 — Software Security</strong>: Banking-app threat modeling + mitigations (CIA, OWASP, parameterized SQL)</li>
        <li><strong>CS-360 — Mobile Architecture & Programming</strong>: Android grocery list app (Java, SQLite, intents, JSON)</li>
        <li><strong>CS-340 — Client/Server Development</strong>: REST API + MongoDB (Node/Express, CRUD, Postman)</li>
        <li><strong>CS-320 — Software Testing</strong>: Test plan + unit tests (unittest, coverage, black/white box)</li>
        <li><strong>CS-260 — Data Structures & Algorithms</strong>: Merge/Quick/Bubble; DFS/BFS; hash table (C++, complexity, recursion)</li>
        <li><strong>CS-315 — Operating Systems</strong>: Process scheduling + multithreaded app (threading, system calls)</li>
        <li><strong>CS-330 — Computer Graphics & Visualization</strong>: OpenGL 2D interface (render pipeline, transforms)</li>
      </ul>
    </details>

    
  <script>
      // --- Data (edit text here if you need to tweak wording) ---
      const OCP_ENTRIES = [
        {
          code:"CS-250",
          title:"Software Development Lifecycle",
          project:"Developed a software development plan with risk analysis, use cases, and maintenance strategy for a hypothetical car rental system.",
          skills:["SDLC Phases","Agile Process","Change Management","Maintenance Planning","UML"],
          tags:["process","uml","planning","agile"]
        },
        {
          code:"CS-305",
          title:"Software Security",
          project:"Security risk analysis for an online banking application, including threat modeling and countermeasures.",
          skills:["Vulnerability Identification","CIA Triad","OWASP Mitigations","Threat Modeling","Input Validation"],
          tags:["security","owasp","cia","risk"]
        },
        {
          code:"CS-360",
          title:"Mobile Architecture & Programming",
          project:"Created a mobile app prototype using Java and Android Studio to track grocery lists with SQLite integration.",
          skills:["Mobile Lifecycle","UI Design","Local Storage","Intent Handling","JSON Parsing","SQLite"],
          tags:["mobile","android","sqlite","java","ui"]
        },
        {
          code:"CS-340",
          title:"Client/Server Development",
          project:"Designed a RESTful API and connected it to a MongoDB backend using Node.js and Express, with a functional CRUD frontend.",
          skills:["API Routing","HTTP Methods","Middleware","Postman Testing","CRUD Operations","JSON"],
          tags:["api","backend","mongodb","node","express","crud"]
        },
        {
          code:"CS-320",
          title:"Software Testing",
          project:"Built a test plan for a file handling program and implemented unit tests using Python’s unittest.",
          skills:["Test Coverage","Test Case Design","Black/White Box","Test Automation","Python unittest"],
          tags:["testing","qa","python"]
        },
        {
          code:"CS-260",
          title:"Data Structures & Algorithms",
          project:"Implemented sorting algorithms (Merge, Quick, Bubble), graph traversal (DFS, BFS), and a basic hash table in C++.",
          skills:["Time Complexity Analysis","Memory Management","Recursion","Abstract Data Types","Graphs"],
          tags:["algorithms","c++","ds","sorting","graphs","hash"]
        },
        {
          code:"CS-315",
          title:"Operating Systems",
          project:"Simulated process scheduling using C++, created a multi-threaded application.",
          skills:["Threading","Concurrency","Scheduling Algorithms","System Calls","Memory Hierarchy"],
          tags:["systems","concurrency","threads","c++"]
        },
        {
          code:"CS-330",
          title:"Computer Graphics & Visualization",
          project:"Used OpenGL to create a simple 2D game interface with interactive elements.",
          skills:["Rendering Pipeline","Geometric Transformations","Coordinate Space Math","Buffers"],
          tags:["graphics","opengl","rendering","transforms"]
        }
      ];

      // --- Tag bar + filtering ---
      let OCP_ACTIVE = new Set();

      function ocpAllTags(){
        const s = new Set();
        OCP_ENTRIES.forEach(e => e.tags.forEach(t => s.add(t)));
        return Array.from(s).sort();
      }

      function ocpRenderTags(){
        const bar = document.getElementById('ocp-tagbar');
        bar.innerHTML = ocpAllTags().map(t =>
          `<button class="ocp-tag" data-tag="${t}" aria-pressed="${OCP_ACTIVE.has(t)}">${t}</button>`
        ).join('');
        bar.querySelectorAll('.ocp-tag').forEach(btn => {
          const tg = btn.dataset.tag;
          if (OCP_ACTIVE.has(tg)) btn.style.background = "var(--chip-bg)";
          btn.onclick = () => {
            OCP_ACTIVE.has(tg) ? OCP_ACTIVE.delete(tg) : OCP_ACTIVE.add(tg);
            ocpRenderTags(); ocpRenderFeed();
          };
        });
      }

      function ocpCard(e){
        return `
          <article class="ocp-card">
            <h3 class="ocp-title">${e.code} — ${e.title}</h3>
            <p class="ocp-sub"><strong>Project:</strong> ${e.project}</p>
            <div><strong>Skills:</strong>
              <div class="ocp-skill-list">
                ${e.skills.map(s => `<span class="ocp-skill">${s}</span>`).join('')}
              </div>
            </div>
            <div class="ocp-tags">
              ${e.tags.map(t => `<span class="ocp-tag" data-t="${t}" title="Filter by ${t}">${t}</span>`).join('')}
            </div>
          </article>
        `;
      }

      function ocpRenderFeed(){
        const grid = document.getElementById('ocp-grid');
        const q = (document.getElementById('ocp-search').value || '').toLowerCase().trim();
        const filtered = OCP_ENTRIES.filter(e => {
          const matchTags = OCP_ACTIVE.size === 0 || [...OCP_ACTIVE].some(t => e.tags.includes(t));
          const hay = (e.code + ' ' + e.title + ' ' + e.project + ' ' + e.skills.join(' ')).toLowerCase();
          const matchQuery = !q || hay.includes(q);
          return matchTags && matchQuery;
        });
        grid.innerHTML = filtered.map(ocpCard).join('') || `<div role="status" style="opacity:.8">no projects match your filter.</div>`;

        // make the inline tag chips also toggle filters
        grid.querySelectorAll('.ocp-tag').forEach(el => {
          el.onclick = () => {
            const tg = el.dataset.t;
            OCP_ACTIVE.has(tg) ? OCP_ACTIVE.delete(tg) : OCP_ACTIVE.add(tg);
            ocpRenderTags(); ocpRenderFeed();
          };
        });
      }

      document.addEventListener('DOMContentLoaded', () => {
        ocpRenderTags(); ocpRenderFeed();
        const input = document.getElementById('ocp-search');
        const reset = document.getElementById('ocp-reset');
        input.addEventListener('input', ocpRenderFeed);
        reset.addEventListener('click', () => {
          input.value = ''; OCP_ACTIVE = new Set(); ocpRenderTags(); ocpRenderFeed();
        });
      });
    </script>
  </section>

</section>


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
