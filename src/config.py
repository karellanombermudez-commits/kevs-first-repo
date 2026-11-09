"""Single source of truth for paths and settings. Import this everywhere."""
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / os.getenv("DATA_DIR", "data")
RAW = DATA_DIR / "raw"
INTERIM = DATA_DIR / "interim"
PROCESSED = DATA_DIR / "processed"
CLEAN_PATH = PROCESSED / "clean.parquet"          # Contract 1
MODEL_DIR = ROOT / os.getenv("MODEL_DIR", "models/latest")   # Contract 2
REPORTS = ROOT / "reports"
FIGURES = REPORTS / "figures"
SEED = 42

for p in (RAW, INTERIM, PROCESSED, MODEL_DIR, FIGURES):
    p.mkdir(parents=True, exist_ok=True)
