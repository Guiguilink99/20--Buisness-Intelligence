import streamlit as st

def render_overview(df):
    st.subheader("Dataset overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Listings", len(df))
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing values", df.isna().sum().sum())

    st.markdown("### Missing values (%)")
    missing = (df.isna().mean() * 100).sort_values(ascending=False)
    st.dataframe(missing.to_frame("Missing %"))

    st.markdown("### Numeric summary")
    st.dataframe(df.describe())
