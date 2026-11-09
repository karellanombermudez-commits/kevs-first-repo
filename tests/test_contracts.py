"""Guards the two team contracts. Runs in CI on every PR."""
import pandas as pd
from src.data.make_dataset import make_fake, SCHEMA
from src.models.predict_model import predict


def test_schema_matches_fake_data():
    df = make_fake(20)
    assert list(df.columns) == list(SCHEMA)
    for c, t in SCHEMA.items():
        assert str(df[c].dtype) == t, f"{c}: {df[c].dtype} != {t}"


def test_predict_contract():
    df = make_fake(10)
    out = predict(df)
    assert list(out.columns) == ["probability", "prediction"]
    assert len(out) == len(df)
    assert out["prediction"].isin([0, 1]).all()
