# Modern academic website — visual redesign overlay

This update is for **tufu0321.github.io**, an existing **Academic Pages / Jekyll** site. It changes presentation and homepage/research content only; it does **not** replace the layout templates, theme core, Ruby dependencies, navigation, or publication data.

## Files changed

- `_pages/about.md` — polished homepage with research cards and selected papers
- `_pages/research.md` — styled research-area panels
- `assets/css/custom-academic.css` — typography, colors, navigation, sidebar, cards, mobile layout
- `_includes/head/custom.html` — reference to the stylesheet

## Install safely (Ubuntu)

From your existing repository:

```bash
cd /media/ssd/tufan_data/Github_repo/tufu0321.github.io
git status
# Recommended: first make a backup or commit the current working website.
```

Extract `tufan-modern-academic-overlay.zip` into the **root** of your existing repository, merging those four paths. Do **not** run `scripts/apply_site_settings.py` again: this redesign does not need configuration changes.

```bash
bundle exec jekyll serve --livereload
```

Visit http://localhost:4000 and check the homepage, research, publications, teaching, contact, profile sidebar and mobile width. If styles do not update, hard refresh with Ctrl+Shift+R. The CSS targets Academic Pages' standard selectors; minor variations in old forks may need adjustment.

## Publish

```bash
git status
git add _pages/about.md _pages/research.md assets/css/custom-academic.css _includes/head/custom.html
git commit -m "Polish academic website visual design"
git push origin "$(git branch --show-current)"
```

## Notes

- Your existing `_config.yml`, publications, teaching and contact information are intentionally left untouched.
- The stylesheet includes responsive layouts and reduced-motion support.
- Profile image is not bundled; retain/replace `images/profile.png` separately.
- The website was **not** Jekyll-built inside this delivery environment; verify locally before pushing.
