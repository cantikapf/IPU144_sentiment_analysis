# Task: Implement Visualization Dashboard (index.html)

## Identity
- Archetype: teamwork_preview_worker
- Working directory: D:\PERSONAL PROJECT\IPU144-sentiment-viz\.agents\teamwork_preview_worker_m3
- Role: Implementer/Worker

## Objective
Create a premium, dark-mode, self-contained static HTML dashboard `index.html` at `D:\PERSONAL PROJECT\IPU144-sentiment-viz\index.html`. It must visually represent the extracted sentiment analysis data from the IPU144 Indonesian Twitter dataset.

## Specifications
1. **Tech Stack**: Single self-contained HTML file. You may use Tailwind CSS (CDN), Chart.js (CDN), or D3.js (CDN) for styling and interactive charts.
2. **Design Theme**: Premium Dark Mode aesthetic (deep grays/blacks, high-contrast text, vibrant accents for sentiment labels: green/blue for positive, red/orange for negative, gray/yellow for neutral).
3. **Interactive Sections (5)**:
   - **Sentiment Distribution**: Chart (e.g., Pie, Doughnut, or Bar) displaying Positive (213 / 61.56%), Negative (83 / 23.99%), and Neutral (50 / 14.45%) sentiments.
   - **Interactive Word Cloud**: Visual representation of the most common terms (ipu, zeroemission, stopclimatechange, indonesia, bal, dpr, puan, maret, rusia, ukraina, damai, etc.) rendered using HTML5 Canvas or SVG, allowing hover/click interactivity.
   - **Confusion Matrix & Performance Metrics Section**: Explicitly present that model evaluation metrics (Accuracy, Precision, Recall, F1) and a confusion matrix are mathematically N/A because VADER is an unsupervised lexicon-based classifier and no manual ground-truth labels are present in the dataset. Display this explanation inside a visually polished card/banner.
   - **Browsable Sample Tweets**: A search-and-filter-enabled table or grid showing representative tweets, their English translations, predicted sentiments, and compound scores. Use the sample tweets data from Milestone 1.
   - **Sentiment Trend over Time**: Visually explain that chronological trend data is N/A because tweet timestamp metadata was not captured. Provide a clean timeline/event-window graphic or description mapping the sentiment to the 144th IPU Assembly event window (March 20-24, 2022, Nusa Dua, Bali) where the tweets were concentrated.
4. **Data Input**: Embed the extracted data from `D:\PERSONAL PROJECT\IPU144-sentiment-viz\.agents\teamwork_preview_explorer_m1\extracted_data.json` directly into the script or load it locally. Since the page should run standalone in a browser (e.g. file:// protocol), embedding the JSON data directly into a JS variable in `index.html` is the most robust and standard approach.

## Constraints
- **MANDATORY INTEGRITY WARNING**: DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task.
- Do not write code directly in this orchestrator window. All edits must be done by you inside the target file `D:\PERSONAL PROJECT\IPU144-sentiment-viz\index.html`.
- Run tests and verify the visual output.

## Output
Write `index.html` to `D:\PERSONAL PROJECT\IPU144-sentiment-viz\index.html` and document your changes in `D:\PERSONAL PROJECT\IPU144-sentiment-viz\.agents\teamwork_preview_worker_m3\changes.md` and `handoff.md`.
