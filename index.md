---
layout: default
title: Home
---

<!-- Simple nav -->
<nav style="margin-bottom: 20px;">
  <a href="./index.html">Home</a> |
  <a href="./enhancement-2.html">Enhancement 2</a> |
  <a href="./enhancement-3.html">Enhancement 3</a> |
  <a href="./contact.html">Contact</a>
</nav>

<!-- Typed header -->
<h1 id="typed-header">Welcome to my ePortfolio</h1>

<p>This site is built with the Hacker theme. The header above types out once when the page loads.</p>

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
