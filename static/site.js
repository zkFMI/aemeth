/* æmeth — the only script: the letter demo. Everything else is plain HTML. */
(function () {
  var demo = document.getElementById('letter-demo');
  if (!demo) return;
  var btn = demo.querySelector('button');
  var ae = demo.querySelectorAll('.ae');
  var state = demo.querySelector('.state-text');
  var on = true;
  btn.addEventListener('click', function () {
    on = !on;
    demo.classList.toggle('off', !on);
    for (var i = 0; i < ae.length; i++) ae[i].classList.toggle('erased', !on);
    state.textContent = on ? btn.dataset.on : btn.dataset.off;
    btn.textContent = on ? btn.dataset.erase : btn.dataset.restore;
    btn.setAttribute('aria-pressed', on ? 'false' : 'true');
  });
})();
