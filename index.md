---
layout: default
title: Home
---

<!-- Simple nav -->
<nav style="margin-bottom: 20px;">
  <a href="./index.html">Home</a> |
  <a href="./enhancement-1.md">Enhancement 1</a> |
  <a href="./enhancement-2.md">Enhancement 2</a> |
  <a href="./enhancement-3.md">Enhancement 3</a> |
   <a href="https://corner-grocer-alyshaspradlin.replit.app">Enhancement Demo</a> |
  </nav>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cascadia+Code:ital,wght@0,200..700;1,200..700&family=Cascadia+Mono:ital,wght@0,200..700;1,200..700&family=DotGothic16&family=Fira+Code:wght@300..700&family=Handjet:wght@100..900&family=Jersey+15&family=Jersey+20&family=Jersey+25&family=Pixelify+Sans:wght@400..700&family=Press+Start+2P&family=Share+Tech&family=Share+Tech+Mono&family=Silkscreen:wght@400;700&family=VT323&display=swap" rel="stylesheet">

 .press-scope h1{
    font-family: "Press Start 2P", system-ui, monospace;
    text-align: center;
    font-weight: 400;        /* Press Start 2P only ships as 400 */
    letter-spacing: .5px;
    line-height: 1.25;
  }

  /* Scoped to this section so it won't fight the theme */
    .skills-showcase { --accent:#39ff14; --card-bg: transparent; --chip-bg: rgba(57,255,20,.08); }
    .skills-showcase * { box-sizing: border-box; }
    .skills-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
      margin: 1rem 0 2rem;
    }
    .skill-card {
      border: 1px solid var(--accent);
      border-left-width: 6px;
      border-radius: 12px;
      padding: 1rem;
      background: var(--card-bg);
      display: flex;
      flex-direction: column;
      height: 100%;
    }
    .skill-card h3 {
      margin: 0 0 .4rem;
      line-height: 1.2;
      font-size: 1.05rem;
      display: flex; align-items: center; gap: .5rem;
      color: var(--accent);
    }
    .skill-card h3 .icon { filter: saturate(.9); }
    .skill-card p.sub { margin: 0 0 .5rem; font-size: .9rem; opacity: .85; }
    .chips { display: flex; flex-wrap: wrap; gap: .5rem; align-items: flex-start; }
    .chip {
      display: inline-block;
      border: 1px solid var(--accent);
      background: var(--chip-bg);
      padding: .25rem .6rem;
      border-radius: 999px;
      font-size: .9rem;
      max-width: 100%;
      /* key fixes so chips don't escape cards */
      white-space: normal;              /* allow wrapping */
      overflow-wrap: anywhere;          /* break long words */
    }
    /* Collapsible controls */
    .skill-card details { margin-top: .25rem; }
    .skill-card summary {
      cursor: pointer; user-select: none; outline: none;
      font-size: .9rem; opacity: .9; margin: .25rem 0 .5rem;
    }
    .skill-card summary::-webkit-details-marker { display: none; }
    .skill-card summary::before { content: "▸ "; }
    .skill-card details[open] summary::before { content: "▾ "; }
    @media (max-width: 420px) {
      .chip { font-size: .85rem; }
    }

<!-- Typed header -->
<center> <h1 id="typed-header">Welcome to my ePortfolio</h1></center>

# About Me
Hello! My name is Alysha Pursley, and I am currently pursuing a degree in Computer Science with a focus on Software Development at Southern New Hampshire University. I have a strong passion for creating engaging, user-friendly interfaces and developing websites and applications that are both functional and visually appealing. My goal is to become a skilled front-end or full-stack developer, where I can bring ideas to life through innovative design and efficient coding. Throughout my studies, I’ve gained valuable experience in various programming languages and development tools, which I am eager to apply in real-world projects. This portfolio reflects my dedication, growth, and the skills I’ve cultivated so far, and I look forward to contributing to exciting tech solutions in the future.

## Capstone & Program Takeaways
I learned how to turn rough ideas into screens that make sense. That means planning the flow first, then building layouts with readable typography, sensible spacing, and color choices that don’t fight the content. I treat accessibility as a basic requirement, not an extra—keyboard paths, focus states, and contrast checks are part of how I work. Responsive behavior and small interaction details (like validation messages and loading hints) matter, because they’re the difference between “it works” and “it feels right.”

I also learned to structure front-end code so it stays easy to change. Breaking features into components, keeping concerns separate, and using clear, consistent names for files, functions, and variables makes the code understandable to someone new. Small, focused commits and straightforward Git/GitHub workflows keep reviews calm and mistakes easy to spot. When something breaks, I lean on targeted logs, step-through debugging, and simple tests for the tricky parts instead of guessing.

Finally, I learned to connect features to real data without surprises. I’m comfortable with basic CRUD, simple schemas, and the patterns that keep data predictable—validation on input, helpful error messages, and parameterized queries when SQL is involved. I make sure the interface always reflects the true state of the data, including loading and failure states, so users aren’t left guessing. That discipline keeps the UI honest and builds trust in what the app is showing.

Completing my capstone truly brought my entire degree together. It challenged me to be precise in every aspect—carefully selecting what to include, organizing my ideas logically, and telling a compelling story. Building the ePortfolio was especially valuable; it sharpened my skills in writing clear instructions, explaining trade-offs, and documenting processes thoroughly. Throughout this project, I reaffirmed my commitment to producing quality work, communicating ideas clearly, and establishing strong foundations for future success. This experience not only demonstrated my technical abilities but also reinforced my dedication to professionalism and continuous improvement in all my endeavors.


<div class="skills-grid">
    <!-- 1 -->
    <article class="skill-card">
      <h3>Programming Proficiency</h3>
      <p class="sub">Core languages and habits that make code easier to write, read, and change.</p>
      <details>
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
      <h3>Software Design &amp; Architecture</h3>
      <p class="sub">Structure that keeps features maintainable and team-friendly.</p>
      <details>
        <summary>Show skills</summary>
        <div class="chips">
          <span class="chip">Software Design Principles</span>
          <span class="chip">Modular Architecture &amp; Design</span>
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
      <h3>Data Handling &amp; Structures</h3>
      <p class="sub">Moving, storing, and guarding data responsibly.</p>
      <details>
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
      <h3> Data Processing &amp; Output</h3>
      <p class="sub">Turning raw values into results people can use.</p>
      <details>
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
      <h3>Interface Design &amp; Usability</h3>
      <p class="sub">Flows that are predictable and easy to navigate.</p>
      <details>
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
      <h3>Documentation &amp; Readability</h3>
      <p class="sub">Code that explains itself and is easy to hand off.</p>
      <details>
        <summary>Show skills</summary>
        <div class="chips">
          <span class="chip">Code Documentation</span>
          <span class="chip">Commenting and Readability</span>
        </div>
      </details>
    </article>
  </div>
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
