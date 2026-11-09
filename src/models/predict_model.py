"""Contract 2: predict(df) -> df

The app and the API import ONLY this. If no trained model exists yet it
falls back to random predictions so the frontend team is never blocked.
"""
import json
import numpy as np
import pandas as pd
import joblib

from src.config import MODEL_DIR, SEED
from src.features.build_features import build_features

_MODEL = None
_COLS = None


def _load():
    global _MODEL, _COLS
    path = MODEL_DIR / "model.joblib"
    if path.exists():
        _MODEL = joblib.load(path)
        _COLS = json.loads((MODEL_DIR / "columns.json").read_text())
    return _MODEL


def predict(df: pd.DataFrame) -> pd.DataFrame:
    """Input: rows matching data/schema.md (target optional).
    Output: same index with columns ['prediction', 'probability']."""
    out = pd.DataFrame(index=df.index)
    model = _MODEL or _load()
    if model is None:                       # STUB: no model trained yet
        rng = np.random.default_rng(SEED)
        out["probability"] = rng.random(len(df))
        out["prediction"] = (out["probability"] > 0.5).astype(int)
        out.attrs["stub"] = True
        return out
    X = build_features(df).reindex(columns=_COLS, fill_value=0.0)
    out["probability"] = model.predict_proba(X)[:, 1]
    out["prediction"] = model.predict(X)
    return out


if __name__ == "__main__":
    from src.config import CLEAN_PATH
    print(predict(pd.read_parquet(CLEAN_PATH).head()))
