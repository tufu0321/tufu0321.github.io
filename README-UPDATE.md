# Tufan Ghosh academic website update

This **overlay** preserves the existing `tufu0321.github.io` Academic Pages/Jekyll repository. It is **not** a full replacement repository.

## Included

- `_pages/about.md`, `research.md`, `publications.html`, `teaching.html`, `contact.md`
- `_data/navigation.yml` — streamlined navigation
- `assets/css/custom-academic.css` — responsive styles
- `_includes/head/custom.html` — loads the stylesheet (check compatibility with your site's header include)
- `scripts/apply_site_settings.py` — updates selected values in your existing `_config.yml` without replacing it

## Install on Ubuntu/Linux

```bash
git clone https://github.com/tufu0321/tufu0321.github.io.git
cd tufu0321.github.io
# Extract the ZIP overlay INTO this directory, merging folders.
python3 scripts/apply_site_settings.py
git status
```

**Important:** The existing Academic Pages theme includes a custom head fragment. This update preserves its original icon links and appends the new stylesheet. If the stylesheet does not load, add the following line to the active head include:

```liquid
<link rel="stylesheet" href="{{ '/assets/css/custom-academic.css' | relative_url }}">
```

Check the existing `images/profile.png` (specified in `_config.yml`). Add your own photograph if needed; no photograph was downloaded or substituted.

## Remove default demo materials

The overlay replaces the default homepage, teaching listing page, and publications listing page. Existing sample entries under `_publications`, `_teaching`, `_talks`, `_portfolio`, and `_posts` **remain in the repository** to avoid deleting your work. Their navigation links are hidden by the new menu, but some may still be accessible at direct URLs. Review and remove demonstration files as appropriate, especially if restoring collection-driven pages later.

## Preview and publish

```bash
bundle install
bundle exec jekyll serve --livereload
# Visit http://localhost:4000
```

Then, when satisfied:

```bash
git add _pages _data/navigation.yml assets/css/custom-academic.css _includes/head/custom.html _config.yml scripts/apply_site_settings.py
git commit -m "Create academic website from Google Sites content"
git push origin master
```

GitHub Pages should build it using your existing configuration. Check repository **Settings → Pages** and **Actions** for build status.

## Editorial checks

- Confirm current position, affiliation, office contact, and 2026 publication details.
- Make sure the email and phone number are intended to be public.
- Update teaching dates as new courses are offered.
- Add a verified ORCID/LinkedIn URL if desired; neither is invented here.
- The source site does not offer a clearly accessible full research biography; research descriptions are summarized from publication topics and ongoing directions rather than copied verbatim.
