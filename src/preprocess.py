import pandas as pd

def load_and_clean(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    return df.dropna()
