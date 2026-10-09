Bridge To Heaven Ministries
Static website for Bridge To Heaven Ministries, a church in Bergenfield, New Jersey. It is a multi-page HTML site with shared navigation, a mobile menu, and a single stylesheet — no framework, no build step required to view it.

Status: preview. Copy, photos, service times, leadership, sermons, events, and giving details are placeholders. A yellow bar at the top of every page marks the site as awaiting answers from the church questionnaire. Confirmed details so far are the street address, email, and Instagram.
164 E Church St, Bergenfield, NJ 07621 · info@bridgetoheavenministries.org · @bthministry

Pages

Page	File	What it holds
Home	index.html	Welcome, visit info, John 14:6, ministry cards, giving banner
About	about.html	Story, statement of faith, leadership (all pending)
Ministries	ministries.html	Children, Youth, Worship, Bible Study, Outreach, Men’s & Women’s
Sermons	sermons.html	Archive shell, waiting on a YouTube or livestream link
Events	events.html	Coming-soon list
Give	give.html	In-person, mail, and online giving (platform not chosen yet)
Contact	contact.html	Address, map, Instagram, and a message form
Home, the info strip, and the footer currently say Sunday worship and midweek Bible study times are still to be confirmed.

Stack

HTML pages generated from Python string templates
One stylesheet: styles.css
Google Fonts: Fraunces for headings, Inter for body text
Palette: deep teal (#0f5f5c), mint, cream, and lime accents
Responsive at 860px — desktop nav collapses to a toggle menu
Contact form is marked for Netlify Forms (data-netlify="true", honeypot field). It only receives submissions after the site is deployed on Netlify with forms enabled
Map embed points at the church address
Python 3 standard library only — no packages to install
Project structure

.
├── assets/
│   └── logo.png              # header, footer, and favicon
├── build_site.py             # shared header, footer, page shell, file writer
├── pages_content.py          # page bodies; run this to regenerate HTML
├── styles.css
├── index.html
├── about.html
├── ministries.html
├── sermons.html
├── events.html
├── give.html
└── contact.html
pages_content.py imports page and write from build_site.py, fills in each page body, and writes the HTML next to the scripts. Edit content in pages_content.py, not by hand in the HTML, or the next run will overwrite those edits.

Preview locally

Clone the repo and open the home page. Any static server works; a simple one:

git clone https://github.com/santanajay21/Bridge-to-Heaven-site.git
cd Bridge-to-Heaven-site
python3 -m http.server 8000
Then visit http://localhost:8000. Opening index.html directly in a browser also works.

Update the site

Edit the page body strings in pages_content.py (and the header, footer, or nav in build_site.py if those change).
Regenerate:
python3 pages_content.py
Refresh the browser.
Shared facts — address, email, service times, copyright — live in footer() inside build_site.py. Change them there so every page stays in sync.

Still to fill in

Founding story and why the church is named Bridge To Heaven
Statement of faith
Pastor and staff names, photos, and bios
Sunday and midweek service times, and a phone number
Real ministry descriptions, leaders, and schedules
Sermon videos or a livestream URL
Upcoming events
Online giving platform and tax-deductible status
Worship and congregation photos to replace the placeholder blocks
Drop new images in assets/ and point the src attributes in pages_content.py at them.

Deploy

The HTML, CSS, and assets/ folder are the whole site. They can be hosted on GitHub Pages, Netlify, or any static host.

On Netlify, publish the repository root (no build command). The contact form is already annotated for Netlify Forms; confirm the form appears under Forms after the first deploy.

Credits

## Credits

Volunteer project, with help from Emmanuel Reynoso. Provided at no cost.

© 2026 Bridge To Heaven Ministries.
