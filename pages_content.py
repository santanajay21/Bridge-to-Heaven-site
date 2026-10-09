#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_site import page, write

# ---------------- HOME ----------------
home_body = """
<section class="hero">
  <div class="container hero-inner">
    <span class="kicker">Welcome Home</span>
    <h1>A place to belong, right here in Bergenfield.</h1>
    <p class="lead">Bridge To Heaven Ministries is a community of faith devoted to worship, discipleship, and reaching our neighbors with hope. Whoever you are, wherever you're coming from — there's a seat for you.</p>
    <div class="hero-actions">
      <a href="contact.html" class="btn btn-primary">Plan Your Visit</a>
      <a href="sermons.html" class="btn btn-outline">Watch Online</a>
    </div>
  </div>
</section>

<div class="info-strip">
  <div class="container">
    <div class="info-item">
      <div class="info-icon">&#128337;</div>
      <div><h4>Service Times</h4><p>Sundays — time to be confirmed</p></div>
    </div>
    <div class="info-item">
      <div class="info-icon">&#128205;</div>
      <div><h4>Location</h4><p>164 E Church St, Bergenfield, NJ 07621</p></div>
    </div>
    <div class="info-item">
      <div class="info-icon">&#9742;</div>
      <div><h4>Get in Touch</h4><p>Phone &amp; email — pending</p></div>
    </div>
  </div>
</div>

<section>
  <div class="container">
    <div class="grid-2">
      <div>
        <div class="eyebrow">Who We Are</div>
        <h2>Faith, family, and a warm place to land.</h2>
        <p>This is a placeholder introduction — once your questionnaire answers are in, we'll replace this with your church's real story, mission statement, and voice. For now, imagine a few warm paragraphs here about who Bridge To Heaven Ministries is and what a first visit feels like.</p>
        <a href="about.html" class="btn btn-outline-teal">Learn More About Us</a>
      </div>
      <div class="placeholder-photo">Congregation / worship photo<br>goes here</div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="verse-block">
      <p class="verse">&ldquo;I am the way and the truth and the life. No one comes to the Father except through me.&rdquo;</p>
      <div class="ref">John 14:6</div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Get Involved</div>
      <h2>Ministries for every season of life</h2>
      <p>Placeholder ministry list — final names and descriptions will come from Section D/E of your questionnaire.</p>
    </div>
    <div class="grid-3">
      <div class="card">
        <div class="icon-badge">&#127793;</div>
        <h3>Children's Ministry</h3>
        <p>A safe, joyful space for kids to learn and grow in faith during service.</p>
      </div>
      <div class="card">
        <div class="icon-badge">&#10013;</div>
        <h3>Youth Ministry</h3>
        <p>Community, mentorship, and Bible study built for middle and high schoolers.</p>
      </div>
      <div class="card">
        <div class="icon-badge">&#129309;</div>
        <h3>Outreach &amp; Missions</h3>
        <p>Serving our Bergenfield neighbors and beyond with practical love.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="banner">
      <h2>Partner with us</h2>
      <p>Your generosity helps keep our doors — and our mission — open. Giving details are being finalized with the church.</p>
      <a href="give.html" class="btn btn-lime">See How to Give</a>
    </div>
  </div>
</section>
"""
write('index.html', page(
    "Home",
    "Bridge To Heaven Ministries in Bergenfield, NJ — service times, ministries, and how to visit.",
    "index.html", home_body))

# ---------------- ABOUT ----------------
about_body = """
<section class="hero" style="padding:56px 0;">
  <div class="container hero-inner">
    <span class="kicker">About Us</span>
    <h1>Our Story &amp; What We Believe</h1>
    <p class="lead">This page will hold your church's real history, mission, and statement of faith once Section A is filled in — for now, here's the shape it will take.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid-2">
      <div class="placeholder-photo">Church building / history photo</div>
      <div>
        <div class="eyebrow">Our Story</div>
        <h2>How Bridge To Heaven began</h2>
        <p><em>Placeholder — founding year, key milestones, and the story behind the name "Bridge To Heaven" will go here, drawn from your answers in Section A.</em></p>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">What We Believe</div>
      <h2>Statement of Faith</h2>
      <p><em>Placeholder — paste your statement of faith or core values here once available, or let us know and we'll help draft one.</em></p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Leadership</div>
      <h2>Meet the team</h2>
      <p>Staff photos and bios pending — one card per leader, drawn from Section F.</p>
    </div>
    <div class="grid-3">
      <div class="card">
        <div class="placeholder-photo" style="min-height:140px;margin-bottom:14px;">Photo</div>
        <h3>Pastor Name</h3>
        <p>Senior Pastor / Lead Minister — short bio pending.</p>
      </div>
      <div class="card">
        <div class="placeholder-photo" style="min-height:140px;margin-bottom:14px;">Photo</div>
        <h3>Staff Name</h3>
        <p>Role — short bio pending.</p>
      </div>
      <div class="card">
        <div class="placeholder-photo" style="min-height:140px;margin-bottom:14px;">Photo</div>
        <h3>Staff Name</h3>
        <p>Role — short bio pending.</p>
      </div>
    </div>
  </div>
</section>
"""
write('about.html', page(
    "About",
    "The story, beliefs, and leadership of Bridge To Heaven Ministries.",
    "about.html", about_body))

# ---------------- MINISTRIES ----------------
ministries_body = """
<section class="hero" style="padding:56px 0;">
  <div class="container hero-inner">
    <span class="kicker">Ministries</span>
    <h1>Find your place to grow &amp; serve</h1>
    <p class="lead">Placeholder ministry lineup — we'll swap these for your church's actual programs once Section D/E of the questionnaire is back.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid-3">
      <div class="card">
        <div class="icon-badge">&#127793;</div>
        <h3>Children's Ministry</h3>
        <p>Sunday programming for kids, age groups and curriculum pending.</p>
      </div>
      <div class="card">
        <div class="icon-badge">&#10013;</div>
        <h3>Youth Ministry</h3>
        <p>Weekly gatherings for teens — schedule to be confirmed.</p>
      </div>
      <div class="card">
        <div class="icon-badge">&#127925;</div>
        <h3>Worship &amp; Music</h3>
        <p>Our music &amp; worship team — details pending.</p>
      </div>
      <div class="card">
        <div class="icon-badge">&#128214;</div>
        <h3>Bible Study</h3>
        <p>Small groups / Bible studies — meeting times pending.</p>
      </div>
      <div class="card">
        <div class="icon-badge">&#129309;</div>
        <h3>Outreach &amp; Missions</h3>
        <p>How we serve Bergenfield and beyond — details pending.</p>
      </div>
      <div class="card">
        <div class="icon-badge">&#10084;</div>
        <h3>Men's &amp; Women's Ministry</h3>
        <p>Fellowship groups — details pending.</p>
      </div>
    </div>
  </div>
</section>
"""
write('ministries.html', page(
    "Ministries",
    "Ministries and programs at Bridge To Heaven Ministries.",
    "ministries.html", ministries_body))

# ---------------- GIVE ----------------
give_body = """
<section class="hero" style="padding:56px 0;">
  <div class="container hero-inner">
    <span class="kicker">Give</span>
    <h1>Support the mission</h1>
    <p class="lead">Every gift helps Bridge To Heaven Ministries serve our congregation and community. Full giving details are being finalized — here's the placeholder layout.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid-2">
      <div>
        <div class="eyebrow">Ways to Give</div>
        <h2>Online, in person, or by mail</h2>
        <ul class="detail-list">
          <li><b>Online giving</b> Platform to be confirmed (Section G)</li>
          <li><b>In person</b> During Sunday service</li>
          <li><b>By mail</b> 164 E Church St, Bergenfield, NJ 07621</li>
          <li><b>Tax-deductible</b> 501(c)(3) status — to be confirmed</li>
        </ul>
      </div>
      <div class="banner">
        <h2>Give Online</h2>
        <p>Your online giving button/embed will go here once a platform is selected.</p>
        <a href="contact.html" class="btn btn-lime">Ask a Question</a>
      </div>
    </div>
  </div>
</section>
"""
write('give.html', page(
    "Give",
    "Ways to give to Bridge To Heaven Ministries.",
    "give.html", give_body))

# ---------------- SERMONS (placeholder) ----------------
sermons_body = """
<section class="hero" style="padding:56px 0;">
  <div class="container hero-inner">
    <span class="kicker">Sermons</span>
    <h1>Messages &amp; Worship Online</h1>
    <p class="lead">Once your YouTube channel or livestream link is confirmed, this page will hold embedded sermon videos and a message archive.</p>
  </div>
</section>
<section>
  <div class="container">
    <span class="badge-soon">Coming Soon</span>
    <div class="grid-3">
      <div class="card"><div class="placeholder-photo" style="min-height:140px;margin-bottom:14px;">Video</div><h3>Message Title</h3><p>Date &middot; Speaker</p></div>
      <div class="card"><div class="placeholder-photo" style="min-height:140px;margin-bottom:14px;">Video</div><h3>Message Title</h3><p>Date &middot; Speaker</p></div>
      <div class="card"><div class="placeholder-photo" style="min-height:140px;margin-bottom:14px;">Video</div><h3>Message Title</h3><p>Date &middot; Speaker</p></div>
    </div>
  </div>
</section>
"""
write('sermons.html', page(
    "Sermons",
    "Watch sermons and worship online from Bridge To Heaven Ministries.",
    "sermons.html", sermons_body))

# ---------------- EVENTS (placeholder) ----------------
events_body = """
<section class="hero" style="padding:56px 0;">
  <div class="container hero-inner">
    <span class="kicker">Events</span>
    <h1>What's Happening</h1>
    <p class="lead">A calendar of upcoming events, services, and programs will live here once dates are confirmed.</p>
  </div>
</section>
<section>
  <div class="container">
    <span class="badge-soon">Coming Soon</span>
    <ul class="detail-list">
      <li><b>Event Name</b> Date &amp; time — pending</li>
      <li><b>Event Name</b> Date &amp; time — pending</li>
      <li><b>Event Name</b> Date &amp; time — pending</li>
    </ul>
  </div>
</section>
"""
write('events.html', page(
    "Events",
    "Upcoming events at Bridge To Heaven Ministries.",
    "events.html", events_body))

# ---------------- CONTACT ----------------
contact_body = """
<section class="hero" style="padding:56px 0;">
  <div class="container hero-inner">
    <span class="kicker">Contact</span>
    <h1>We'd love to meet you</h1>
    <p class="lead">Reach out with a question, or send us your info and we'll follow up before your first visit.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid-2">
      <div>
        <div class="eyebrow">Visit Us</div>
        <h2>164 E Church St</h2>
        <p>Bergenfield, NJ 07621</p>
        <ul class="detail-list">
          <li><b>Phone</b> Pending</li>
          <li><b>Email</b> info@bridgetoheavenministries.org</li>
          <li><b>Instagram</b> <a href="https://www.instagram.com/bthministry/" target="_blank" rel="noopener">@bthministry</a></li>
        </ul>
        <div style="border-radius:14px;overflow:hidden;border:1px solid var(--line);margin-top:20px;">
          <iframe
            src="https://www.google.com/maps?q=164+E+Church+St,+Bergenfield,+NJ+07621&output=embed"
            width="100%" height="260" style="border:0;" loading="lazy"
            referrerpolicy="no-referrer-when-downgrade" title="Map to Bridge To Heaven Ministries"></iframe>
        </div>
      </div>

      <div class="card">
        <h3>Send a Message</h3>
        <form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
          <input type="hidden" name="form-name" value="contact">
          <p style="display:none;"><label>Don't fill this out: <input name="bot-field"></label></p>
          <p><label style="font-size:13.5px;font-weight:600;">Name<br>
            <input type="text" name="name" required style="width:100%;padding:10px;border:1px solid var(--line);border-radius:8px;margin-top:4px;">
          </label></p>
          <p><label style="font-size:13.5px;font-weight:600;">Email<br>
            <input type="email" name="email" required style="width:100%;padding:10px;border:1px solid var(--line);border-radius:8px;margin-top:4px;">
          </label></p>
          <p><label style="font-size:13.5px;font-weight:600;">Message<br>
            <textarea name="message" rows="4" required style="width:100%;padding:10px;border:1px solid var(--line);border-radius:8px;margin-top:4px;font-family:inherit;"></textarea>
          </label></p>
          <button type="submit" class="btn btn-primary" style="border:none;cursor:pointer;">Send Message</button>
        </form>
      </div>
    </div>
  </div>
</section>
"""
write('contact.html', page(
    "Contact",
    "Contact and visit Bridge To Heaven Ministries in Bergenfield, NJ.",
    "contact.html", contact_body))

print("all pages written")
