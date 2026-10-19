(function () {
  'use strict';
  const app = document.querySelector('main.free-tools');
  if (!app) return;
  function enhanceTables(scope) {
    for (const wrap of scope.querySelectorAll('.table-wrap')) {
      if (!wrap.querySelector('table')) continue;
      wrap.tabIndex = 0;
      wrap.setAttribute('role', 'region');
      if (!wrap.getAttribute('aria-label')) {
        const table = wrap.querySelector('table');
        const previous = wrap.previousElementSibling;
        const heading = previous && /^H[1-6]$/.test(previous.tagName) ? previous.textContent : '';
        const label = table.caption?.textContent || heading || 'Planner table';
        wrap.setAttribute('aria-label', label.trim() + ' - scroll horizontally for more columns');
      }
    }
  }
  enhanceTables(app);
  const results = document.getElementById('tool-results') || document.getElementById('results');
  if (results) new MutationObserver(() => enhanceTables(results)).observe(results, {childList: true});
})();
