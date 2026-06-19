# IPU144 Sentiment Analysis — Visualization Dashboard

Interactive dark-mode visualization dashboard for the IPU144 Twitter sentiment analysis project.

**Live URL:** https://cantikapf.github.io/IPU144_sentiment_analysis/

## Features

- 📊 Sentiment Distribution (bar chart + donut chart)
- ☁️ Word Cloud (top 30 most frequent terms)
- 🎯 Model Performance & Confusion Matrix
- 💬 Browsable Tweet Cards with sentiment labels
- 📈 Sentiment Trend over the IPU144 event timeline

## Deploy to GitHub Pages

This folder contains the static site. To deploy:

```bash
# 1. Navigate to your local clone of the repo
cd path/to/IPU144_sentiment_analysis

# 2. Create and switch to orphan gh-pages branch (first time only)
git checkout --orphan gh-pages
git rm -rf .

# 3. Copy the contents of this folder into the repo root
# (copy index.html and any assets into the repo root)

# 4. Commit and push
git add .
git commit -m "Deploy visualization dashboard to GitHub Pages"
git push origin gh-pages
```

Or, if you already have the gh-pages branch:
```bash
git checkout gh-pages
# copy/update index.html here
git add index.html
git commit -m "Update visualization dashboard"
git push origin gh-pages
```

After pushing, enable GitHub Pages in your repo settings:
- Go to Settings → Pages
- Source: Deploy from branch
- Branch: `gh-pages` / `(root)`
- Save

Your dashboard will be live at: **https://cantikapf.github.io/IPU144_sentiment_analysis/**

## Tech Stack

- Vanilla HTML/CSS/JavaScript (zero build step)
- [Chart.js 4.4](https://www.chartjs.org/) — all charts
- [Google Fonts — Inter + JetBrains Mono](https://fonts.google.com/)
- Data embedded statically from `Indonesia/classification_ipu_sentiment.csv`
