/* Website analytics only; never read worksheet values or offline app records. */
(function () {
  'use strict';
  if (!/^https?:$/.test(location.protocol) || !/^(www\.)?nexalyplanner\.com$/.test(location.hostname) || /^\/(demos|downloads)\//.test(location.pathname)) return;
  var id = 'G-NPE1Y88BDG', key = 'nexaly-analytics-consent-v1', started = false, allowed = false;
  var choice; try { choice = localStorage.getItem(key); } catch (_) {}
  // Retain referring domains without collecting private URL paths or query strings.
  var referrer = '';
  try { var referring = new URL(document.referrer); if (/^https?:$/.test(referring.protocol)) referrer = referring.origin + '/'; } catch (_) {}
  function start() {
    allowed = true; window['ga-disable-' + id] = false;
    if (started) return; started = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', id, {send_page_view: false, page_location: location.origin + location.pathname, page_referrer: referrer, allow_google_signals: false, allow_ad_personalization_signals: false});
    window.gtag('event', 'page_view', {page_location: location.origin + location.pathname, page_referrer: referrer, page_title: document.title});
    var script = document.createElement('script'); script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + id; document.head.appendChild(script);
  }
  function save(value) {
    try { localStorage.setItem(key, value); } catch (_) {}
    choice = value; panel.hidden = true;
    if (value === 'accepted') start();
    else {
      allowed = false; window['ga-disable-' + id] = true;
      document.cookie.split(';').forEach(function (entry) {
        var name = entry.split('=')[0].trim(); if (!/^_ga(?:_|$)/.test(name)) return;
        ['', '; domain=nexalyplanner.com', '; domain=.nexalyplanner.com', '; domain=' + location.hostname].forEach(function (domain) { document.cookie = name + '=; Max-Age=0; path=/' + domain; });
      });
    }
  }
  // The homepage supplies first-render markup; other pages retain the same fallback.
  var existingPanel = document.getElementById('nexaly-analytics-panel');
  var panel = existingPanel || document.createElement('section'); panel.setAttribute('aria-label', 'Analytics preferences');
  if (!existingPanel) panel.style.cssText = 'position:fixed;bottom:52px;left:16px;right:16px;max-width:560px;z-index:10001;background:#fff;color:#15283b;padding:16px;border:1px solid #cbd5e1;border-radius:12px;box-shadow:0 8px 30px #0002;font:14px/1.5 system-ui';
  if (!existingPanel) panel.innerHTML = '<p style="margin:0 0 12px">Allow optional Google Analytics cookies to help us understand website visits, template downloads and planner link/button use? Planner entries are never sent. <a href="/privacy/">Privacy policy</a></p><button type="button" data-choice="accepted">Allow analytics</button> <button type="button" data-choice="rejected">Decline</button>';
  panel.querySelectorAll('button').forEach(function (button) { if (!existingPanel) button.style.cssText = 'padding:9px 14px;border:1px solid #64748b;border-radius:7px;background:#f8fafc;color:#15283b;cursor:pointer'; button.addEventListener('click', function () { save(button.dataset.choice); }); button.disabled = false; });
  panel.hidden = choice === 'accepted' || choice === 'rejected'; if (!panel.parentNode) document.body.appendChild(panel);
  var settings = document.createElement('button'); settings.type = 'button'; settings.textContent = 'Analytics settings';
  settings.style.cssText = 'position:fixed;bottom:12px;left:16px;z-index:10000;padding:7px 10px;border:1px solid #cbd5e1;border-radius:7px;background:#fff;color:#15283b;font:12px system-ui;cursor:pointer';
  settings.addEventListener('click', function () { panel.hidden = !panel.hidden; }); document.body.appendChild(settings);
  if (choice === 'accepted') start();
  var actions = {'tool-calculate':'calculate_click','tool-csv':'csv_click','tool-json':'backup_click','tool-print':'print_click','tool-sample':'sample_click','calculate':'calculate_click','csv':'csv_click','json':'backup_click','print':'print_click','sample':'sample_click'};
  document.addEventListener('click', function (event) {
    if (!allowed || !started) return;
    if (!event.target || typeof event.target.closest !== 'function') return;
    var anchor = event.target.closest('a[href]');
    if (anchor) {
      var url; try { url = new URL(anchor.href, location.origin); } catch (_) { return; }
      var sheetResources = {'1rxi5554h8Wfc3Vd66TY9_ZXuiTZZ3KBO8Lvcb_24bqM':'assignment-tracker-template','1XllAhmk7sDGlajM7xfy3xUhqeoF0X4-0SYIVk4L4d1Y':'13-week-cash-flow-forecast-template','1JaEvb77fWoaBfUc9_0Lo1L4kR9Tp-iP1znyYHaYqQrA':'purchase-order-tracker-template'};
      var sheetLink = url.pathname.match(/^\/spreadsheets\/d\/([A-Za-z0-9_-]+)\/copy$/);
      if (url.origin === 'https://docs.google.com' && sheetLink && sheetResources[sheetLink[1]]) window.gtag('event', 'template_open', {resource_id: sheetResources[sheetLink[1]], file_extension: 'google_sheets', page_location: location.origin + location.pathname, page_referrer: ''});
      if (url.origin === location.origin) {
        var resource = url.pathname.match(/^\/assets\/downloads\/([a-z0-9][a-z0-9-]*)\.(xlsx|pdf|html|txt|csv)$/i);
        if (resource) window.gtag('event', resource[2] === 'html' ? 'template_open' : 'template_download', {resource_id: resource[1], file_extension: resource[2], page_location: location.origin + location.pathname, page_referrer: ''});
        var product = url.pathname.match(/^\/planners\/([a-z0-9-]+)\/$/);
        // Count the same product-intent event from both editorial guides and free worksheets.\n        if (/^\/(?:journal|tools)\/[a-z0-9-]+\/$/.test(location.pathname) && product && !/^(digital-planners|business-operating-systems)$/.test(product[1])) window.gtag('event', 'product_click', {product_id: product[1], page_location: location.origin + location.pathname, page_referrer: ''});
        var demo = url.pathname.match(/^\/demos\/([a-z0-9-]+)\/(?:index\.html)?$/);
        if (demo) window.gtag('event', 'demo_open', {product_id: demo[1], page_location: location.origin + location.pathname});
      }
      // A checkout click is intent only; it is never a purchase event.
      if (url.origin === 'https://buy.polar.sh' && /^\/polar_cl_[A-Za-z0-9_]+$/.test(url.pathname)) window.gtag('event', 'checkout_click', {page_location: location.origin + location.pathname});
    }
    var button = event.target.closest('button');
    if (button && button.getAttribute && button.getAttribute('onclick') === 'buyProduct()' && window.products && window.products[window.curP] && window.products[window.curP].buyUrl) window.gtag('event', 'checkout_click', {page_location: location.origin + location.pathname});
    var match = location.pathname.match(/^\/tools\/([a-z0-9-]+)\/$/);
    if (match && button && actions[button.id]) window.gtag('event', 'planner_action', {planner_id: match[1], planner_action: actions[button.id], page_location: location.origin + location.pathname, page_referrer: ''});
  });
}());
