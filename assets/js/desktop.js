<script>

function openDoc(url) {
  const win = document.getElementById('documents-window');
  const frame = document.getElementById('doc-frame');
  if (win) win.style.display = 'block';
  if (frame) frame.src = url;
}

/* ===== Win98 portfolio glue (typed title + bold/italic in Notepad) ===== */
(function () {
  // ---- Helpers ----------------------------------------------------------
  function bringToFront(openInputId, onTopInputId) {
    const open = document.getElementById(openInputId);
    const onTop = document.getElementById(onTopInputId);
    if (open) open.checked = true;
    if (onTop) onTop.checked = true;
  }

  function escapeHTML(s) {
    return s
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  // Minimal markdown: **bold**, *italic* or _italic_
  function parseLiteMD(txt) {
    // escape first, then re-insert allowed tags
    let html = escapeHTML(txt);

    // bold: **text**
    html = html.replace(/\*\*(.+?)\*\*/g, "<b>$1</b>");
    // italic: *text* or _text_
    html = html.replace(/(^|[^*])\*(?!\s)(.+?)(?!\s)\*(?!\*)/g, '$1<i>$2</i>');
    html = html.replace(/(^|[^_])_(?!\s)(.+?)(?!\s)_(?!_)/g, '$1<i>$2</i>');

    return html;
  }

  function typeTitleThenShowRest(container, fullText, charDelay) {
    const lines = fullText.split(/\r?\n/);

    // find first non-empty (visible) line
    let idx = lines.findIndex(l => l.trim().length > 0);
    if (idx < 0) { container.innerHTML = parseLiteMD(fullText); return; }

    const before = lines.slice(0, idx).join("\n");
    const title = lines[idx];
    const after = lines.slice(idx + 1).join("\n");

    // show any blank lines before the title (escaped)
    container.innerHTML = parseLiteMD(before + (before ? "\n" : ""));

    // type the title as plain text first
    let i = 0;
    (function type() {
      if (i <= title.length) {
        container.innerHTML = parseLiteMD(before + (before ? "\n" : "")) + escapeHTML(title.slice(0, i));
        container.scrollTop = container.scrollHeight;
        i++;
        setTimeout(type, charDelay);
      } else {
        // when done typing, re-render the title with formatting and append the rest (formatted)
        const fullHTML =
          parseLiteMD(before + (before ? "\n" : "")) +
          parseLiteMD(title) + "\n\n" +
          parseLiteMD(after);
        container.innerHTML = fullHTML;
        container.scrollTop = 0;
      }
    })();
  }

  // ---- Actions ----------------------------------------------------------
  function openNotepad(path, typedTitle) {
    const np = document.getElementById('npText');
    if (!np) return;

    // show Notepad window (update these IDs to match your dist index.html)
    bringToFront('windows-notepad-input', 'windows-notepad-input-on-top');

    fetch(path)
      .then(r => r.text())
      .then(text => {
        if (typedTitle) {
          np.innerHTML = ""; // clear and type first line
          typeTitleThenShowRest(np, text, 14);
        } else {
          np.innerHTML = parseLiteMD(text);
          np.scrollTop = 0;
        }
      })
      .catch(err => alert('Could not load: ' + path + '\n' + err));
  }

  function openIE(url) {
    const frame = document.querySelector('.window.ie iframe');
    if (frame) frame.src = url || 'about:blank';
    bringToFront('windows-ie-input', 'windows-ie-input-on-top');
  }

  // ---- Event delegation for all links -------------------------------
  document.addEventListener('click', function (e) {
    const a = e.target.closest('a[data-open]');
    if (!a) return;

    const action = a.dataset.open;
    if (action === 'notepad') {
      e.preventDefault();
      const typed = a.dataset.typedTitle === '1' ||
                    /\/narratives\//.test(a.getAttribute('href') || '');
      openNotepad(a.getAttribute('href'), typed);
    } else if (action === 'ie') {
      e.preventDefault();
      openIE(a.dataset.url || a.getAttribute('href'));
    }
  });

  // ---- Typed welcome on first load (optional file) ------------------
  // Change/remove this if you don't want the desktop to boot into Notepad
  const WELCOME = 'content/welcome.txt';
  fetch(WELCOME).then(r => r.text()).then(text => {
    const np = document.getElementById('npText');
    if (!np) return;
    bringToFront('windows-notepad-input', 'windows-notepad-input-on-top');

    // type entire welcome
    let i = 0;
    (function typeAll() {
      if (i <= text.length) {
        // For welcome we keep it plain while typing; then format once at end
        np.innerHTML = escapeHTML(text.slice(0, i));
        np.scrollTop = np.scrollHeight;
        i++;
        setTimeout(typeAll, 12);
      } else {
        np.innerHTML = parseLiteMD(text);
        np.scrollTop = 0;
      }
    })();
  }).catch(() => { /* no welcome file, ignore */ });
})();
</script>
