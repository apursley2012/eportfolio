<script>
(function () {
  async function loadInclude(el) {
    const src = el.getAttribute('data-include');
    if (!src) return;
    try {
      const res = await fetch(src, { cache: 'no-cache' });
      if (!res.ok) throw new Error(res.status + ' ' + src);
      el.innerHTML = await res.text();
    } catch (e) {
      el.innerHTML = '<!-- include failed: ' + e.message + ' -->';
    }
  }
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-include]').forEach(loadInclude);
  });
})();
</script>
