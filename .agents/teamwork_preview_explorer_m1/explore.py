import pandas as pd
import os
import json

path = r"D:\Twitter Scrape\IPU144_sentiment_analysis\Indonesia"

files = [
    "clean_ipu.csv",
    "translation_ipu.csv",
    "classification_ipu_sentiment.csv"
]

for f in files:
    full_path = os.path.join(path, f)
    if os.path.exists(full_path):
        print(f"=== {f} ===")
        try:
            df = pd.read_csv(full_path)
            print("Shape:", df.shape)
            print("Columns:", list(df.columns))
            print("Head:")
            print(df.head(2))
            print("-" * 40)
        except Exception as e:
            print("Error:", e)
    else:
        print(f"File {f} does not exist")
