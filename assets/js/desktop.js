/* assets/js/desktop.js
   Hooks into the existing Windows 98 demo from your dist/index.html
   - Opens Notepad with rich text (bold/italic) loaded from /content/*.html
   - Opens Internet Explorer window and sets its iframe URL for GitHub links
   - Types the Notepad window title (and first H1 inside the doc) on load
   - Respects the demo’s checkbox IDs already present in the dist markup:
       #windows-notepad-input, #windows-notepad-input-on-top
       #windows-ie-input,     #windows-ie-input-on-top
*/

(function () {
  // --- Cached handles (filled on DOM ready) ---
  let notepadOnInput, notepadTopInput, notepadWindow, notepadTitleEl, notepadContentHost;
  let ieOnInput, ieTopInput, ieWindow, ieIframe, ieTitleEl;

  // Small helper: bring a pair of ON/TOP checkboxes to the front
  function bringToFront(onInput, topInput) {
    if (onInput) onInput.checked = true;
    if (topInput) topInput.checked = true;
  }

  // Replace Notepad's <textarea> once with a HTML-capable pane
  function ensureNotepadHtmlPane() {
    if (!notepadWindow) return;
    const content = notepadWindow.querySelector('.content');
    if (!content) return;

    // If we've already converted it, bail
    if (content.querySelector('.notepad-body')) {
      notepadContentHost = content.querySelector('.notepad-body');
      return;
    }

    // Remove existing <textarea> (demo default)
    const ta = content.querySelector('textarea');
    if (ta) ta.remove();

    // Insert our HTML-capable area (styled to look like Notepad)
    const host = document.createElement('div');
    host.className = 'notepad-body';
    host.setAttribute('role', 'document');
    content.appendChild(host);
    notepadContentHost = host;
  }

  // Typed effect for a single element’s text
  function typeText(el, text, speed) {
    if (!el) return;
    el.textContent = '';
    let i = 0;
    (function tick() {
      if (i < text.length) {
        el.textContent += text.charAt(i++);
        setTimeout(tick, speed);
      }
    })();
  }

  // Optional: also type the first H1 in the loaded doc
  function typeFirstHeadingInNotepad(speed) {
    if (!notepadContentHost) return;
    const h1 = notepadContentHost.querySelector('h1');
    if (!h1) return;
    const original = h1.textContent.trim();
    typeText(h1, original, speed);
  }

  // Load an external HTML fragment into Notepad (keeps formatting)
  function loadIntoNotepad(path, windowTitle, { typeTitle = true, typeSpeed = 20 } = {}) {
    ensureNotepadHtmlPane();
    if (!notepadContentHost) return;

    fetch(path, { cache: 'no-cache' })
      .then(resp => resp.text())
      .then(html => {
        notepadContentHost.innerHTML = html;

        if (notepadTitleEl && windowTitle) {
          if (typeTitle) {
            typeText(notepadTitleEl, windowTitle, typeSpeed);
          } else {
            notepadTitleEl.textContent = windowTitle;
          }
        }
        // Optional type animation for first H1 in doc
        typeFirstHeadingInNotepad(typeSpeed);
      })
      .catch(err => {
        if (notepadContentHost) {
          notepadContentHost.innerHTML =
            '<p><strong>Error loading document.</strong></p><p>' +
            (err && err.message ? err.message : 'Unknown error') + '</p>';
        }
        if (notepadTitleEl && windowTitle) notepadTitleEl.textContent = windowTitle;
      });
  }

  // Public: open a narrative in Notepad
  window.openNarrative = function (path, title) {
    bringToFront(notepadOnInput, notepadTopInput);
    loadIntoNotepad(path, title, { typeTitle: true, typeSpeed: 16 });
  };

  // Public: open a URL in Internet Explorer window (inside desktop)
  window.openInIE = function (url, title) {
    if (!ieIframe) return;
    bringToFront(ieOnInput, ieTopInput);
    ieIframe.setAttribute('src', url || 'about:blank');
    if (ieTitleEl && title) ieTitleEl.textContent = title;
  };

  // OPTIONAL: auto-load the welcome doc on first paint
  function autoLoadWelcome() {
    if (!notepadOnInput || !notepadTopInput) return;
    bringToFront(notepadOnInput, notepadTopInput);
    loadIntoNotepad('content/welcome.html', 'Welcome — Read Me First', { typeTitle: true, typeSpeed: 20 });
  }

  // DOM ready: wire everything
  document.addEventListener('DOMContentLoaded', function () {
    // Notepad
    notepadOnInput  = document.getElementById('windows-notepad-input');
    notepadTopInput = document.getElementById('windows-notepad-input-on-top');
    notepadWindow   = document.querySelector('.window.notepad');
    notepadTitleEl  = notepadWindow ? notepadWindow.querySelector('.title-bar-text') : null;

    // Internet Explorer
    ieOnInput  = document.getElementById('windows-ie-input');
    ieTopInput = document.getElementById('windows-ie-input-on-top');
    ieWindow   = document.querySelector('.window.ie');
    ieTitleEl  = ieWindow ? ieWindow.querySelector('.title-bar-text') : null;
    ieIframe   = ieWindow ? ieWindow.querySelector('.content iframe') : null;

    // Make the whole Notepad content HTML-capable
    ensureNotepadHtmlPane();

    // If you want the desktop to open with instructions, enable this:
    autoLoadWelcome();

    // Example wiring (use these in your Start menu or desktop shortcuts):
    // <a href="#" onclick="openNarrative('content/enhancement1.html','Software Design & Engineering'); return false;">Enhancement 1</a>
    // <a href="#" onclick="openInIE('https://github.com/USER/REPO/path','Corner Grocer — GitHub'); return false;">View Code</a>
  });
})();
