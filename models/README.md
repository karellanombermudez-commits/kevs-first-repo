Trained artifacts live in `models/latest/` and are git-ignored.

Share them one of two ways:
- **DVC**: `dvc init && dvc add models/latest && git commit` — then `dvc push` to a Drive/S3 remote.
- **Simple**: upload the folder to shared Drive; `make train` regenerates it locally.

Files predict() expects in `models/latest/`:
- `model.joblib` (sklearn) **or** `model.pt` (torch)
- `columns.json` — feature column order
- `metrics.json`
