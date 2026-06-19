# E2E Test Infra: IPU144 Sentiment Viz & Portfolio Integration

## Test Philosophy
- **Opaque-box & Requirement-driven**: The E2E test suite evaluates the project from the perspective of an end user. It asserts functionality via external interfaces (HTML structure, DOM elements, CSS styles, query parameters, file metadata, and image resolution) without relying on internal code implementations.
- **Methodology**: Apply Category-Partitioning, Boundary Value Analysis, Pairwise Combinatorial Testing, and Real-World Workload Testing to ensure complete and robust coverage.

## Feature Inventory
| # | Feature | Source (requirement) | Tier 1 (Feature Coverage) | Tier 2 (Boundary & Corner) | Tier 3 (Cross-Feature) |
|---|---------|---------------------|:--------------------------:|:--------------------------:|:----------------------:|
| F1 | Sentiment Distribution Chart | plan.md §3 | 5 | 5 | ✓ |
| F2 | Interactive Word Cloud | plan.md §3 | 5 | 5 | ✓ |
| F3 | Confusion Matrix & Performance Metrics | plan.md §3 | 5 | 5 | ✓ |
| F4 | Browsable Sample Tweets Table | plan.md §3 | 5 | 5 | ✓ |
| F5 | Sentiment Trend over Time | plan.md §3 | 5 | 5 | ✓ |
| F6 | Premium Dark Mode Aesthetic | plan.md §3 | 5 | 5 | ✓ |
| F7 | Project README & Instructions | plan.md §4 | 5 | 5 | ✓ |
| F8 | Portfolio Integration: data.js | plan.md §5 | 5 | 5 | ✓ |
| F9 | Portfolio Integration: projects.html | plan.md §5 | 5 | 5 | ✓ |
| F10| Programmatic Thumbnail | plan.md §6 | 5 | 5 | ✓ |

## Test Architecture
- **Language**: Python 3.x
- **Framework**: `unittest` standard library with `playwright` sync API
- **Execution Mode**: Headless Chromium (Chrome)
- **Directory Layout**:
  ```
  D:\PERSONAL PROJECT\IPU144-sentiment-viz\
  ├── index.html (visualization dashboard)
  ├── e2e_tests/
  │   ├── __init__.py
  │   ├── test_dashboard.py    # Tests F1-F6
  │   ├── test_portfolio.py    # Tests F8-F9
  │   ├── test_assets.py       # Tests F7, F10
  │   └── run_tests.py         # Test runner and reporter
  ```
- **Pass/Fail Semantics**: The test suite returns exit code `0` if all tests pass. Any failure returns a non-zero exit code.

## Real-World Application Scenarios (Tier 4)
| # | Scenario | Features Exercised | Complexity |
|---|----------|--------------------|------------|
| 1 | **End-to-End User Dashboard Exploration** | F1, F2, F3, F4, F5, F6 | High |
| 2 | **Portfolio Navigation & Detail Load** | F8, F9 | Medium |
| 3 | **Responsive Mockup & Media Verification** | F6, F9, F10 | Medium |
| 4 | **Dashboard Filtering & Data Integrity** | F1, F4, F5 | High |
| 5 | **Deployment Verification Workflow** | F7 | Low |

## Coverage Thresholds
- **Tier 1 (Feature Coverage)**: ≥5 test cases per feature (Total: 50 test cases)
- **Tier 2 (Boundary & Corner cases)**: ≥5 test cases per feature (Total: 50 test cases)
- **Tier 3 (Cross-Feature Combinations)**: ≥10 test cases covering feature interactions
- **Tier 4 (Real-World Application Scenarios)**: ≥5 test cases representing actual user flows
- **Total Minimum**: 115 test cases
