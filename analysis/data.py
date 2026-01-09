import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path="cleaned_dataset.csv"):
    df = pd.read_csv(path)

    # Normalize column names
    df.columns = df.columns.str.lower()

    # Convert price if needed
    if "price" in df.columns and df["price"].dtype == object:
        df["price"] = (
            df["price"]
            .str.replace("€", "", regex=False)
            .str.replace(",", "", regex=False)
            .astype(float)
        )

    return df
