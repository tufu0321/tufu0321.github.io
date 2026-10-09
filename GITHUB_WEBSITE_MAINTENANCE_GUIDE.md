# Maintaining and Customizing Your Academic Website

**Website:** https://tufu0321.github.io  
**Repository:** https://github.com/tufu0321/tufu0321.github.io  
**Framework:** Academic Pages / Jekyll  
**Design:** Modern academic overlay (October 2026)

This guide documents the files in the **website update package** and the **modern design overlay** provided for your repository. It explains exactly where to edit content, appearance, links, and settings, and how to preview and publish safely.

> **Scope:** This guide is based on the two provided ZIP packages, rather than a fresh inspection of your local Git checkout. Your repository may include additional files. Edit existing files rather than creating duplicate pages or configuration keys.

---

## 1. At a glance: what to edit where

| I want to change… | File to edit | What to look for |
|---|---|---|
| Name, large introduction, homepage biography | `_pages/about.md` | `.tg-hero`, `## About me` |
| Homepage research cards | `_pages/about.md` | `<div class="tg-grid">` |
| Homepage featured publications | `_pages/about.md` | `<div class="tg-pub">` |
| Full research descriptions | `_pages/research.md` | `## Phase-field…`, `## Multiscale…`, `## Numerical…` |
| Publications, DOI links, software citations | `_pages/publications.html` | `<div class="publication-entry">` |
| Teaching history and course cards | `_pages/teaching.html` | `<div class="course-card">` |
| Email, office, telephone | `_pages/contact.md` | `## Tufan Ghosh`, `## Office` |
| Top navigation labels and order | `_data/navigation.yml` | `main:` |
| Sidebar name, biography, photo, profile links | `_config.yml` | `author:` |
| Site title, URL, description | `_config.yml` | top-level `title`, `description`, `url`, `baseurl` |
| Colors, font sizes, cards, spacing, mobile styles | `assets/css/custom-academic.css` | `:root`, `.tg-*`, `@media` |
| Loading custom CSS | `_includes/head/custom.html` | `custom-academic.css` link |
| Profile picture itself | `images/profile.png` (as supplied) | Replace image, keep matching filename |
| Add a CV (PDF) | `files/cv.pdf` or another chosen path | Create file; add link to a page or sidebar |
| Favicon | `images/favicon.svg`, PNG variants | Replace asset with same filename |
| Preview & deployment | Terminal, GitHub repository | `bundle exec jekyll serve`, `git push` |

> **Important:** The homepage is stored in `_pages/about.md` even though its public URL is `/`. Do not create a separate `index.md` for the same path without first checking your existing routing.

## 2. Understand the repository structure

Relevant structure after applying both packages:

```text
tufu0321.github.io/
├── _config.yml                     # Site-wide settings + sidebar
├── Gemfile                         # Ruby/Jekyll dependencies
├── _data/
│   └── navigation.yml              # Menu tabs
├── _pages/
│   ├── about.md                    # Homepage (permalink: /)
│   ├── research.md                 # Research page
│   ├── publications.html           # Publications page
│   ├── teaching.html               # Teaching page
│   └── contact.md                  # Contact page
├── _includes/
│   └── head/
│       └── custom.html             # Loads supplemental CSS
├── assets/
│   └── css/
│       └── custom-academic.css     # Colors and layout
├── images/
│   └── profile.png                 # Profile photo (expected name)
├── scripts/
│   └── apply_site_settings.py      # One-time configuration helper
└── README-MODERN-DESIGN.md         # Overlay notes (if retained)
```

The actual repository also contains theme folders such as `_layouts`, `_sass`, `_includes`, and potentially collections. **Normally you do not need to edit them** for routine updates.

### Markdown, HTML, YAML, and Liquid

- **Markdown:** `## Heading`, `**bold**`, `[label](https://example.com)` — easy for prose.
- **HTML:** `<div>`, `<h3>`, `<a>` — used for styled cards and publication rows.
- **YAML:** `key: value` — used in `_config.yml`, navigation, and the front matter at the top of page files.
- **Liquid:** `{{ '/research/' | relative_url }}` — Jekyll's way to generate paths that work with the configured site URL.

Always keep the YAML `---` blocks at the beginning of page files. Indentation in YAML matters; use spaces rather than tabs.

---

## 3. Edit the homepage

**File:** `_pages/about.md`

The top of the file currently contains:

```yaml
---
permalink: /
title: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---
```

- `permalink: /` makes this the homepage.
- `title: ""` keeps the generic page heading empty so the large custom name header can dominate.
- `author_profile: true` shows the profile sidebar.
- `redirect_from` preserves the older About URLs if the corresponding Jekyll plugin is active.

### 3.1 Change your name and headline

Find:

```html
<div class="tg-hero">
  <div class="tg-kicker">Researcher · Applied mathematics &amp; computational science</div>
  <h1>Tufan Ghosh <span class="tg-native">তুফান ঘোষ</span></h1>
  <p>I develop mathematical models and numerical methods ...</p>
```

Change the kicker, `<h1>`, and `<p>` to your preferred wording. To remove the Bengali name, remove only the `<span class="tg-native">…</span>` element.

**Tip:** Keep the introduction to approximately 2–4 lines on desktop for a balanced hero area.

### 3.2 Edit the buttons

Find:

```html
<div class="tg-actions">
  <a class="tg-button" href="{{ '/research/' | relative_url }}">Explore my research ↗</a>
  <a class="tg-button tg-button--ghost" href="{{ '/publications/' | relative_url }}">Browse publications →</a>
</div>
```

The actual source includes separate arrow spans; you can preserve them. Edit the visible button text and/or the URL.

Examples:

```html
<a class="tg-button" href="{{ '/research/' | relative_url }}">Research</a>
<a class="tg-button tg-button--ghost" href="{{ '/files/cv.pdf' | relative_url }}">Download CV</a>
```

Create `files/cv.pdf` before adding the CV link.

### 3.3 Change the topic badges

Look for `.tg-strip` and `.tg-chip`:

```html
<div class="tg-strip">
  <span class="tg-chip">Phase-field methods</span>
  <span class="tg-chip">Porous-media flow</span>
</div>
```

Add, delete, or rename chip elements to match your research interests.

### 3.4 Update the three research cards

Find:

```html
<div class="tg-grid">
  <a class="tg-card" href="{{ '/research/#phase-field-and-moving-interfaces' | relative_url }}">
    <span class="tg-card__num">01 / INTERFACES</span>
    <h3>Phase-field modelling</h3>
    <p>Diffuse interfaces, evaporation, precipitation ...</p>
  </a>
  ...
</div>
```

Each `<a class="tg-card"> ... </a>` is **one entire card**. Edit its heading, short explanation, and target URL.

To add a fourth research card, copy an entire card and update its contents. The desktop layout currently uses three columns; a fourth will wrap to the next row. Adjust `.tg-grid` in CSS if you want two columns instead.

**Anchor links:** The `#phase-field-and-moving-interfaces` portion points to an automatically generated heading ID on the research page. If you rename that heading, verify that the anchor still works. You can avoid the ambiguity by adding an explicit `<h2 id="phase-field-and-moving-interfaces">…</h2>`.

### 3.5 Update featured publications

Find rows beginning:

```html
<div class="tg-pub">
  <span class="tg-year">2026</span>
  <div>
    <h3>Paper title</h3>
    <p><em>Journal name</em></p>
    <a href="https://doi.org/...">Read paper ↗</a>
  </div>
</div>
```

Edit the year, title, venue, and DOI URL. For consistency, keep approximately three selected papers on the homepage and the full list on the publications page.

**Important:** The featured publications and the full publications page are presently maintained **separately**. Updating a paper in one place does **not** automatically update the other.

### 3.6 Change the biography and contact sentence

Edit the paragraphs under `## About me` and `## Let's connect`. For an email link:

```markdown
[tufan.ghosh@iws.uni-stuttgart.de](mailto:tufan.ghosh@iws.uni-stuttgart.de)
```

---

## 4. Edit your research page

**File:** `_pages/research.md`

It currently contains three subject headings:

```markdown
## Phase-field and moving interfaces
## Multiscale upscaling
## Numerical methods
```

Each topic has a styled feature panel:

```html
<div class="tg-feature">
  <h3>Diffuse-interface models for multiphase systems</h3>
  <p>Describe the research question, methods, and applications here.</p>
</div>
```

To update a research area, replace its explanatory paragraph. To add a new area, add another `##` heading and corresponding `.tg-feature` block.

A useful structure for more detailed sections:

```markdown
## Evaporation and precipitation in porous media

A short description of the physical processes and why they matter.

### Modelling approaches

Describe governing models, asymptotics, discretization, and validation.

### Related publication

[Paper title](https://doi.org/your-doi)
```

For research graphics, place your own images in `images/research/` and add:

```markdown
![Short accessible description]({{ '/images/research/evaporation.png' | relative_url }})
```

Use compressed PNG/WebP images where possible and give each image informative alternative text.

---

## 5. Add or change publications

**File:** `_pages/publications.html`

This file presently has **Journal articles**, **Preprints**, and **Software contributions** sections. Each journal paper is a self-contained HTML row, for example:

```html
<div class="publication-entry">
  <span class="pub-year">2026</span>
  <div>
    <h3>Article title</h3>
    <p>Author One, Author Two, Tufan Ghosh</p>
    <p>
      <em>Journal Name</em> ·
      <a href="https://doi.org/10.xxxx/example"
         target="_blank" rel="noopener noreferrer">DOI ↗</a>
    </p>
  </div>
</div>
```

### Add a new publication

1. Copy an entire `<div class="publication-entry"> ... </div>` block.
2. Paste it in the correct year position under `## Journal articles`.
3. Replace year, title, authors, journal name and full DOI URL.
4. Verify the DOI in a browser.
5. If this is a highlighted paper, update `_pages/about.md` separately.

For preprints, use an arXiv link if one exists. For software, edit the Markdown list under `## Software contributions`.

**Be careful with `<div>` tags:** each opening `<div>` needs a corresponding closing `</div>`. A missing tag may disrupt the layout of all subsequent publications.

**Optional future enhancement:** Use Jekyll's `_publications/` collection and a generated publications listing so entries are not maintained twice. That is a structural enhancement, **not** how the provided overlay currently works.

---

## 6. Edit teaching information

**File:** `_pages/teaching.html`

The Stuttgart courses use cards:

```html
<div class="course-card">
  <span class="course-term">Summer 2025 · 2024</span>
  <h3>Course title</h3>
  <p>Course description.</p>
</div>
```

For a new course, copy the full block, update the semester, course title, and description, and place it under the correct university heading.

Earlier teaching experience is stored as a Markdown bullet list. You can edit it directly:

```markdown
- **MA51003 · Fluid Mechanics** — July–December 2016
```

---

## 7. Edit your contact page

**File:** `_pages/contact.md`

Update your position, department, institution, office address, phone, and email in the main body.

Examples:

```markdown
**Email:** [tufan.ghosh@iws.uni-stuttgart.de](mailto:tufan.ghosh@iws.uni-stuttgart.de)

**Phone:** [+49 (0) 711 685 60136](tel:+4971168560136)
```

When you change your email or affiliation, also check `_config.yml` and the contact sentence in `_pages/about.md`; these are currently separate copies.

---

## 8. Update your sidebar and profile photo

### 8.1 Change profile data

**File:** `_config.yml`

Find the existing `author:` block, then edit the fields *inside that block*:

```yaml
author:
  avatar: "profile.png"
  name: "Tufan Ghosh"
  bio: "Porous media · Multiscale modelling · Phase-field methods"
  location: "Stuttgart, Germany"
  employer: "University of Stuttgart"
  email: "tufan.ghosh@iws.uni-stuttgart.de"
  github: "tufu0321"
```

Your configuration may contain other fields such as `googlescholar`, `orcid`, `twitter`, `researchgate`, etc. Preserve the field names supported by your actual theme. Some profile links only appear when the relevant value exists **and** the theme's sidebar template supports it.

**Do not add a second `author:` block.** YAML duplicates can cause confusing behavior.

### 8.2 Replace the portrait

The supplied update expects:

```text
images/profile.png
```

Replace that file with a square or near-square photo, ideally around 500–800 pixels wide, and retain the filename. If you instead choose `new-photo.jpg`, update the `author.avatar` setting accordingly.

If the photo appears unchanged, try a hard refresh (`Ctrl+Shift+R`) or confirm that the actual sidebar template resolves the avatar path you expect.

### 8.3 Add a CV link

Option A — add a prominent link on the homepage:

1. Copy your PDF to `files/cv.pdf`.
2. Add in `_pages/about.md`:

```markdown
[Download my academic CV (PDF)]({{ '/files/cv.pdf' | relative_url }})
```

Option B — add a link to a sidebar profile list, if the theme's sidebar include and configuration format support it. Do not assume adding an arbitrary YAML key automatically creates a sidebar item.

---

## 9. Change the navigation menu

**File:** `_data/navigation.yml`

Current menu:

```yaml
main:
  - title: "Home"
    url: /
  - title: "Research"
    url: /research/
  - title: "Publications"
    url: /publications/
  - title: "Teaching"
    url: /teaching/
  - title: "Contact"
    url: /contact/
```

Reorder entire two-line entries to change menu order. Change `title` to rename the visible tab; change `url` to change its destination.

### Add a CV tab

```yaml
  - title: "CV"
    url: /files/cv.pdf
```

Ensure the file exists. If your theme expects `url` values to be relative to the site root, the above is suitable for `baseurl: ""`.

### Add a new Projects page

1. Create `_pages/projects.md`:

```markdown
---
layout: single
title: "Projects"
permalink: /projects/
author_profile: true
---

# Research projects

Add your projects here.
```

2. Add to `_data/navigation.yml`:

```yaml
  - title: "Projects"
    url: /projects/
```

3. Restart or reload the local Jekyll preview and test the link.

---

## 10. Change colors, typography, cards, and spacing

**File:** `assets/css/custom-academic.css`

This file is the main entry point for visual design changes. The provided overlay defines these CSS custom properties near the top:

```css
:root {
  --tg-navy: #14273d;
  --tg-ink: #22354b;
  --tg-muted: #586c7d;
  --tg-teal: #087e88;
  --tg-teal-dark: #006872;
  --tg-border: #dfebef;
  --tg-mist: #f3f9f9;
  --tg-white: #fff;
  --tg-radius: 18px;
  --tg-shadow: 0 16px 40px rgba(23,61,76,.075);
}
```

**Note:** The actual CSS in the ZIP is mostly minified (several rules on each line). Searching for a selector is easier than relying on a line number. You may reformat it for readability without changing its behavior.

| Desired appearance change | Selector or setting |
|---|---|
| Main dark text | `--tg-ink` |
| Heading navy | `--tg-navy` |
| Accent buttons and links | `--tg-teal`, `--tg-teal-dark` |
| Pale boxes and borders | `--tg-mist`, `--tg-border` |
| Rounded card corners | `--tg-radius` |
| Navbar layout | `.masthead`, `.greedy-nav` |
| Sidebar photo and text | `.sidebar .author__avatar img`, `.sidebar .author__bio` |
| Homepage hero background | `.tg-hero` |
| Homepage large name | `.tg-hero h1` |
| Hero buttons | `.tg-button`, `.tg-button--ghost` |
| Topic chips | `.tg-chip` |
| Research card layout | `.tg-grid`, `.tg-card` |
| Publication rows | `.tg-pub`, `.publication-entry` |
| Teaching panels | `.course-card` |
| General research panels | `.tg-feature` |
| Intro callouts | `.page-lede` |
| Mobile/tablet adjustments | `@media(max-width:1050px)` and `@media(max-width:700px)` |

### Example: change accent from teal to blue

Update these variables:

```css
:root {
  --tg-teal: #2466aa;
  --tg-teal-dark: #164e87;
}
```

Some colors in the stylesheet are written directly as hex codes (for example, the hero gradient and hover states), so changing the variables **will not recolor every element**. Search for the older teal color codes if you want a fully consistent palette.

### Example: make homepage cards two columns

Change:

```css
.tg-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}
```

to:

```css
.tg-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
```

Keep the responsive media queries so smaller screens still use fewer columns.

### Example: make the hero less tall

Find `.tg-hero` and reduce `padding: 3.4rem 3.2rem` to, for example, `padding: 2.5rem 2.4rem`.

### Example: change name size

Find `.tg-hero h1` and adjust:

```css
font-size: clamp(2.5rem, 5.3vw, 4.15rem);
```

The three values are minimum size, viewport-responsive size, and maximum size.

### What NOT to edit first

Avoid editing core theme CSS or generated files under `_site/`. Your overlay is specifically designed to keep styling changes in `custom-academic.css` and to load that stylesheet after the theme CSS.

---

## 11. Verify the custom CSS is loaded

**File:** `_includes/head/custom.html`

The modern overlay contains:

```liquid
<link rel="stylesheet" href="{{ '/assets/css/custom-academic.css' | relative_url }}" />
```

That line is essential. If changes to the CSS have no visual effect:

1. Confirm the file exists in `assets/css/`.
2. Confirm this include is actually inserted in the HTML `<head>` by your theme.
3. Use the browser's Developer Tools → Network to check for a successful CSS request.
4. Hard refresh using `Ctrl+Shift+R`.
5. Inspect whether a later-loaded CSS rule overrides yours.

Don't add the same stylesheet reference repeatedly.

---

## 12. Safely preview changes locally

Use the directory you have already been working in:

```bash
cd /media/ssd/tufan_data/Github_repo/tufu0321.github.io
bundle exec jekyll serve --livereload
```

Open:

**http://localhost:4000**

Use `Ctrl+C` to stop the server.

### Important preview checks

- Desktop: navigation stays aligned; cards have consistent heights.
- Mobile: no horizontal scrolling; buttons and cards stack.
- Home: name, research links, selected publications and email work.
- Publications: all DOI links open the right papers.
- Research: homepage card anchors point to correct headings.
- Profile: photo appears and sidebar links are correct.
- CV: PDF opens if you added a CV link.

Run a production-style build to expose configuration errors:

```bash
bundle exec jekyll build
```

The generated `_site/` directory is **output**, not a source file to edit.

---

## 13. Publish your modifications to GitHub

Before your first substantial edit, save the current working version:

```bash
git status
git add _config.yml _data/navigation.yml _pages assets/css/custom-academic.css _includes/head/custom.html
git commit -m "Save working academic website before customization"
```

This is an example; Git may report there is nothing new to commit if the files were previously saved.

After editing and previewing:

```bash
git status
git diff
git add _config.yml _data/navigation.yml _pages assets/css/custom-academic.css _includes/head/custom.html
git commit -m "Update academic website content and styling"
git push origin "$(git branch --show-current)"
```

**If you added images, CV files, or new pages**, stage those paths too (for example `git add images files _pages/projects.md`).

Confirm `.gitignore` excludes locally generated artifacts, e.g.:

```gitignore
_site/
.bundle/
vendor/
.jekyll-cache/
```

**Before pushing:** inspect `git status` and `git diff --cached` for accidentally staged personal or generated files.

Visit the GitHub repository's **Actions** tab to verify deployment. Your live address is:

https://tufu0321.github.io

If GitHub Pages does not update, check **Settings → Pages** and confirm that the configured publishing source matches the branch or workflow you are using.

---

## 14. Make updates efficiently

### Routine changes

| Frequency | Recommended task |
|---|---|
| Whenever a new article is published | Update `_pages/publications.html` and optionally selected papers on `_pages/about.md` |
| Whenever you begin a project | Add a paragraph or topic block to `_pages/research.md` |
| Each semester | Update `_pages/teaching.html` |
| When affiliation/contact changes | Update `_config.yml`, `_pages/contact.md`, and homepage contact text |
| Every few months | Verify external links, DOI references, portrait, CV |
| When redesigning | Change `assets/css/custom-academic.css`, inspect mobile layout |

### Edit → preview → publish checklist

```bash
# 1. Get current version (only when working tree is clean)
git pull --ff-only

# 2. Edit the relevant source file(s)

# 3. Preview in browser
bundle exec jekyll serve --livereload

# 4. After stopping server, review and commit
git status
git diff
git add <paths-you-edited>
git commit -m "Describe the website update"

# 5. Publish
git push origin "$(git branch --show-current)"
```

Replace `<paths-you-edited>` with the filenames; do not type the angle brackets literally.

---

## 15. Troubleshooting

| Problem | Likely reason | What to try |
|---|---|---|
| CSS edits don't appear | Browser cache or stylesheet not loaded | Hard refresh; verify `_includes/head/custom.html` and Network tab |
| Page shows `{{ ... }}` verbatim | Liquid syntax not rendered | Confirm Jekyll processes the file and it has proper front matter |
| Navigation link goes to 404 | `permalink` and nav URL disagree | Check `_pages/…` front matter and `_data/navigation.yml` |
| Homepage card goes to wrong section | Heading anchor changed | Fix the `#…` fragment or give the heading an explicit ID |
| Profile photo missing | Filename/path mismatch | Check `author.avatar` and `images/` location |
| Broken layout after publication edit | Unbalanced HTML `div` tags | Compare a new publication block with an existing working one |
| `bundle exec jekyll` fails | Missing Ruby gems | Run `bundle install`; check Ruby development dependencies |
| Bundler permission error | Gems installing system-wide | Use `bundle config set --local path vendor/bundle` |
| Changes not live | Not pushed or failed Pages build | Check branch, Actions logs, and Settings → Pages |
| Git wants to commit hundreds of gem files | `vendor/` not ignored | Add it to `.gitignore`, then check staging |

### Avoid rerunning the setup script for normal edits

`scripts/apply_site_settings.py` was supplied for the **initial** configuration of your website. It sets several values in `_config.yml`; running it after you customize your author details could overwrite your changes. For ongoing maintenance, edit `_config.yml` directly.

---

## 16. Suggested improvements as your website grows

You can gradually add:

- A standalone **CV** page and downloadable PDF.
- **Projects** pages with your own simulation figures and technical descriptions.
- A **Software** page for DuMux contributions and reusable computational tools.
- A **News** or **Updates** section for recent publications and talks.
- An automatically generated publication list to avoid duplicate manual updates.

These are optional enhancements; your current Academic Pages structure is already suitable for maintaining a professional personal academic website.

---

### Quick reference

**Content:** `_pages/`  
**Site identity & sidebar:** `_config.yml`  
**Navigation:** `_data/navigation.yml`  
**Appearance:** `assets/css/custom-academic.css`  
**Stylesheet inclusion:** `_includes/head/custom.html`  
**Portrait and graphics:** `images/`  
**Local preview:** `bundle exec jekyll serve --livereload`  
**Publish:** `git add` → `git commit` → `git push`
