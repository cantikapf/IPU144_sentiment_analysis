# Project Plan: IPU144 Sentiment Analysis Portfolio Integration

## Objective
Build an interactive data visualization webpage for the IPU144 Sentiment Analysis project, host it locally at `D:\PERSONAL PROJECT\IPU144-sentiment-viz`, write a README with deployment instructions to `gh-pages` (R1, R2, R3), and integrate it as the 6th project in the `cantikapf.github.io` portfolio (R4) with programmatic thumbnail generation.

## Milestones

### Milestone 1: Exploration & Data Extraction
- **Task**: Inspect the local repository at `D:\Twitter Scrape\IPU144_sentiment_analysis\Indonesia\` to read `twitter scrape_indo.ipynb` and related CSV files. Extract sentiment label counts, word frequencies, model evaluation metrics (accuracy, precision, recall, F1), sample tweets with predicted labels, and date/time trend data.
- **Worker**: `teamwork_preview_explorer` (Explorer 1)
- **Output**: Analysis report and a static `data.json` / `data.js` containing the extracted data.
- **Verification**: Verify that the JSON contains valid metrics, counts, word frequencies, and trends, and matches the data in the notebooks/CSVs.

### Milestone 2: E2E Testing Track Setup
- **Task**: Set up a robust, opaque-box E2E testing framework to verify all acceptance criteria: visualization dashboard sections rendering, styling, portfolio JS data integration, projects list HTML correctness, and thumbnail size.
- **Worker**: `self` (spawned as E2E Testing Orchestrator)
- **Output**: Test suite scripts and `TEST_READY.md` containing test specifications and coverage thresholds.
- **Verification**: Run E2E test harness and check that tests run and fail initially (Red phase).

### Milestone 3: Visualization Dashboard Implementation
- **Task**: Create the self-contained static dashboard `index.html` in `D:\PERSONAL PROJECT\IPU144-sentiment-viz\index.html` with the 5 interactive sections: Sentiment distribution (chart), Word cloud (interactive SVG or Canvas), Confusion matrix (heatmap + metrics), Sample tweets (browsable table), and Sentiment trend over time (line/area chart). Ensure dark mode premium visual aesthetic.
- **Worker**: `self` (spawned as Worker)
- **Output**: `D:\PERSONAL PROJECT\IPU144-sentiment-viz\index.html` and assets.
- **Verification**: Open the dashboard directly in a browser. Run E2E tests for the dashboard.

### Milestone 4: README & Deployment Instructions
- **Task**: Create a `README.md` at `D:\PERSONAL PROJECT\IPU144-sentiment-viz\README.md` with clear instructions on how to deploy to `gh-pages` branch using git commands.
- **Worker**: `self` (spawned as Worker)
- **Output**: `README.md`
- **Verification**: Inspect file contents and verify git commands are correct.

### Milestone 5: Portfolio HTML & JS Integration
- **Task**: Update `cantikapf.github.io\assets\js\data.js` to add `project6` entry with proper browser mockup wrapper HTML. Update `cantikapf.github.io\projects.html` to add the card, update project numbering (001/006 to 006/006), and ensure carousel links work correctly.
- **Worker**: `self` (spawned as Worker)
- **Output**: Updated `data.js` and `projects.html`.
- **Verification**: Run E2E tests on portfolio integration, open portfolio page, and click links to verify no "Data not found" or navigation errors occur.

### Milestone 6: Thumbnail Generation
- **Task**: Programmatically generate a 770x498px thumbnail image representing the dashboard and save it to `cantikapf.github.io\assets\images\project6.png`.
- **Worker**: `self` (spawned as Worker)
- **Output**: `project6.png` at `D:\PERSONAL PROJECT\cantikapf.github.io\assets\images\project6.png`.
- **Verification**: Verify that the image exists and matches the exact 770x498 dimensions.

### Milestone 7: Final Audit & Victory Verification
- **Task**: Run full E2E testing suite, run the Forensic Auditor, review all outputs, and finalize the project handoff.
- **Worker**: `teamwork_preview_reviewer` (Reviewers) and `teamwork_preview_auditor` (Auditor)
- **Output**: Clean audit report and complete handoff.
- **Verification**: 100% test pass rate, clean audit verdict.
