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

 Completing my Computer Science program and assembling this ePortfolio has been a rewarding journey that brought together my academic projects, real-world work experience, and evolved problem-solving approach. Building this site challenged me to select and showcase my key strengths clearly, articulate them in plain language, and provide verifiable evidence—all of which reinforced my professional focus.

## What I’ve Learned

I've learned so many things throughout this program, it would be hard to name them all, honestly. Earlier in this Capstone course, I was asked to list the three most important skills I have learned. Now, at the end of this course, these three skills still stand out as most important to me:

**1. Programming in Multiple Languages:** I’ve built projects in Python, Java, C++, and JavaScript, which has made it easier to pick up new tools or frameworks and has given me flexibility for future roles.
**2. User Interface Design and Programming:** In my mobile architecture and programming course, I gained experience designing and coding interfaces that are actually enjoyable to use, which is essential for web and full-stack development.
**3. Problem-Solving and Debugging:** Almost every course required me to troubleshoot logic errors, find bugs, and figure out how to make my code work efficiently. This skill comes up constantly in real-world programming

To name just a few other things I have learned throughout my degree program, collaboration, communication, and working with databases, data structures and algorithms are a few that stand out. Below you can find summaries on what I learned about each of these.

### Collaboration 
I learned to structure code so other people can step in quickly: clear names, small focused functions, and comments that explain why a choice was made, not just what it does. Group work and code reviews taught me to keep logic modular and leave helpful breadcrumbs for the next person. Those habits map directly to Outcome 1 on collaboration and supported by the planning I captured for my capstone. 
 
### Communication
I got comfortable switching between technical detail and plain English—README instructions, user-facing prompts, and short demos that focus on outcomes first. My e-commerce work reinforced this: translating platform, hosting, and security work into clear updates for customers or vendors, and documenting steps so non-engineers can follow along. 
 
### Data Structures and Algorithms 
Across courses, I practiced choosing simple, predictable structures—lists, maps/dicts, queues—then measuring when sorting or searching variants actually help. I also learned to weigh clarity vs. performance and to use language-idiomatic tools (e.g., Python’s defaultdict, safe lookups) to keep behavior predictable. 

## This Portfolio

In this ePortfolio, you will find three enhancements I made to previously written code. When I planned my enhancements for this portfolio, I wanted to make sure I was focusing on skills that employers actually care about while also covering every course outcome. To keep everything manageable this term, I decided to use the same Corner Grocer App project for all three enhancement categories.


<section id="skills-demonstrated" class="skills-showcase" aria-labelledby="skills-title">
  <h2 id="skills-title">Skills Demonstrated</h2>

  <p class="section-intro">
    This is how I work: clean structure, readable code, and small, testable pieces.
    I lean front-end in a full-stack context—modular design, safe data handling, approachable UX, and secure habits.
    Each chip reflects something I actually implemented during my enhancements.
  </p>

  <style>
    .skills-showcase{
      --accent:#39ff14;
      --card-bg: transparent;
      --chip-bg: rgba(57,255,20,.08);
      margin: 1.5rem 0 2rem;
    }
    .skills-showcase h2{ margin-bottom:1rem; }
    .skills-showcase .section-intro{ opacity:.9; margin:.5rem 0 1rem; }

    .skills-grid{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
      gap:1rem;
    }
    .skill-card{
      border:1px solid var(--accent);
      border-left-width:6px;
      border-radius:12px;
      padding:1rem;
      background:var(--card-bg);
    }
    .skill-card h3{
      margin:0 0 .5rem;
      line-height:1.2;
      font-size:1.05rem;
      display:flex; align-items:center; gap:.5rem;
    }
    .skill-card h3 .icon{ font-size:1.2rem; }
    .skill-card p.sub{ margin:0 0 .75rem; font-size:.9rem; opacity:.85; }
    .chips{ display:flex; flex-wrap:wrap; gap:.5rem; }
    .chip{
      display:inline-block;
      border:1px solid var(--accent);
      background:var(--chip-bg);
      color:var(--accent);
      padding:.25rem .6rem;
      border-radius:999px;
      font-size:.9rem;
      white-space:nowrap;
    }
    @media (max-width:420px){
      .chips{ gap:.4rem; }
      .chip{ font-size:.85rem; }
    }
  </style>

  <div class="skills-grid">
    <!-- 1. Programming Proficiency (no tech names) -->
    <article class="skill-card">
      <h3><span class="icon">💻</span> Programming Proficiency</h3>
      <p class="sub">Habits that make code easier to write, read, and change.</p>
      <div class="chips">
        <span class="chip">Language Portability Across Stacks</span>
        <span class="chip">Algorithmic Problem-Solving</span>
        <span class="chip">Function Abstraction</span>
        <span class="chip">Readable, Testable Functions</span>
        <span class="chip">Idiomatic Refactoring</span>
        <span class="chip">Commit Hygiene & Versioning</span>
      </div>
    </article>
    <!-- 2. Software Design & Architecture -->
    <article class="skill-card">
      <h3><span class="icon">🧩</span> Software Design &amp; Architecture</h3>
      <p class="sub">Structure that keeps features maintainable and team-friendly.</p>
      <div class="chips">
        <span class="chip">Modular Architecture</span>
        <span class="chip">Separation of Concerns</span>
        <span class="chip">Reusability & Composition</span>
        <span class="chip">Basic Class Design</span>
        <span class="chip">Persistent Storage Design</span>
        <span class="chip">Schema Planning</span>
        <span class="chip">Backward-Compatible Iteration</span>
        <span class="chip">Scalability Mindset</span>
      </div>
    </article>
    <!-- 3. Data Handling & Structures -->
    <article class="skill-card">
      <h3><span class="icon">🗄️</span> Data Handling &amp; Structures</h3>
      <p class="sub">Moving, storing, and guarding data responsibly.</p>
      <div class="chips">
        <span class="chip">File I/O Patterns</span>
        <span class="chip">Relational Query Construction</span>
        <span class="chip">Database Integration</span>
        <span class="chip">Safe Data Access</span>
        <span class="chip">Map/Dictionary Utilities</span>
        <span class="chip">String Normalization</span>
        <span class="chip">Input Validation</span>
        <span class="chip">Robust Error Handling</span>
      </div>
    </article>
    <!-- 4. Data Processing & Output -->
    <article class="skill-card">
      <h3><span class="icon">📊</span> Data Processing &amp; Output</h3>
      <p class="sub">Turning raw values into results people can use.</p>
      <div class="chips">
        <span class="chip">Sorting (Alpha / Frequency)</span>
        <span class="chip">Search & Filtering</span>
        <span class="chip">Usable Data Displays</span>
        <span class="chip">Histogram & Summary Output</span>
      </div>
    </article>
    <!-- 5. Interface Design & Usability -->
    <article class="skill-card">
      <h3><span class="icon">🧭</span> Interface Design &amp; Usability</h3>
      <p class="sub">Flows that are predictable and easy to navigate.</p>
      <div class="chips">
        <span class="chip">Menu Architecture</span>
        <span class="chip">Guided Prompts</span>
        <span class="chip">Progressive Disclosure</span>
        <span class="chip">UX-Focused Iteration</span>
      </div>
    </article>
    <!-- 6. Documentation & Readability -->
    <article class="skill-card">
      <h3><span class="icon">📝</span> Documentation &amp; Readability</h3>
      <p class="sub">Code that explains itself and is easy to hand off.</p>
      <div class="chips">
        <span class="chip">Concise Docstrings & Headers</span>
        <span class="chip">Self-Documenting Code</span>
        <span class="chip">Clear Change Notes</span>
      </div>
    </article>
  </div>
</section>


<!-- =========================================================
=  SECTION 2 — LANGUAGES & TECH I’M FAMILIAR WITH (chips)    =
=  (all tech names live here; no overlap with skills above)  =
========================================================= -->
<section id="tech-familiar" class="tech-simple" aria-labelledby="tech-title">
  <h2 id="tech-title">Languages &amp; Tech I’m Familiar With</h2>

  <p class="section-intro">
    Broader toolset I use across coursework and projects—languages, web frameworks, databases, testing,
    security, and dev tools (Git/GitHub, VS Code, Replit, Postman). Grouped for quick scanning.
  </p>

  <style>
    .tech-simple{
      --accent:#39ff14;
      --chip-bg: rgba(57,255,20,.08);
      margin:1.5rem 0 2rem;
    }
    .tech-simple .section-intro{ opacity:.9; margin:.5rem 0 1rem; }
    .tech-grid{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
      gap:1rem 1.25rem;
    }
    .tech-cat{ margin:.25rem 0 .5rem; color:var(--accent); font-size:1rem; }
    .chiplist{ display:flex; flex-wrap:wrap; gap:.5rem; margin:0; padding:0; list-style:none; }
    .chiplist .chip{
      border:1px solid var(--accent);
      background:var(--chip-bg);
      color:var(--accent);
      padding:.25rem .6rem; border-radius:999px; font-size:.9rem; white-space:nowrap;
    }
    @media (max-width:420px){ .chiplist .chip{ font-size:.85rem; } }
  </style>

  <div class="tech-grid">
    <div>
      <h3 class="tech-cat">🧠 Languages</h3>
      <ul class="chiplist">
        <li class="chip">Python</li>
        <li class="chip">Java</li>
        <li class="chip">C++</li>
        <li class="chip">JavaScript</li>
        <li class="chip">HTML</li>
        <li class="chip">CSS</li>
        <li class="chip">SQL</li>
        <li class="chip">NoSQL (MongoDB)</li>
        <li class="chip">Shell / Bash</li>
      </ul>
    </div>
    <div>
      <h3 class="tech-cat">🌐 Front-End</h3>
      <ul class="chiplist">
        <li class="chip">Angular</li>
        <li class="chip">Bootstrap</li>
        <li class="chip">Pug (Jade)</li>
        <li class="chip">Responsive Design</li>
        <li class="chip">SPA Patterns</li>
      </ul>
    </div>
    <div>
      <h3 class="tech-cat">🔌 Back-End &amp; APIs</h3>
      <ul class="chiplist">
        <li class="chip">Node.js</li>
        <li class="chip">Express.js</li>
        <li class="chip">Flask (basic)</li>
        <li class="chip">REST APIs</li>
        <li class="chip">JSON</li>
        <li class="chip">Postman</li>
        <li class="chip">Middleware</li>
        <li class="chip">Auth Basics</li>
      </ul>
    </div>
    <div>
      <h3 class="tech-cat">🗄️ Databases</h3>
      <ul class="chiplist">
        <li class="chip">SQLite</li>
        <li class="chip">MongoDB</li>
        <li class="chip">MySQL</li>
        <li class="chip">SQL Server</li>
        <li class="chip">Oracle</li>
        <li class="chip">SQL Joins</li>
        <li class="chip">Normalization (1NF–3NF)</li>
        <li class="chip">Query Construction</li>
        <li class="chip">JSON Data Handling</li>
      </ul>
    </div>
    <div>
      <h3 class="tech-cat">🛠️ Dev Tools &amp; Environments</h3>
      <ul class="chiplist">
        <li class="chip">Git</li>
        <li class="chip">GitHub</li>
        <li class="chip">GitLab</li>
        <li class="chip">Replit</li>
        <li class="chip">VS Code</li>
        <li class="chip">Jupyter Notebook</li>
        <li class="chip">npm</li>
        <li class="chip">MongoDB Compass</li>
        <li class="chip">SQLiteStudio</li>
        <li class="chip">VirtualBox / VMware</li>
        <li class="chip">Bash CLI</li>
      </ul>
    </div>
    <div>
      <h3 class="tech-cat">☁️ Hosting &amp; Deployment</h3>
      <ul class="chiplist">
        <li class="chip">GitHub Pages</li>
        <li class="chip">PythonAnywhere</li>
        <li class="chip">Replit Deploy</li>
      </ul>
    </div>
    <div>
      <h3 class="tech-cat">🧪 Testing &amp; QA</h3>
      <ul class="chiplist">
        <li class="chip">unittest / JUnit / PyTest</li>
        <li class="chip">Test Plans &amp; Coverage</li>
        <li class="chip">Black-Box / White-Box</li>
        <li class="chip">Regression Testing</li>
        <li class="chip">API Response Validation</li>
        <li class="chip">Logging & Debugging</li>
      </ul>
    </div>
    <div>
      <h3 class="tech-cat">🔐 Security</h3>
      <ul class="chiplist">
        <li class="chip">OWASP Top 10</li>
        <li class="chip">CIA Triad</li>
        <li class="chip">Threat Modeling</li>
        <li class="chip">Input Validation</li>
        <li class="chip">Parameterized SQL</li>
        <li class="chip">SQL Injection Mitigation</li>
        <li class="chip">XSS / CSRF Awareness</li>
        <li class="chip">Secure Password Hashing</li>
        <li class="chip">RBAC</li>
        <li class="chip">Least Privilege</li>
        <li class="chip">Encryption Basics</li>
        <li class="chip">SSDLC</li>
      </ul>
    </div>
    <div>
      <h3 class="tech-cat">🏢 Enterprise &amp; IT</h3>
      <ul class="chiplist">
        <li class="chip">ServiceNow</li>
        <li class="chip">SharePoint</li>
        <li class="chip">Salesforce</li>
        <li class="chip">Zendesk</li>
        <li class="chip">Citrix</li>
        <li class="chip">Epic</li>
        <li class="chip">Avaya</li>
        <li class="chip">Demandware</li>
        <li class="chip">Domain Mgmt / Backups</li>
      </ul>
    </div>
  </div>
</section>

<!-- =========================================================
=  SECTION 3 — OTHER COURSEWORK PROJECTS (accordions)        =
========================================================= -->
<section id="coursework-projects" class="ocp-accordion" aria-labelledby="ocp-title">
  <h2 id="ocp-title">Other Coursework Projects (Not in ePortfolio Artifacts)</h2>

  <p class="section-intro">
    These aren’t the capstone artifacts—these are other course projects that shaped my skill set:
    testing a Python file-handler with unit tests, a REST API with Node/Express + MongoDB, an Android app with SQLite,
    OS concurrency work in C++, SDLC/UML planning, and a security risk analysis aligned to OWASP.
  </p>

  <style>
    .ocp-accordion{
      --accent:#39ff14;
      --chip-bg: rgba(57,255,20,.08);
      margin:1.5rem 0 2rem;
    }
    .ocp-accordion .section-intro{ opacity:.9; margin:.5rem 0 1rem; }
    .ocp-controls{ display:flex; gap:.5rem; margin-bottom:.75rem; }
    .ocp-btn{
      border:1px solid var(--accent);
      color:var(--accent);
      background:var(--chip-bg);
      border-radius:999px;
      padding:.35rem .7rem;
      cursor:pointer;
    }
    .ocp-list{ display:grid; gap:.75rem; }
    .ocp-item{
      border:1px solid var(--accent);
      border-left-width:6px;
      border-radius:12px;
      background:transparent;
      overflow:hidden;
    }
    .ocp-item summary{
      cursor:pointer; user-select:none; outline:none;
      padding:.75rem 1rem;
      color:var(--accent);
      font-weight:700;
    }
    .ocp-item summary::-webkit-details-marker{ display:none; }
    .ocp-item summary::before{ content:"▸ "; }
    .ocp-item[open] summary::before{ content:"▾ "; }
    .ocp-body{ padding:.2rem 1rem 1rem; }
    .ocp-body p{ margin:.25rem 0 .6rem; }
    .ocp-skilllist{
      display:flex; flex-wrap:wrap; gap:.5rem;
      list-style:none; margin:0; padding:0;
    }
    .ocp-skilllist .chip{
      border:1px solid var(--accent);
      background:var(--chip-bg);
      color:var(--accent);
      padding:.25rem .6rem; border-radius:999px; font-size:.9rem; white-space:nowrap;
    }
    @media (max-width:420px){ .ocp-skilllist .chip{ font-size:.85rem; } }
  </style>

  <div class="ocp-controls">
    <button type="button" class="ocp-btn" id="ocp-open">Expand all</button>
    <button type="button" class="ocp-btn" id="ocp-close">Collapse all</button>
  </div>

  <div class="ocp-list" id="ocp-list">
    <details class="ocp-item">
      <summary>CS-250 — Software Development Lifecycle</summary>
      <div class="ocp-body">
        <p><strong>Project:</strong> SDLC plan with risk analysis, use cases, and maintenance strategy for a car-rental system.</p>
        <ul class="ocp-skilllist">
          <li class="chip">SDLC Phases</li>
          <li class="chip">Agile Process</li>
          <li class="chip">Change Management</li>
          <li class="chip">Maintenance Planning</li>
          <li class="chip">UML</li>
        </ul>
      </div>
    </details>
    <details class="ocp-item">
      <summary>CS-305 — Software Security</summary>
      <div class="ocp-body">
        <p><strong>Project:</strong> Security risk analysis for an online banking app with threat modeling and countermeasures.</p>
        <ul class="ocp-skilllist">
          <li class="chip">CIA Triad</li>
          <li class="chip">OWASP Mitigations</li>
          <li class="chip">Threat Modeling</li>
          <li class="chip">Input Validation</li>
          <li class="chip">Parameterized SQL</li>
          <li class="chip">RBAC / Least Privilege</li>
        </ul>
      </div>
    </details>
    <details class="ocp-item">
      <summary>CS-360 — Mobile Architecture &amp; Programming</summary>
      <div class="ocp-body">
        <p><strong>Project:</strong> Android grocery-list app (Java + SQLite), with lifecycle, intents, and JSON parsing.</p>
        <ul class="ocp-skilllist">
          <li class="chip">Android Lifecycle</li>
          <li class="chip">UI Design</li>
          <li class="chip">SQLite</li>
          <li class="chip">Intents</li>
          <li class="chip">JSON Parsing</li>
        </ul>
      </div>
    </details>
    <details class="ocp-item">
      <summary>CS-340 — Client/Server Development</summary>
      <div class="ocp-body">
        <p><strong>Project:</strong> RESTful API with Node.js/Express and MongoDB backend; CRUD frontend; validated with Postman.</p>
        <ul class="ocp-skilllist">
          <li class="chip">API Routing</li>
          <li class="chip">HTTP Methods</li>
          <li class="chip">Middleware</li>
          <li class="chip">CRUD Operations</li>
          <li class="chip">Postman Testing</li>
        </ul>
      </div>
    </details>
    <details class="ocp-item">
      <summary>CS-320 — Software Testing</summary>
      <div class="ocp-body">
        <p><strong>Project:</strong> Test plan + unit tests (Python unittest) for a file-handling program.</p>
        <ul class="ocp-skilllist">
          <li class="chip">Test Coverage</li>
          <li class="chip">Test Case Design</li>
          <li class="chip">Black-Box / White-Box</li>
          <li class="chip">Test Automation</li>
        </ul>
      </div>
    </details>
    <details class="ocp-item">
      <summary>CS-260 — Data Structures &amp; Algorithms</summary>
      <div class="ocp-body">
        <p><strong>Project:</strong> Merge/Quick/Bubble sorts, DFS/BFS, and a basic hash table in C++.</p>
        <ul class="ocp-skilllist">
          <li class="chip">Time Complexity</li>
          <li class="chip">Recursion</li>
          <li class="chip">Graphs</li>
          <li class="chip">Hashing</li>
          <li class="chip">Memory Management</li>
        </ul>
      </div>
    </details>
    <details class="ocp-item">
      <summary>CS-315 — Operating Systems</summary>
      <div class="ocp-body">
        <p><strong>Project:</strong> Process scheduling simulation and a multithreaded C++ application.</p>
        <ul class="ocp-skilllist">
          <li class="chip">Threading</li>
          <li class="chip">Concurrency</li>
          <li class="chip">Scheduling Algorithms</li>
          <li class="chip">System Calls</li>
          <li class="chip">Memory Hierarchy</li>
        </ul>
      </div>
    </details>
    <details class="ocp-item">
      <summary>CS-330 — Computer Graphics &amp; Visualization</summary>
      <div class="ocp-body">
        <p><strong>Project:</strong> OpenGL 2D interface with interactive elements.</p>
        <ul class="ocp-skilllist">
          <li class="chip">Rendering Pipeline</li>
          <li class="chip">Geometric Transformations</li>
          <li class="chip">Coordinate Space Math</li>
          <li class="chip">Buffers</li>
        </ul>
      </div>
    </details>
  </div>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const openBtn  = document.getElementById('ocp-open');
      const closeBtn = document.getElementById('ocp-close');
      const items    = () => document.querySelectorAll('#coursework-projects .ocp-item');
      openBtn?.addEventListener('click', () => items().forEach(d => d.open = true));
      closeBtn?.addEventListener('click', () => items().forEach(d => d.open = false));
    });
  </script>
</section>
