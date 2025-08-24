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
   <a href="https://corner-grocer-alyshaspradlin.replit.app">Completed Enhancements Demo</a> |
  </nav>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cascadia+Code:ital,wght@0,200..700;1,200..700&family=Cascadia+Mono:ital,wght@0,200..700;1,200..700&family=DotGothic16&family=Fira+Code:wght@300..700&family=Handjet:wght@100..900&family=Jersey+15&family=Jersey+20&family=Jersey+25&family=Pixelify+Sans:wght@400..700&family=Press+Start+2P&family=Share+Tech&family=Share+Tech+Mono&family=Silkscreen:wght@400;700&family=VT323&display=swap" rel="stylesheet">

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
