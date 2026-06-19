# Sentiment Analysis Exploration Report: IPU 144 (Indonesia)

This report details the findings and data extracted from the sentiment analysis pipeline implemented in the Indonesian Twitter scraping project located at `D:\Twitter Scrape\IPU144_sentiment_analysis\Indonesia\`.

---

## 1. Sentiment Distribution / Label Counts

The sentiment classification of the scraped tweets was conducted using the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** lexicon sentiment analysis library on the English-translated versions of the tweets. The compound scores were mapped to three sentiment categories:
- **Positive (Positif)**: $\text{Compound Score} > 0$
- **Neutral (Netral)**: $\text{Compound Score} = 0$
- **Negative (Negatif)**: $\text{Compound Score} < 0$

Based on the raw data in `classification_ipu_sentiment.csv` and the cell 71 output of `twitter scrape_indo.ipynb`, the sentiment counts and percentages for the **346 unique tweets** are as follows:

| Sentiment Label | Label (Indonesian) | Total Count | Percentage (%) |
| :--- | :--- | :---: | :---: |
| **Positive** | Positif | 213 | 61.56% |
| **Negative** | Negatif | 83 | 23.99% |
| **Neutral** | Netral | 50 | 14.45% |
| **Total** | **Total** | **346** | **100.00%** |

---

## 2. Word Frequencies & Core Themes

The tokenization and stemming steps in `twitter scrape_indo.ipynb` utilize the Indonesian Sastrawi stemmer to clean and normalize raw Indonesian words (stored in `clean_ipu.csv`). A word cloud generation step (Cell 72) illustrates the most prominent terms. The following key terms represent the core discussion themes:

* **Event Identifiers & Host Location**:
  * `ipu`: Reference to the Inter-Parliamentary Union.
  * `indonesia` / `ri`: The host nation (Republic of Indonesia).
  * `bal`: Normalized stem for "Bali", specifically Nusa Dua, Bali, where the 144th assembly took place.
  * `maret`: The month of March, in which the event was staged.
  * `puan` / `puanmaharani`: Puan Maharani, the Speaker of the Indonesian House of Representatives (DPR RI) who hosted the assembly.
  * `dpr` / `dprri`: Dewan Perwakilan Rakyat (the Indonesian Parliament).

* **Assembly Theme ("Getting to Zero")**:
  * `zeroemission`: Cleaned term for "Zero Emission".
  * `stopclimatechange`: Theme-specific hashtag "Stop Climate Change".
  * `iklim` / `ubah`: Terms related to climate change.
  * `kerja` / `sama` (`kerjasama`): Focus on inter-parliamentary collaboration.
  * `parlemen` / `sidang`: Reference to the parliamentary sessions.

* **Geopolitical & Global Security Focus**:
  * `rusia` & `ukraina`: References to the Russia-Ukraine conflict, which became a prominent topic of discussion and the subject of proposed emergency resolution items (e.g., "emergency item", "peace task force", "diplomasi").
  * `damai`: Focus on peace and resolution.

---

## 3. Model Evaluation Metrics

* **Accuracy**: N/A
* **Precision**: N/A
* **Recall / Sensitivity**: N/A
* **F1-Score**: N/A
* **Confusion Matrix**: N/A

### Explanation:
The sentiment classification pipeline in `twitter scrape_indo.ipynb` is an **unsupervised, rule-based lexicon approach** (VADER Sentiment Intensity Analyzer). 
1. **No Supervised Model**: The notebook loads translations and calculates polarity scores directly without training a model or dividing data into train/test sets.
2. **No Ground Truth**: There are no manual, human-annotated ground-truth labels to evaluate the classification outputs against. 
3. **Impossibility of Calculation**: Consequently, standard evaluation metrics (accuracy, precision, recall, F1) and a confusion matrix are mathematically undefined and cannot be calculated for this dataset.

---

## 4. Sample Tweets with Predicted Labels

The table below shows illustrative samples from `classification_ipu_sentiment.csv` demonstrating how VADER classified translated tweets.

| Index | Cleaned Indonesian (from `clean_ipu.csv`) | English Translation (from `translation_ipu.csv`) | Predicted Sentiment | Compound Score |
| :---: | :--- | :--- | :---: | :---: |
| **2** | syukur sekarang makin banyak masyarakat gemar beli produk lokal bagai daerah ini bentuk gotong royong jadi ciri khas masyarakat indonesia ipu umkm wastranusantara solusipuan | thankfully, now more and more people like to buy local products, like this area, the form of gotong royong is a hallmark of the Indonesian people IPU UMKM Wastranusantara Solusipuan | **Positif** | `0.7951` |
| **3** | sejak awal sidang indonesia tekan penting peran sentral ipu cari solusi isu ukraina imbang depan hormat hukum internasional integritas daulat wilayah ipu zeroemission stopclimatechange | Since the beginning of the session, Indonesia has emphasized the importance of the central role of IPU in finding solutions to the issue of Ukraine, drawing a balance before respecting international law, territorial integrity and sovereignty, IPU, zero emission, stop climate change | **Positif** | `0.7783` |
| **4** | bahagia sekali rasa ikut toreh sejarah bangun komitmen kerja sama global atas ubah iklim upaya cipta suatu dunia sehat tenteram sejahtera ipu zeroemission stopclimatechange solusipuan | I am very happy to participate in making history, building a commitment to global cooperation on changing the climate, efforts to create a world, healthy, peaceful and prosperous, IPU zero emission stop climatechange, your solution | **Positif** | `0.9501` |
| **0** | international parliamentary union ipu selenggara nusa bal tanggal maret inidiplomasi indonesianway rintiskemajuan ipu ri | IPU International Parliamentary Union will be held in Nusa Bal this March | **Netral** | `0.0000` |
| **12** | indonesia satu agam dunia ipu | Indonesia is one religion in the world of Ipu | **Netral** | `0.0000` |
| **14** | tengah sidang ipu puan sampai duka atas jatuh pesawat china ipu puanmaharani ri | In the middle of the trial, Ipu Puan is saddened by the downing of the Chinese plane, Ipu Puanmaharani Ri | **Negatif** | `-0.5267` |
| **27** | live sidang inter parliamentary union nusa indonesia governing council assembly kamis maret ipu zeroemission stopclimatechange | live session inter parliamentary union nusa indonesia governing council assembly thursday march ipu zeroemission stop climatechange | **Negatif** | `-0.2960` |
| **53** | wakil ketua badan kerja sama antar parlemen bksap dpr ri mardani ali sera ungkap beberapa negara serta sidang ipu minta konflik rusia ukraina benar benar fokus bahas ipu zeroemission stopclimatechange | Deputy chairman of the inter-parliamentary cooperation body, BKSAP, DPR RI, mardani ali, sera, said several countries and the IPU session asked for the Russia-Ukraine conflict to really focus on discussing IPU Zeroemission Stop Climate Change | **Negatif** | `-0.5423` |
| **113** | ketua bksap dpr ri fadli zon sampai parlemen indonesia usul emergency item isi tawar jalan tengah dekat diplomasi libat peran parlemen atas konflik rusia ukraina ipu zeroemission stopclimatechange | Chairman of BKSAP DPR RI, Zon Fadli, to Indonesian Parliament, proposes emergency items, content of bargaining, middle ground, close diplomacy, involves parliament's role in conflict, Russia, Ukraine, IPU, zero emission, stop climate change | **Negatif** | `-0.7269` |

---

## 5. Date / Time Trend Data

* **Temporal Columns in CSVs**: None
* **Timestamp Metadata**: Absent from DataFrames and output CSV files.
* **Scraping Query**: `#IPU144 lang:id since:2021-01-01 until:2022-10-01`

### Analysis:
1. **Lack of Metadata**: The scraping routine in `Cell 42` appended only the tweet text (`tweet.content`) to the dataframe. Time metrics, date fields, or creation timestamps were omitted. Consequently, it is impossible to chart sentiment trends chronologically using the files.
2. **Contextual Trend Inference**: The 144th IPU Assembly was held from **March 20 to March 24, 2022** in Bali, Indonesia. This matches the extensive occurrences of the word "Maret" (March) and "20-24 maret" in the cleaned texts, showing that the vast majority of these tweets are concentrated around this 5-day event window.
