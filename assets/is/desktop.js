<script>
function openDoc(url) {
  const win = document.getElementById('documents-window');
  const frame = document.getElementById('doc-frame');
  if (win) win.style.display = 'block';
  if (frame) frame.src = url;
}

function openIE(url) {
  const win = document.getElementById('ie-window');
  const frame = document.getElementById('ie-frame');
  if (win) win.style.display = 'block';
  if (frame) frame.src = url;
}
</script>
