"""processed/clean.parquet -> model matrix.

Keep this importable: predict_model.py calls the same function at inference
time so training and serving never drift.
"""
import pandas as pd

FEATURES = ["feature_1", "feature_2", "category"]
TARGET = "target"


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    X = df[FEATURES].copy()
    X = pd.get_dummies(X, columns=["category"], dtype=float)
    return X


def split_xy(df: pd.DataFrame):
    return build_features(df), df[TARGET]


if __name__ == "__main__":
    from src.config import CLEAN_PATH
    X = build_features(pd.read_parquet(CLEAN_PATH))
    print(X.head())
