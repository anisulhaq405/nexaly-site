(() => {
  const buckets = ['Current', '1–30 days', '31–60 days', '61–90 days', '91+ days'];
  const day = 86400000;
  const fields = [
    ['Customer', 'text'], ['Invoice', 'text'], ['Due date', 'date'], ['Open balance', 'number']
  ];
  const get = (name) => document.getElementById('aging-' + name);
  const rows = get('rows');
  const results = get('results');
  const asOf = get('date');
  const status = get('status');
  const print = get('print');
  const money = new Intl.NumberFormat(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });

  function invalidate() {
    results.replaceChildren();
    print.disabled = true;
    status.textContent = 'Select Calculate report to review the current inputs.';
  }

  function addInvoice(values = []) {
    const row = rows.insertRow();
    fields.forEach(([label, type], index) => {
      const input = document.createElement('input');
      input.type = type;
      input.required = true;
      input.setAttribute('aria-label', label);
      input.value = values[index] ?? '';
      if (type === 'number') {
        input.step = '0.01';
        input.min = '0';
        input.max = '999999999.99';
      }
      row.insertCell().append(input);
    });
    const remove = document.createElement('button');
    remove.type = 'button';
    remove.textContent = 'Remove';
    remove.addEventListener('click', () => {
      row.remove();
      invalidate();
    });
    row.insertCell().append(remove);
    invalidate();
  }

  get('add').addEventListener('click', () => {
    addInvoice();
    rows.lastElementChild.querySelector('input').focus();
  });
  get('example').addEventListener('click', () => {
    asOf.value = '2026-11-27';
    rows.replaceChildren();
    [
      ['North', 'N-100', '2026-11-27', 600],
      ['East', 'E-101', '2026-10-28', 750],
      ['East', 'E-102', '2026-10-27', 400],
      ['West', 'W-103', '2026-08-28', 250],
      ['South', 'S-104', '2026-09-27', 210]
    ].forEach(addInvoice);
    get('form').requestSubmit();
  });
  get('form').addEventListener('input', invalidate);
  get('form').addEventListener('submit', (event) => {
    event.preventDefault();
    invalidate();
    if (!rows.rows.length) {
      status.textContent = 'Add at least one invoice.';
      return;
    }
    const customers = new Map();
    const totals = buckets.map(() => 0);
    for (const row of rows.rows) {
      const [customer, invoice, due, balance] = row.querySelectorAll('input');
      const name = customer.value.trim();
      if (!name || !invoice.value.trim()) {
        status.textContent = 'Enter a customer and invoice reference on each row.';
        (!name ? customer : invoice).focus();
        return;
      }
      const amount = Math.round(balance.valueAsNumber * 100);
      if (!amount) continue;
      const late = Math.floor((asOf.valueAsNumber - due.valueAsNumber) / day);
      const bucket = Math.min(4, Math.max(0, Math.ceil(late / 30)));
      if (!customers.has(name)) customers.set(name, buckets.map(() => 0));
      customers.get(name)[bucket] += amount;
      totals[bucket] += amount;
    }
    const table = document.createElement('table');
    const header = table.createTHead().insertRow();
    for (const label of ['Customer', ...buckets, 'Total open']) {
      const cell = document.createElement('th');
      cell.scope = 'col';
      cell.textContent = label;
      header.append(cell);
    }
    const tbody = table.createTBody();
    for (const [name, amounts] of [...customers, ['Total', totals]]) {
      const row = tbody.insertRow();
      row.insertCell().textContent = name;
      for (const amount of [...amounts, amounts.reduce((sum, x) => sum + x, 0)]) {
        row.insertCell().textContent = money.format(amount / 100);
      }
    }
    results.append(table);
    status.textContent = 'Open balances as of ' + asOf.value + ' · ' + customers.size + ' customer accounts';
    print.disabled = false;
  });
  print.addEventListener('click', () => window.print());
  asOf.valueAsDate = new Date(Date.now() - new Date().getTimezoneOffset() * 60000);
  addInvoice();
})();
