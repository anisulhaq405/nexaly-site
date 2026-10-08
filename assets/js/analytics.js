/* Website analytics only; never read worksheet values or offline app records. */
(function () {
  'use strict';
  if (!/^https?:$/.test(location.protocol) || !/^(www\.)?nexalyplanner\.com$/.test(location.hostname) || /^\/(demos|downloads)\//.test(location.pathname)) return;
  var id = 'G-NPE1Y88BDG', key = 'nexaly-analytics-consent-v1', started = false, allowed = false;
  var choice; try { choice = localStorage.getItem(key); } catch (_) {}
  function start() {
    allowed = true; window['ga-disable-' + id] = false;
    if (started) return; started = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', id, {send_page_view: false, page_location: location.origin + location.pathname, page_referrer: '', allow_google_signals: false, allow_ad_personalization_signals: false});
    window.gtag('event', 'page_view', {page_location: location.origin + location.pathname, page_referrer: '', page_title: document.title});
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
  var panel = document.createElement('section'); panel.setAttribute('aria-label', 'Analytics preferences');
  panel.style.cssText = 'position:fixed;bottom:52px;left:16px;right:16px;max-width:560px;z-index:10001;background:#fff;color:#15283b;padding:16px;border:1px solid #cbd5e1;border-radius:12px;box-shadow:0 8px 30px #0002;font:14px/1.5 system-ui';
  panel.innerHTML = '<p style="margin:0 0 12px">Allow optional Google Analytics cookies to help us understand website visits and planner button use? Planner entries are never sent. <a href="/privacy/">Privacy policy</a></p><button type="button" data-choice="accepted">Allow analytics</button> <button type="button" data-choice="rejected">Decline</button>';
  panel.querySelectorAll('button').forEach(function (button) { button.style.cssText = 'padding:9px 14px;border:1px solid #64748b;border-radius:7px;background:#f8fafc;color:#15283b;cursor:pointer'; button.addEventListener('click', function () { save(button.dataset.choice); }); });
  panel.hidden = choice === 'accepted' || choice === 'rejected'; document.body.appendChild(panel);
  var settings = document.createElement('button'); settings.type = 'button'; settings.textContent = 'Analytics settings';
  settings.style.cssText = 'position:fixed;bottom:12px;left:16px;z-index:10000;padding:7px 10px;border:1px solid #cbd5e1;border-radius:7px;background:#fff;color:#15283b;font:12px system-ui;cursor:pointer';
  settings.addEventListener('click', function () { panel.hidden = !panel.hidden; }); document.body.appendChild(settings);
  if (choice === 'accepted') start();
  var actions = {'tool-calculate':'calculate_click','tool-csv':'csv_click','tool-json':'backup_click','tool-print':'print_click','tool-sample':'sample_click','calculate':'calculate_click','csv':'csv_click','json':'backup_click','print':'print_click','sample':'sample_click'};
  document.addEventListener('click', function (event) {
    if (!allowed || !started) return;
    var button = event.target.closest('button');
    var match = location.pathname.match(/^\/tools\/([a-z0-9-]+)\/$/);
    if (match && button && actions[button.id]) window.gtag('event', 'planner_action', {planner_id: match[1], planner_action: actions[button.id], page_location: location.origin + location.pathname, page_referrer: ''});
  });
}());
