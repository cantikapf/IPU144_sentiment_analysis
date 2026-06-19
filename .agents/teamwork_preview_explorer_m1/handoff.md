# Handoff Report: IPU 144 Sentiment Analysis (Indonesia) Data Extraction

## 1. Observation
I observed the following files and code snippets in the workspace:
* **Directory Path**: `D:\Twitter Scrape\IPU144_sentiment_analysis\Indonesia\`
* **Target Files**:
  - `twitter scrape_indo.ipynb` (Jupyter Notebook, 684 KB)
  - `clean_ipu.csv` (Cleaned Indonesian tweets, 46.6 KB, 348 lines)
  - `translation_ipu.csv` (English translations, 56.7 KB, 348 lines)
  - `classification_ipu_sentiment.csv` (Sentiments classified, 61.7 KB, 348 lines)

* **Code and Execution Output in Jupyter Notebook**:
  - In cell 71 (`twitter scrape_indo.ipynb` at line 2636):
    ```
    The number of negative sentiments is:	 83
    The number of positive sentiments is:	 213
    The number of neutral sentiments is:	 50
    The overall total of sentiments is:	 346
    ```
  - In cell 42 (`twitter scrape_indo.ipynb` at line 40):
    ```python
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('#IPU144 lang:id since:2021-01-01 until:2022-10-01').get_items()):
        tweets_list2.append([tweet.content])
    ```
  - In cell 66 (`twitter scrape_indo.ipynb` at line 2439):
    ```python
    tweet_df.loc[tweet_df['Compound_Score'] < 0, 'Sentiments'] = 'Negatif'
    tweet_df.loc[tweet_df['Compound_Score'] == 0, 'Sentiments'] = 'Netral'
    tweet_df.loc[tweet_df['Compound_Score'] > 0, 'Sentiments'] = 'Positif'
    ```
  - In cell 64 (`twitter scrape_indo.ipynb` at line 2264):
    ```python
    scores = [analyser.polarity_scores(x) for x in tweet_df['Tweet']]
    ```

* **CSV Structures**:
  - `clean_ipu.csv` contains a single column labeled `Tweet` with tokenized, stemmed, and cleaned Indonesian words.
  - `translation_ipu.csv` contains a single column labeled `Tweet` with translated English text.
  - `classification_ipu_sentiment.csv` has three columns: `Tweet` (which contains the translated English text), `Compound_Score` (numeric float between -1.0 and 1.0), and `Sentiments` (values 'Positif', 'Negatif', or 'Netral').

## 2. Logic Chain
1. **Sentiment Distribution**:
   - The notebook output for cell 71 explicitly states that positive sentiments count is 213, negative is 83, and neutral is 50, with a total of 346.
   - I manually verified the counts in the 346 valid data rows of `classification_ipu_sentiment.csv` (excluding headers and empty trailing lines). Line-by-line counting confirmed exactly 50 "Netral" sentiments, 83 "Negatif" sentiments, and 213 "Positif" sentiments.
   - Calculating the percentages:
     * Positive: 61.56%
     * Negative: 23.99%
     * Neutral: 14.45%

2. **Word Frequencies**:
   - The cell 72 of `twitter scrape_indo.ipynb` uses Python's `wordcloud` library to generate a word cloud from the tweets.
   - By examining the text in `clean_ipu.csv` and tracking the raw frequency of terms, the most common keywords are `ipu` (the core topic), `zeroemission` & `stopclimatechange` (the assembly's theme), `indonesia` (the host), `bal` (Bali, the location), `parlemen` (parliament), `sidang` (session/assembly), `puan` (Puan Maharani), and the geopolitically focused `rusia` & `ukraina`.

3. **Model Evaluation Metrics**:
   - In cell 64 of the notebook, VADER (`SentimentIntensityAnalyzer`) is invoked on the English translation of the tweets. VADER is a rule-based lexicon sentiment analyzer.
   - Since VADER uses pre-defined sentiment scores for words, no model training occurred. There are no manual ground-truth labels in the dataset.
   - Therefore, standard supervised evaluation metrics (accuracy, precision, recall, F1-score) and confusion matrices are not available because no classification model was trained or compared against a validation set.

4. **Sentiment Trend over Time**:
   - The snscrape loop in cell 42 shows that only `[tweet.content]` was appended to the list and written to the CSVs.
   - Inspecting the header columns of all three CSV files confirms that no date, timestamp, or temporal fields were recorded.
   - Therefore, a direct time-series analysis is impossible from the raw files.
   - However, the contextual temporal window is known from the query parameters: the search retrieved tweets under the query `#IPU144 lang:id since:2021-01-01 until:2022-10-01`. The 144th IPU Assembly event itself took place between March 20 and March 24, 2022, in Nusa Dua, Bali, which aligns with the heavy occurrence of the word "Maret" (March) and "20-24 maret" in the cleaned text.

## 3. Caveats
- I assumed that the translation API `googletrans` translated the Indonesian text correctly, as the VADER analysis is based entirely on the translated English columns.
- The word frequencies were extracted based on manual checking of tokenized texts in `clean_ipu.csv` and notebook flow, as no explicit code cell output printed the exact numerical frequency of each word in the notebook.
- No direct chronological plots can be constructed due to the absence of date metadata in the scraped dataset.

## 4. Conclusion
* The sentiment distribution of the 346 Indonesian tweets shows a predominantly positive outlook (61.56%), with negative sentiments at 23.99% and neutral sentiments at 14.45%.
* The core focus of the tweets centers on parliamentary cooperation (`parlemen`, `kerjasama`), the climate change theme (`zeroemission`, `stopclimatechange`), the location and host (`indonesia`, `bal`, `puan`), and emergency discussions surrounding the Russia-Ukraine conflict (`rusia`, `ukraina`).
* VADER lexicon classifier was used without model training, meaning no evaluation metrics or confusion matrices are present.
* There is no temporal column in the dataset, but the context points to a peak in tweets around March 2022 during the active IPU 144 assembly dates.

## 5. Verification Method
1. **File Checks**:
   - Inspect the file `D:\PERSONAL PROJECT\IPU144-sentiment-viz\.agents\teamwork_preview_explorer_m1\extracted_data.json` to verify that all structured fields are populated and match the counts.
   - View `classification_ipu_sentiment.csv` to confirm the sentiment column labels ('Positif', 'Negatif', 'Netral') and compound scores.
