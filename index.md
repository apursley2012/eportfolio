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

# About Me
Hello! My name is Alysha Pursley, and I am currently pursuing a degree in Computer Science with a focus on Software Development at Southern New Hampshire University. I have a strong passion for creating engaging, user-friendly interfaces and developing websites and applications that are both functional and visually appealing. My goal is to become a skilled front-end or full-stack developer, where I can bring ideas to life through innovative design and efficient coding. Throughout my studies, I’ve gained valuable experience in various programming languages and development tools, which I am eager to apply in real-world projects. This portfolio reflects my dedication, growth, and the skills I’ve cultivated so far, and I look forward to contributing to exciting tech solutions in the future.

## Capstone & Program Takeaways
I learned how to turn rough ideas into screens that make sense. That means planning the flow first, then building layouts with readable typography, sensible spacing, and color choices that don’t fight the content. I treat accessibility as a basic requirement, not an extra—keyboard paths, focus states, and contrast checks are part of how I work. Responsive behavior and small interaction details (like validation messages and loading hints) matter, because they’re the difference between “it works” and “it feels right.”

I also learned to structure front-end code so it stays easy to change. Breaking features into components, keeping concerns separate, and using clear, consistent names for files, functions, and variables makes the code understandable to someone new. Small, focused commits and straightforward Git/GitHub workflows keep reviews calm and mistakes easy to spot. When something breaks, I lean on targeted logs, step-through debugging, and simple tests for the tricky parts instead of guessing.

Finally, I learned to connect features to real data without surprises. I’m comfortable with basic CRUD, simple schemas, and the patterns that keep data predictable—validation on input, helpful error messages, and parameterized queries when SQL is involved. I make sure the interface always reflects the true state of the data, including loading and failure states, so users aren’t left guessing. That discipline keeps the UI honest and builds trust in what the app is showing.

Completing my capstone truly brought my entire degree together. It challenged me to be precise in every aspect—carefully selecting what to include, organizing my ideas logically, and telling a compelling story. Building the ePortfolio was especially valuable; it sharpened my skills in writing clear instructions, explaining trade-offs, and documenting processes thoroughly. Throughout this project, I reaffirmed my commitment to producing quality work, communicating ideas clearly, and establishing strong foundations for future success. This experience not only demonstrated my technical abilities but also reinforced my dedication to professionalism and continuous improvement in all my endeavors.


<!-- Typed header -->
<h1 id="typed-header">Welcome to my ePortfolio</h1>


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
