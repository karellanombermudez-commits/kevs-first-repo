# Data contract: `data/processed/clean.parquet`

Change this file only by pull request. `tests/test_contracts.py` enforces it,
and `SCHEMA` in `src/data/make_dataset.py` must match.

| column      | type     | description                          | allowed values / range |
|-------------|----------|--------------------------------------|------------------------|
| id          | int64    | unique row id                        | ≥ 0                    |
| feature_1   | float64  | (describe)                           |                        |
| feature_2   | float64  | (describe)                           |                        |
| category    | category | (describe)                           | a, b, c                |
| target      | int64    | label the model predicts             | 0, 1                   |

Missing values: none allowed after cleaning.
Row grain: one row per ___.
Source: `data/raw/*.csv` from ___ (date pulled: ___).
