---
layout: default
title: Home
---

<!-- Simple nav -->
<nav style="margin-bottom: 20px;">
  <a href="https://apursley2012.github.io/eportfolio/">Home</a> |
  <a href="./enhancement-one-narrative">Enhancement 1 Narrative</a> |
  <a href="./enhancement-two-narrative">Enhancement 2 Narrative</a> |
  <a href="./enhancement-three-narrative">Enhancement 3 Narrative</a> |
   <a href="https://corner-grocer-alyshaspradlin.replit.app">Enhancement Demo</a> |
  </nav>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cascadia+Code:ital,wght@0,200..700;1,200..700&family=Cascadia+Mono:ital,wght@0,200..700;1,200..700&family=DotGothic16&family=Fira+Code:wght@300..700&family=Handjet:wght@100..900&family=Jersey+15&family=Jersey+20&family=Jersey+25&family=Pixelify+Sans:wght@400..700&family=Press+Start+2P&family=Share+Tech&family=Share+Tech+Mono&family=Silkscreen:wght@400;700&family=VT323&display=swap" rel="stylesheet">


 
<!-- Typed header -->
<center> <h1 id="typed-header">Welcome to my ePortfolio</h1></center>

# About Me
Hello! My name is Alysha Pursley, and I am currently finishing up a degree in Computer Science, with a focus on Software Development, at Southern New Hampshire University. I have a strong passion for creating engaging, user-friendly interfaces and developing websites and applications that are both functional and visually appealing. My goal is to become a skilled front-end or full-stack developer, where I can bring ideas to life through innovative design and efficient coding. Throughout my studies, I’ve gained valuable experience in various programming languages and development tools, which I am eager to apply in real-world projects. This portfolio reflects my dedication, growth, and the skills I’ve cultivated so far, and I look forward to contributing to exciting tech solutions in the future.

Completing my Computer Science program and assembling this ePortfolio has been a rewarding journey that brought together my academic projects, real-world work experience, and evolved problem-solving approach. Building this site challenged me to select and showcase my key strengths clearly, articulate them in plain language, and provide verifiable evidence—all of which reinforced my professional focus.

<!-- ==============================
     REVIEWS & INSTRUCTOR FEEDBACK
     Cards + 5-star outlines + swipe
     (Hacker theme compatible)
================================= -->
<section id="reviews" class="reviews-carousel" aria-labelledby="reviews-title">
  <h2 id="reviews-title">Reviews &amp; Instructor Feedback</h2>
  <p class="rc-intro">Highlights from course feedback. Stars are based on letter grade<br> (A=★★★★★, B=★★★★, C=★★★, D=★★, F=★).</p>

  <style>
    .reviews-carousel{
      --accent:#39ff14;
      --chip-bg: rgba(57,255,20,.08);
      margin:1.75rem 0 2.25rem;
    }
    .reviews-carousel h2{ margin-bottom:.35rem; }
    .rc-intro{ opacity:.9; margin:.25rem 0 1rem; }

    .rc-shell{
      display:grid;
      grid-template-columns:auto 1fr auto;
      align-items:center;
      gap:.5rem;
    }
    .rc-nav{
      border:1px solid var(--accent);
      background:var(--chip-bg);
      color:var(--accent);
      border-radius:999px;
      padding:.35rem .7rem;
      cursor:pointer;
      user-select:none;
    }
    .rc-nav:disabled{ opacity:.4; cursor:not-allowed; }

    .rc-viewport{
      overflow:hidden;
      border-radius:12px;
    }
    .rc-track{
      display:flex;
      transition:transform .35s ease;
      will-change:transform;
    }

    .rc-card{
      min-width:100%;
      box-sizing:border-box;
      border:1px solid var(--accent);
      border-left-width:6px;
      border-radius:12px;
      background:transparent;
      padding:1rem;
    }
    .rc-top{
      display:flex; align-items:flex-start; justify-content:space-between;
      gap:.75rem; flex-wrap:wrap;
      margin-bottom:.5rem;
    }
    .rc-course{
      color:var(--accent);
      font-weight:700;
      margin-bottom:.15rem;
    }
    .rc-meta{ opacity:.85; font-size:.95rem; }
    blockquote.rc-quote{
      margin:.35rem 0 .6rem; padding:0;
      font-style:italic; line-height:1.5;
    }
    .rc-tags{ display:flex; flex-wrap:wrap; gap:.5rem; }
    .rc-tag{
      border:1px solid var(--accent);
      background:var(--chip-bg);
      color:var(--accent);
      padding:.2rem .55rem;
      border-radius:999px;
      font-size:.85rem;
      white-space:nowrap;
    }

    .rc-stars{ display:flex; gap:.15rem; align-items:center; }
    .rc-star{ width:20px; height:20px; display:inline-block; }
    .rc-star svg{
      width:100%; height:100%;
      stroke:var(--accent); stroke-width:1.3;
      fill:transparent; opacity:.55;
    }
    .rc-star.filled svg{ fill:var(--accent); opacity:1; }

    .rc-dots{
      display:flex; gap:.4rem; justify-content:center;
      margin-top:.6rem;
    }
    .rc-dot{
      width:8px; height:8px; border-radius:50%;
      border:1px solid var(--accent);
      background:transparent; cursor:pointer;
    }
    .rc-dot.active{ background:var(--accent); }

    @media (max-width:420px){
      .rc-card{ padding:.85rem; }
    }
  </style>

  <div class="rc-shell" role="region" aria-label="Reviews carousel">
    <button class="rc-nav rc-prev" aria-label="Previous review">◂</button>
    <div class="rc-viewport">
      <div class="rc-track" id="rc-track"><!-- cards injected by JS --></div>
    </div>
    <button class="rc-nav rc-next" aria-label="Next review">▸</button>
  </div>
  <div class="rc-dots" id="rc-dots" role="tablist" aria-label="Slides"></div>

  <template id="rc-card-tpl">
    <article class="rc-card">
      <div class="rc-top">
        <div>
          <div class="rc-course"></div>
          <div class="rc-meta"></div>
        </div>
        <div class="rc-stars" aria-label="Rating out of 5"></div>
      </div>
      <blockquote class="rc-quote"></blockquote>
      <div class="rc-tags"></div>
    </article>
  </template>

  <script>
    const REVIEWS = [
      {
        course: "CS370: Current/Emerging Trends in Computer Science",
        reviewer: "Dr. Hawk",
        grade: "A",
        quote: "You provided a concise explanation of how neural networks operate, effectively outlining the roles of the input, hidden, and output layers. This was particularly strong in simplifying complex concepts, making them accessible to a non-technical audience. Your identification of legal concerns was on point and relevant.",
        tags: ["Clarity", "AI", "Neural Networks", "Accessible Language"]
      },
      {
        course: "CS465: Full Stack Development I",
        reviewer: "Instructor Benyam Heyi",
        grade: "B",
        quote: "Great work on outlining all the requirements of the rubric—your structure and coverage are well thought out. For future submissions, please make sure to also complete the API endpoints table. Including this information will significantly enhance the quality of your Software Design Document (SDD).",
        tags: ["API", "SDD", "Technical Completeness", "Communication"]
      },
      {
        course: "CS499: Computer Science Capstone",
        reviewer: "Instructor Ramsey Kraya",
        grade: "A",
        quote: "Your Milestone Four submission is an excellent example of a well-executed database integration. You successfully transitioned your Corner Grocer application from in-memory data handling to a persistent SQLite backend, while maintaining original functionality and improving user experience.",
        tags: ["Database Integration", "SQLite", "Persistence", "User Experience"]
      }
    ];

    function gradeToRating(grade){
      const L = String(grade || '').trim().toUpperCase().charAt(0);
      if (L === 'A') return 5;
      if (L === 'B') return 4;
      if (L === 'C') return 3;
      if (L === 'D') return 2;
      return 1;
    }

    function starSVG(filled){
      return `
        <span class="rc-star ${filled ? 'filled' : ''}" aria-hidden="true">
          <svg viewBox="0 0 24 24" focusable="false">
            <path d="M12 17.27l-5.18 3.03 1.39-5.95L3 9.74l6.09-.52L12 3.5l2.91 5.72 6.09.52-5.21 4.61 1.39 5.95z"/>
          </svg>
        </span>`;
    }
    function renderStars(rating){
      let out = '';
      for (let i=1;i<=5;i++) out += starSVG(i <= rating);
      return out;
    }

    const track = document.getElementById('rc-track');
    const dots  = document.getElementById('rc-dots');
    const tpl   = document.getElementById('rc-card-tpl');

    function makeCard(item){
      const node = tpl.content.firstElementChild.cloneNode(true);
      node.querySelector('.rc-course').textContent = item.course;
      node.querySelector('.rc-meta').textContent   = `${item.reviewer} • Grade: ${item.grade}`;
      node.querySelector('.rc-quote').textContent  = `“${item.quote}”`;
      node.querySelector('.rc-stars').innerHTML   = renderStars(gradeToRating(item.grade));
      const tags = node.querySelector('.rc-tags');
      (item.tags || []).forEach(t => {
        const span = document.createElement('span');
        span.className = 'rc-tag';
        span.textContent = t;
        tags.appendChild(span);
      });
      return node;
    }

    function renderAll(){
      track.innerHTML = '';
      REVIEWS.forEach(r => track.appendChild(makeCard(r)));
      dots.innerHTML = REVIEWS.map((_,i)=>`<button class="rc-dot" data-i="${i}" aria-label="Slide ${i+1}"></button>`).join('');
      updateUI();
      dots.querySelectorAll('.rc-dot').forEach(b => b.addEventListener('click', () => goTo(+b.dataset.i)));
    }

    let index = 0;
    const prevBtn = document.querySelector('.rc-prev');
    const nextBtn = document.querySelector('.rc-next');

    function goTo(i){
      const max = REVIEWS.length - 1;
      index = Math.max(0, Math.min(max, i));
      const vw = document.querySelector('.rc-viewport').clientWidth;
      track.style.transform = `translateX(${-index * vw}px)`;
      updateUI();
    }
    function updateUI(){
      const max = REVIEWS.length - 1;
      prevBtn.disabled = index === 0;
      nextBtn.disabled = index === max;
      dots.querySelectorAll('.rc-dot').forEach((d, i) => {
        d.classList.toggle('active', i === index);
      });
    }

    prevBtn.addEventListener('click', () => goTo(index - 1));
    nextBtn.addEventListener('click', () => goTo(index + 1));
    window.addEventListener('resize', () => goTo(index));

    let startX = null, deltaX = 0;
    const viewport = document.querySelector('.rc-viewport');
    viewport.addEventListener('touchstart', (e) => { startX = e.touches[0].clientX; deltaX = 0; }, {passive:true});
    viewport.addEventListener('touchmove',  (e) => { if(startX!==null) deltaX = e.touches[0].clientX - startX; }, {passive:true});
    viewport.addEventListener('touchend',   () => {
      if (startX !== null){
        if (deltaX < -40) goTo(index + 1);
        if (deltaX >  40) goTo(index - 1);
      }
      startX = null; deltaX = 0;
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft')  goTo(index - 1);
      if (e.key === 'ArrowRight') goTo(index + 1);
    });

    document.addEventListener('DOMContentLoaded', renderAll);
  </script>
</section>


## What I’ve Learned

I've learned so many things throughout this program, it would be hard to name them all, honestly. Earlier in this Capstone course, I was asked to list the three most important skills I have learned. Now, at the end of this course, these three skills still stand out as most important to me:

### Programming in Multiple Languages
I’ve built projects in Python, Java, C++, and JavaScript, which has made it easier to pick up new tools or frameworks and has given me flexibility for future roles.<br>

### User Interface Design and Programming
In my mobile architecture and programming course, I gained experience designing and coding interfaces that are actually enjoyable to use, which is essential for web and full-stack development.<br>

### Problem-Solving and Debugging
Almost every course required me to troubleshoot logic errors, find bugs, and figure out how to make my code work efficiently. This skill comes up constantly in real-world programming.<br>

To name just a few other things I have learned throughout my degree program, collaboration, communication, and working with databases, data structures and algorithms are a few that stand out. Below you can find summaries on what I learned about each of these.

### Collaboration 
I learned to structure code so other people can quickly and easily understand exactly whats doing what: clear names, small focused functions, and comments that explain why a choice was made, not just what it does. I learned how to keep logic modular and leave helpful breadcrumbs for the next person. Those habits map directly to Outcome 1 on collaboration and supported by the planning I captured for my capstone. 
 
### Communication
I got comfortable switching between technical detail and plain English—README instructions, user-facing prompts, and short demos that focus on outcomes first. Some personal projects I've been working on helped reinforce this: translating platform, hosting, and security work into clear updates for customers or vendors, and documenting steps so non-engineers can follow along. 
 
### Data Structures and Algorithms 
Across courses, I practiced choosing simple, predictable structures—lists, maps/dicts, queues—then measuring when sorting or searching variants actually help. I also learned to weigh clarity vs. performance and to use language-idiomatic tools (e.g., Python’s defaultdict, safe lookups) to keep behavior predictable. 

<!-- =========================================================
=  SECTION 2 — LANGUAGES & TECH I’M FAMILIAR WITH (chips)    =
=  (all tech names live here; no overlap with skills above)  =
========================================================= -->
<section id="tech-familiar" class="tech-simple" aria-labelledby="tech-title">
  <h2 id="tech-title">Languages &amp; Tech I’m Familiar With (All that I can think of, atleast!) </h2>

  <p class="section-intro">
  Grouped for quick scanning.
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
        <li class="chip">Android Studio</li>
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

## Artifacts & Enhancements

In this ePortfolio, you’ll find three enhancements I made to code I had already written in previous courses. When I started planning these updates, I wanted to make sure I was focusing on skills that hiring managers actually care about, while also hitting all of the required course outcomes. To keep the workload realistic for this term, I chose to stick with a single project—the Corner Grocer App—and build on it across all three categories: Software Design & Engineering, Algorithms & Data Structures, and Databases.

### Artifact 1 — Software Design & Engineering (C++ to Python)

I rewrote the original Corner Grocer console app from C++ into Python, keeping the behavior consistent but making the structure much cleaner. The rewrite makes the code easier to maintain and extend. It’s now broken into clear modules, includes full docstrings, and has a much friendlier command-line interface.

#### Skills 
Language translation (C++ → Python), modular organization, separation of concerns, testable function design, and solid in-code documentation.

#### Outcomes 
Collaboration (the structure helps others quickly get up to speed), professional communication (clear code and docstrings), and sound software design.

### Artifact 2 — Algorithms & Data Structures (Sorting + Search)

I added options to sort items alphabetically and by frequency, included a flexible search function, and cleaned up user input handling. These additions make the app feel more usable, like a real interface where users can easily filter or look up what they need.

#### Skills 
Algorithm selection and analysis, utility function creation, defensive programming, and user-focused input validation.

#### Outcomes
Algorithmic thinking, evaluating tradeoffs (clarity vs. performance), and writing maintainable, practical code.

### Artifact 3 — Databases (SQLite Integration)

I swapped out the in-memory tracking system and implemented a full SQLite database, complete with schema planning and a separate database handler for queries. Real-world apps need persistent data. This change made the app more realistic, reliable, and structured around safer data operations.

#### Skills 
SQL schema design, parameterized queries, input validation, exception handling, and separating database logic into its own clean layer.

#### Outcomes
Database design and use, secure coding practices (aligned with OWASP), and application structure geared toward production use.

### How It All Ties Together

I kept everything centered around one project, building it up layer by layer: first with a cleaner foundation (rewriting it in Python), then smarter features (search and sort), and finally real data persistence (SQLite). All three enhancements build on each other to turn a simple console program into something more realistic and production-ready. Together, they show how I’ve grown—not just in what I can build, but in how I think about code structure, usability, and long-term reliability. This is the kind of mindset I will bring to any full-stack or front-end-leaning engineering role.


<section id="skills-demonstrated" class="skills-showcase" aria-labelledby="skills-title">
  <h2 id="skills-title">Skills Demonstrated</h2>

  <p class="section-intro">
    Each chip reflects skill I utilized while implementing my enhancements.
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
      white-space: wrap;
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
=  SECTION 3 — OTHER COURSEWORK PROJECTS (accordions)        =
========================================================= -->
<section id="coursework-projects" class="ocp-accordion" aria-labelledby="ocp-title">
  <h2 id="ocp-title">Additional Projects</h2>

  <p class="section-intro">
    These are other course projects that shaped my skill set:
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
    <details class="ocp-item" open>
      <summary>CS-250 — Software Development Lifecycle</summary>
      <div class="ocp-body">
        <p><strong>Project:</strong> SDLC plan with risk analysis, use cases, and maintenance strategy for a car-rental system. You can view the repo and projects for this course  <a href= "https://github.com/apursley2012/CS250-SDLC-Program">here</a>.
     </p>
        <ul class="ocp-skilllist">
          <li class="chip">SDLC Phases</li>
          <li class="chip">Agile Process</li>
          <li class="chip">Change Management</li>
          <li class="chip">Maintenance Planning</li>
          <li class="chip">UML</li>
        </ul>
      </div>
    </details>
    <details class="ocp-item" open>
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
    <details class="ocp-item" open>
      <summary>CS-360 — Mobile Architecture &amp; Programming</summary>
      <div class="ocp-body">
        <p><strong>Project:</strong> Event-tracking app, which I named PunctuOwlity; built using Android Studio's GUI and emulator, written with Java and SQLite, including full UI design, lifecycle management, and a marketing/monetization plan.</p>
        <ul class="ocp-skilllist">
          <li class="chip">Android Lifecycle</li>
          <li class="chip">UI Design</li>
          <li class="chip">SQLite</li>
          <li class="chip">Intents</li>
          <li class="chip">JSON Parsing</li>
        </ul>
      </div>
    </details>
    <details class="ocp-item" open>
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
    <details class="ocp-item" open>
      <summary>CS-320 — Software Testing, Automation, QA</summary>
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
    <details class="ocp-item" open>
      <summary>CS-201 — Data Structures &amp; Algorithms</summary>
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
    <details class="ocp-item" open>
      <summary>CS-230 — Operating Platforms Systems</summary>
      <div class="ocp-body">
        <p><strong>Project:</strong> “Draw It or Lose It” application design project, demonstrating software architecture decisions, platform considerations, and effective communication of design ideas.You can view the course repo and projects <a href="https://github.com/apursley2012/CS230_Operating_Platforms_Portfolio">here</a>.</p>
        <ul class="ocp-skilllist">
          <li class="chip">Threading</li>
          <li class="chip">Concurrency</li>
          <li class="chip">Scheduling Algorithms</li>
          <li class="chip">System Calls</li>
          <li class="chip">Memory Hierarchy</li>
        </ul>
      </div>
    </details>
    <details class="ocp-item" open>
      <summary>CS-330 — Computer Graphics &amp; Visualization</summary>
      <div class="ocp-body">
        <p><strong>Project:</strong> OpenGL 2D interface with interactive elements. You can view the repo and projects for this course <a href="https://github.com/apursley2012/CS330-Computer-Graphics-Visualization"> here </a>.</p> 
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

<script>
document.addEventListener("DOMContentLoaded", function () {
  const el = document.getElementById("typed-header");
  const text = el.textContent.trim();
  el.textContent = "";
  let i = 0;

  function type() {
    el.textContent = text.slice(0, i++);
    if (i <= text.length) {
      setTimeout(type, 150); // speed (ms per char)
    }
  }

  type();
});
</script>
