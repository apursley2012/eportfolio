<script>
// Simple Win98 desktop behavior (drag, z-index, open/close, start menu, clock)
(function () {
  const windows = [...document.querySelectorAll('.window')];
  const taskButtons = document.getElementById('taskButtons');
  const startBtn = document.getElementById('startBtn');
  const startMenu = document.getElementById('start-menu');
  const closeStartMenuBtn = document.getElementById('closeStartMenu');

  // z-index stack
  let z = 10;
  function bringToFront(win) {
    z += 1; win.style.zIndex = String(z);
  }

  // Task button mapping
  const winToTaskBtn = new Map();

  function ensureTaskButton(winId, title) {
    if (winToTaskBtn.has(winId)) return;
    const btn = document.createElement('button');
    btn.className = 'button task-button';
    btn.textContent = title || winId;
    btn.addEventListener('click', () => toggleWin(winId));
    taskButtons.appendChild(btn);
    winToTaskBtn.set(winId, btn);
  }

  function setTaskButtonActive(winId, active) {
    const btn = winToTaskBtn.get(winId);
    if (!btn) return;
    btn.classList.toggle('active', !!active);
  }

  function openWin(winId) {
    const win = document.getElementById(winId);
    if (!win) return;
    win.classList.add('active');
    bringToFront(win);
    setTaskButtonActive(winId, true);
    // Create task button lazily
    const title = win.querySelector('.title-bar-text')?.textContent || winId;
    ensureTaskButton(winId, title);
    closeStartMenu();
  }
  window.openWin = openWin;

  function closeWin(winId) {
    const win = document.getElementById(winId);
    if (!win) return;
    win.classList.remove('active');
    win.classList.remove('maximized');
    setTaskButtonActive(winId, false);
  }

  function minimizeWin(winId) {
    const win = document.getElementById(winId);
    if (!win) return;
    win.classList.remove('maximized');
    win.classList.remove('active'); // hide
    setTaskButtonActive(winId, false);
  }

  function toggleWin(winId) {
    const win = document.getElementById(winId);
    if (!win) return;
    if (win.classList.contains('active')) {
      minimizeWin(winId);
    } else {
      openWin(winId);
    }
  }

  function maximizeWin(winId) {
    const win = document.getElementById(winId);
    if (!win) return;
    if (win.classList.contains('maximized')) {
      win.classList.remove('maximized');
    } else {
      win.classList.add('maximized');
      bringToFront(win);
    }
    setTaskButtonActive(winId, true);
  }

  // Wire titlebar controls
  windows.forEach(win => {
    const id = win.id;
    const title = win.querySelector('.title-bar-text')?.textContent || id;
    ensureTaskButton(id, title);

    win.querySelectorAll('[data-close]').forEach(b => b.addEventListener('click', () => closeWin(id)));
    win.querySelectorAll('[data-minimize]').forEach(b => b.addEventListener('click', () => minimizeWin(id)));
    win.querySelectorAll('[data-maximize]').forEach(b => b.addEventListener('click', () => maximizeWin(id)));

    win.addEventListener('mousedown', () => bringToFront(win));
  });

  // Drag move windows by title-bar
  let drag = null;
  document.addEventListener('mousedown', (e) => {
    const bar = e.target.closest('.title-bar');
    const win = e.target.closest('.window');
    if (!bar || !win) return;
    if (win.classList.contains('maximized')) return; // don't drag maximized
    bringToFront(win);
    const rect = win.getBoundingClientRect();
    drag = {
      win,
      offsetX: e.clientX - rect.left,
      offsetY: e.clientY - rect.top
    };
    e.preventDefault();
  });
  document.addEventListener('mousemove', (e) => {
    if (!drag) return;
    const x = Math.max(0, Math.min(window.innerWidth - 80, e.clientX - drag.offsetX));
    const y = Math.max(0, Math.min(window.innerHeight - 80, e.clientY - drag.offsetY));
    drag.win.style.left = x + 'px';
    drag.win.style.top = y + 'px';
  });
  document.addEventListener('mouseup', () => { drag = null; });

  // Desktop icons (double-click)
  document.querySelectorAll('.desktop-icon').forEach(icon => {
    let clicks = 0, timer = null;
    const id = icon.getAttribute('data-open');
    icon.addEventListener('click', () => {
      clicks += 1;
      if (clicks === 1) {
        timer = setTimeout(() => { clicks = 0; }, 300);
      } else {
        clearTimeout(timer);
        clicks = 0;
        openWin(id);
      }
    });
  });

  // Start menu
  function toggleStart() { startMenu.classList.toggle('active'); }
  function closeStartMenu() { startMenu.classList.remove('active'); }
  startBtn.addEventListener('click', toggleStart);
  closeStartMenuBtn.addEventListener('click', closeStartMenu);
  document.addEventListener('click', (e) => {
    if (e.target.closest('#start-menu') || e.target.closest('#startBtn')) return;
    closeStartMenu();
  });

  // Clock
  function pad(n){return String(n).padStart(2,'0');}
  function tickClock(){
    const d=new Date();
    document.getElementById('clock').textContent = `${pad(d.getHours())}:${pad(d.getMinutes())}`;
  }
  tickClock(); setInterval(tickClock, 10_000);

  // Public helpers to route content:
  window.openDoc = function(path) {
    openWin('win-docs');
    const frame = document.getElementById('documents-frame');
    if (frame) frame.src = path;
  };

  // IMPORTANT: Always load the IE wrapper so *everything* stays inside the desktop
  window.openIE = function(url) {
    openWin('win-ie');
    const frame = document.getElementById('ie-frame');
    if (frame) frame.src = 'content/ie-wrapper.html?url=' + encodeURIComponent(url);
  };

  // Load self-assessment into Notepad
  fetch('content/self-assessment.txt', { cache: 'no-cache' })
    .then(r => r.text())
    .then(t => { const ta=document.getElementById('notepad-text'); if(ta) ta.value=t; })
    .catch(()=>{ /* leave blank if missing */ });

  // On first load, focus Help & Documents
  openWin('win-help');
  openWin('win-docs');

})();
</script>
