"""Train on processed data and save to models/latest/ (Contract 2).

Swap the sklearn estimator for anything — a PyTorch model saved via
src/models/deep_learning/ works the same as long as predict() can load it.
"""
import json
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from src.config import CLEAN_PATH, MODEL_DIR, SEED
from src.features.build_features import split_xy


def main() -> None:
    df = pd.read_parquet(CLEAN_PATH)
    X, y = split_xy(df)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=SEED)

    model = RandomForestClassifier(n_estimators=200, random_state=SEED)
    model.fit(Xtr, ytr)

    metrics = {"accuracy": float(accuracy_score(yte, model.predict(Xte)))}
    joblib.dump(model, MODEL_DIR / "model.joblib")
    (MODEL_DIR / "columns.json").write_text(json.dumps(list(X.columns)))
    (MODEL_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2))
    print(f"saved to {MODEL_DIR}  {metrics}")


if __name__ == "__main__":
    main()
