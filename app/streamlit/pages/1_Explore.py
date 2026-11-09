import streamlit as st
import pandas as pd
from src.config import CLEAN_PATH

st.title("Explore")
df = pd.read_parquet(CLEAN_PATH)
col = st.selectbox("Column", df.select_dtypes("number").columns)
st.line_chart(df[col])
