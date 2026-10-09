#!/usr/bin/env python3
import os

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("ministries.html", "Ministries"),
    ("sermons.html", "Sermons"),
    ("events.html", "Events"),
    ("give.html", "Give"),
    ("contact.html", "Contact"),
]

def header(active):
    links = []
    mlinks = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active else ''
        links.append(f'<a href="{href}"{cls}>{label}</a>')
        mlinks.append(f'<a href="{href}"{cls}>{label}</a>')
    nav = "\n        ".join(links)
    mnav = "\n        ".join(mlinks)
    return f"""<div class="preview-bar">🚧 <strong>Preview site</strong> — placeholder text &amp; photos, awaiting your answers to the requirements questionnaire.</div>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="index.html">
      <img src="assets/logo.png" alt="Bridge To Heaven Ministries logo">
      <span class="brand-name">Bridge To Heaven<span>Ministries</span></span>
    </a>
    <nav class="main-nav">
        {nav}
    </nav>
    <a href="contact.html" class="btn btn-primary desktop-only">Plan Your Visit</a>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" onclick="var m=document.getElementById('mobileNav');var open=m.classList.toggle('open');this.setAttribute('aria-expanded',open);this.innerHTML=open?'&amp;#10005;':'&amp;#9776;';">&#9776;</button>
  </div>
  <div class="mobile-nav" id="mobileNav">
        {mnav}
    <a href="contact.html" class="btn btn-primary" style="text-align:center;margin-top:6px;">Plan Your Visit</a>
  </div>
</header>
"""

def footer():
    return """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">
          <img src="assets/logo.png" alt="Bridge To Heaven Ministries logo">
          <span>Bridge To Heaven Ministries</span>
        </div>
        <p>164 E Church St<br>Bergenfield, NJ 07621</p>
        <div class="social-row">
          <a href="https://www.instagram.com/bthministry/" target="_blank" rel="noopener" aria-label="Instagram">IG</a>
        </div>
      </div>
      <div>
        <h4>Quick Links</h4>
        <p><a href="about.html">About Us</a></p>
        <p><a href="ministries.html">Ministries</a></p>
        <p><a href="sermons.html">Sermons</a></p>
        <p><a href="events.html">Events</a></p>
        <p><a href="give.html">Give</a></p>
        <p><a href="contact.html">Contact</a></p>
      </div>
      <div>
        <h4>Service Times</h4>
        <p>Sunday Worship — <em>time to be confirmed</em></p>
        <p>Bible Study / Midweek — <em>to be confirmed</em></p>
        <p><a href="mailto:info@bridgetoheavenministries.org">info@bridgetoheavenministries.org</a></p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Bridge To Heaven Ministries. All rights reserved.</span>
      <span>Site built as a volunteer project — provided at no cost.</span>
    </div>
  </div>
</footer>
"""

def page(title, description, active, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Bridge To Heaven Ministries</title>
<meta name="description" content="{description}">
<link rel="icon" href="assets/logo.png">
<link rel="stylesheet" href="styles.css">
</head>
<body>
{header(active)}
{body}
{footer()}
</body>
</html>
"""

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

def write(name, html):
    with open(os.path.join(OUT_DIR, name), 'w') as f:
        f.write(html)
    print("wrote", name)
