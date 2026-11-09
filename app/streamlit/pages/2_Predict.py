import streamlit as st
import pandas as pd
from src.models.predict_model import predict

st.title("Predict")
st.write("Upload a CSV with the columns in data/schema.md")
up = st.file_uploader("CSV", type="csv")
if up:
    df = pd.read_csv(up)
    out = predict(df)
    st.dataframe(df.join(out))
    st.download_button("Download predictions", out.to_csv(index=False), "predictions.csv")
