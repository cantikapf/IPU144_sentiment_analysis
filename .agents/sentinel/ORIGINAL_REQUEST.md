# Original User Request

## 2026-06-19T02:29:30Z

Build an interactive data visualization webpage for the IPU144 Sentiment Analysis project — a sentiment analysis of Indonesian-language Twitter data about IPU144 (parliamentary policy) — stored locally in `D:\PERSONAL PROJECT\IPU144-sentiment-viz`, configured to be hosted on GitHub Pages via the `cantikapf/IPU144_sentiment_analysis` repository, then integrated into an existing portfolio website as the 6th project entry.

Working directory: `D:\PERSONAL PROJECT`
Integrity mode: development

---

## Reference

- **Sentiment analysis repo**: https://github.com/cantikapf/IPU144_sentiment_analysis (read this to understand the data, model, and results — inspect any notebooks, CSV files, or result outputs available in the repo)
- **Portfolio local path**: `D:\PERSONAL PROJECT\cantikapf.github.io`
- **Portfolio project data file**: `D:\PERSONAL PROJECT\cantikapf.github.io\assets\js\data.js` (the `portfolioData.projects` object drives all project detail pages)
- **Portfolio project list**: `D:\PERSONAL PROJECT\cantikapf.github.io\projects.html` (carousel currently shows 5 projects labeled 001/005 to 005/005)
- **Existing project style reference**: See `project1` through `project5` entries in `data.js` — each has a `content` field with inline HTML including a browser-mockup wrapper (colored dots + URL bar div), a screenshot image, metadata block (Category/Year/Link), description paragraph, and "Project Highlights" ordered list.

---

## Requirements

### R1. Visualization project folder
Create the visualization as a self-contained static web project at `D:\PERSONAL PROJECT\IPU144-sentiment-viz\`. The entry point must be `index.html`. This folder will serve as the source for GitHub Pages.

Since there is no pre-exported output file, inspect the GitHub repo (`cantikapf/IPU144_sentiment_analysis`) — read any Jupyter notebooks, CSV/JSON files, or README — to extract or reconstruct the necessary data (sentiment label counts, word frequencies, model metrics like accuracy/precision/recall/F1, sample texts with labels, date-based sentiment breakdown). Embed this data statically into the HTML as inline JavaScript variables or JSON — no server-side dependencies.

The page must include all 5 of these visualization sections:
- **Sentiment distribution** — bar or donut chart (positive, negative, neutral counts/percentages)
- **Word cloud** — most frequent words from the tweet corpus, rendered visually
- **Confusion matrix** — model evaluation heatmap with accuracy/precision/recall/F1 displayed as metric cards
- **Sample tweets** — browsable card list or table showing example texts with their predicted sentiment label and color coding
- **Sentiment trend over time** — line or area chart showing how sentiment proportions shift across dates/time periods in the dataset

### R2. Premium dark-mode visual design
The visualization page must use a **dark mode, modern, premium aesthetic** suitable for a data science portfolio — curated color palettes (not plain red/blue/green), smooth chart animations, clean typography from Google Fonts, and micro-interactions on hover. It should feel like a professional analytics dashboard. Must be fully responsive for desktop and mobile.

### R3. GitHub Pages setup
The project at `D:\PERSONAL PROJECT\IPU144-sentiment-viz\` must be structured so it can be deployed to GitHub Pages by pushing its contents to the `gh-pages` branch of `https://github.com/cantikapf/IPU144_sentiment_analysis`. Create a `README.md` inside the folder with clear instructions on how to deploy (git commands to push to gh-pages). The live URL will be: `https://cantikapf.github.io/IPU144_sentiment_analysis/`

### R4. Portfolio integration (three files modified)
In `D:\PERSONAL PROJECT\cantikapf.github.io`:

**File 1 — `assets/js/data.js`**: Add a new entry `project6` inside `portfolioData.projects`. Follow the exact same HTML pattern as existing entries (browser mockup wrapper with red/yellow/green dots + URL bar div, image tag for `./assets/images/project6.png`, metadata block, description paragraph, "Project Highlights" `<ol>`). The link must point to `https://cantikapf.github.io/IPU144_sentiment_analysis/`.

**File 2 — `projects.html`**: The carousel currently has two slides; the second slide has only 2 items. Add the IPU144 project as a third item in the second slide (making it a full row of 3), with card numbered `006/006`, title "IPU144 Sentiment Analysis", year "2023", image `./assets/images/project6.png`, and a "Discover" link to `./detail.html?type=projects&id=project6`. Update all project numbering labels if needed (the 5 existing projects currently show 001/005 through 005/005 — update to 001/006 through 005/006, and add 006/006).

**File 3 — `assets/images/project6.png`**: Create a 770×498px thumbnail image representing the sentiment analysis dashboard. Generate this programmatically (e.g., using an HTML canvas script or a small Node/Python script run locally) — a visually styled dark-mode graphic with the project title and sentiment-related visual elements. Save it to `D:\PERSONAL PROJECT\cantikapf.github.io\assets\images\project6.png`.

---

## Acceptance Criteria

### Visualization project
- [ ] `D:\PERSONAL PROJECT\IPU144-sentiment-viz\index.html` exists and opens without errors in a browser (open the file directly)
- [ ] All 5 sections are present and render correctly: sentiment distribution, word cloud, confusion matrix, sample tweets, sentiment trend
- [ ] Charts are interactive (hover tooltips at minimum) and styled in dark mode with smooth animations
- [ ] All data is embedded statically — no broken external data fetches
- [ ] Page is responsive on mobile viewport
- [ ] `README.md` with GitHub Pages deployment instructions exists in the folder

### Portfolio integration
- [ ] `project6` entry exists in `portfolioData.projects` in `data.js`
- [ ] `detail.html?type=projects&id=project6` renders a complete project detail page (no "Data not found" error)
- [ ] `projects.html` carousel includes a visible card for IPU144 Sentiment Analysis labeled `006/006` with a working "Discover" link
- [ ] `assets/images/project6.png` exists at 770×498 aspect ratio
- [ ] All existing 5 project links and carousel navigation remain functional (no regressions)
