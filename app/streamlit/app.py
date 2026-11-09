"""Streamlit dashboard. Run: make app

Imports only predict() (Contract 2) and the processed parquet (Contract 1),
so it can be built with `make fake-data` before the real model exists.
"""
import pandas as pd
import streamlit as st
from src.config import CLEAN_PATH
from src.models.predict_model import predict

st.set_page_config(page_title="Project Dashboard", layout="wide")
st.title("Project Dashboard")


@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_parquet(CLEAN_PATH)


df = load_data()
preds = predict(df)
if preds.attrs.get("stub"):
    st.warning("Showing STUB predictions — no trained model in models/latest/ yet.")

col1, col2, col3 = st.columns(3)
col1.metric("Rows", len(df))
col2.metric("Positive rate (actual)", f"{df['target'].mean():.1%}")
col3.metric("Positive rate (predicted)", f"{preds['prediction'].mean():.1%}")

st.subheader("Data")
st.dataframe(df.join(preds).head(200), use_container_width=True)

st.subheader("Probability distribution")
st.bar_chart(preds["probability"].round(1).value_counts().sort_index())
