from src.preprocess import load_and_clean
from sklearn.linear_model import LogisticRegression

def main():
    df = load_and_clean("data/sample.csv")

    X = df[["age", "income"]]
    y = df["label"]

    model = LogisticRegression()
    model.fit(X, y)

    acc = model.score(X, y)
    print(f"Training Accuracy: {acc:.4f}")

if __name__ == "__main__":
    main()
