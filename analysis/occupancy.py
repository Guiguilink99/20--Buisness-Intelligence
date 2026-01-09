import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def render_occupancy(df):
    st.subheader("Occupancy – 2 to 4 people")

    if not {"accommodates", "availability_365"}.issubset(df.columns):
        st.warning("Missing required columns")
        return

    target = df[df.accommodates.between(2, 4)]
    occupancy = 1 - (target.availability_365 / 365)

    col1, col2 = st.columns(2)
    col1.metric("Current occupancy", f"{occupancy.mean()*100:.1f}%")
    col2.metric("Target", "80%")

    fig, ax = plt.subplots()
    sns.histplot(occupancy, bins=30, ax=ax)
    ax.axvline(0.8, linestyle="--")
    ax.set_xlabel("Occupancy rate")
    st.pyplot(fig)
