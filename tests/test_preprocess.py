from src.preprocess import load_and_clean

def test_preprocess_removes_missing_values():
    df = load_and_clean("data/sample.csv")
    assert not df.empty
    assert df.isna().sum().sum() == 0
