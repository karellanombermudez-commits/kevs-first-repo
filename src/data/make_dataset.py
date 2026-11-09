"""raw/ -> processed/clean.parquet

The output must match data/schema.md exactly. Run `make data`, or
`make fake-data` to write a schema-correct dummy file so the model and app
teams can start before real data is ready.
"""
import argparse
import numpy as np
import pandas as pd
from src.config import RAW, CLEAN_PATH, SEED

# Mirror data/schema.md here. Tests check that the parquet matches this.
SCHEMA = {
    "id": "int64",
    "feature_1": "float64",
    "feature_2": "float64",
    "category": "category",
    "target": "int64",
}


def make_fake(n: int = 500) -> pd.DataFrame:
    rng = np.random.default_rng(SEED)
    df = pd.DataFrame({
        "id": np.arange(n),
        "feature_1": rng.normal(size=n),
        "feature_2": rng.normal(size=n),
        "category": rng.choice(["a", "b", "c"], size=n),
        "target": rng.integers(0, 2, size=n),
    })
    return df.astype(SCHEMA)


def clean(raw: pd.DataFrame) -> pd.DataFrame:
    """Put real cleaning logic here. Keep it pure: DataFrame in, DataFrame out."""
    df = raw.copy()
    # ... drop duplicates, fix types, handle missing values ...
    return df.astype(SCHEMA)


def main(fake: bool = False) -> None:
    if fake:
        df = make_fake()
    else:
        files = sorted(RAW.glob("*.csv")) + sorted(RAW.glob("*.parquet"))
        if not files:
            raise SystemExit(f"No raw files in {RAW}. Use --fake for a dummy dataset.")
        frames = [pd.read_parquet(f) if f.suffix == ".parquet" else pd.read_csv(f) for f in files]
        df = clean(pd.concat(frames, ignore_index=True))
    df.to_parquet(CLEAN_PATH, index=False)
    print(f"wrote {CLEAN_PATH}  shape={df.shape}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fake", action="store_true")
    main(**vars(ap.parse_args()))
