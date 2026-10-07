/* Progressive enhancement of the homepage's existing, crawlable planner links. */
(() => {
  'use strict';
  const section = document.querySelector('.home-free');
  if (!section) return;
  const browser = section.querySelector('.planner-browser');
  const search = section.querySelector('input[type="search"]');
  const buttons = [...section.querySelectorAll('[data-filter]')];
  const cards = [...section.querySelectorAll('.home-free-card')];
  const status = section.querySelector('.planner-result-count');
  const empty = section.querySelector('.planner-empty');
  let category = 'featured';
  const render = () => {
    const query = search.value.trim().toLocaleLowerCase();
    let count = 0;
    cards.forEach(card => {
      const inCategory = category === 'featured' ? (query || card.dataset.featured === 'true') : card.dataset.category === category;
      const matches = Boolean(inCategory) && card.textContent.toLocaleLowerCase().includes(query);
      card.hidden = !matches;
      if (matches) count++;
    });
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === category)));
    status.textContent = query ? `${count} matching planner${count === 1 ? '' : 's'}` : category === 'featured' ? `${count} planners to get you started` : `${count} planner${count === 1 ? '' : 's'} in this category`;
    empty.hidden = count !== 0;
  };
  buttons.forEach(button => button.addEventListener('click', () => { category = button.dataset.filter; render(); }));
  search.addEventListener('input', render);
  section.querySelector('.planner-reset').addEventListener('click', () => { category = 'featured'; search.value = ''; render(); search.focus(); });
  render();
  browser.hidden = false;
})();
