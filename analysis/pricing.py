import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def render_pricing(df):
    st.subheader("Price per person & reviews")

    required = {"price", "accommodates", "review_scores_rating"}
    if not required.issubset(df.columns):
        st.warning("Missing required columns")
        return

    df = df[df.accommodates > 0].copy()
    df["price_per_person"] = df.price / df.accommodates

    median_pp = df.price_per_person.median()

    col1, col2 = st.columns(2)
    col1.metric("Median €/person", f"{median_pp:.2f}")
    col2.metric("Target (+5%)", f"{median_pp*1.05:.2f}")

    fig, ax = plt.subplots()
    sns.scatterplot(
        data=df,
        x="price_per_person",
        y="review_scores_rating",
        alpha=0.4,
        ax=ax
    )
    ax.axhline(4.7, linestyle="--")
    ax.set_xlabel("€ per person")
    ax.set_ylabel("Rating")
    st.pyplot(fig)
