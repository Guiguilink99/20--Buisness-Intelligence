import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def render_amenities(df):
    st.subheader("Amenities analysis")

    if "amenities" not in df.columns:
        st.warning("Missing amenities column")
        return

    df = df.copy()
    df["amenities_count"] = df.amenities.str.count(",") + 1

    low_pct = (df.amenities_count < 20).mean() * 100

    col1, col2 = st.columns(2)
    col1.metric("< 20 amenities", f"{low_pct:.1f}%")
    col2.metric("Target", "< 25%")

    fig, ax = plt.subplots()
    sns.histplot(df.amenities_count, bins=30, ax=ax)
    ax.axvline(20, linestyle="--")
    ax.set_xlabel("Amenities count")
    st.pyplot(fig)
