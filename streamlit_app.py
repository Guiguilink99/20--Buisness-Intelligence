import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------
# App config
# -----------------------
st.set_page_config(
    page_title="Airbnb Data Analysis",
    layout="wide"
)

st.title("🏠 Airbnb Data Analysis Dashboard")

# -----------------------
# Data loading
# -----------------------
@st.cache_data
def load_data():
    df = pd.read_csv("airbnb_tp.csv")
    return df

df = load_data()

st.sidebar.header("Filters")

# -----------------------
# Example filters (adapt to your columns)
# -----------------------
if "neighbourhood" in df.columns:
    neighbourhoods = sorted(df["neighbourhood"].dropna().unique())
    selected_neigh = st.sidebar.multiselect(
        "Neighbourhood",
        neighbourhoods,
        default=neighbourhoods
    )
    df = df[df["neighbourhood"].isin(selected_neigh)]

if "room_type" in df.columns:
    room_types = df["room_type"].dropna().unique()
    selected_room = st.sidebar.multiselect(
        "Room type",
        room_types,
        default=room_types
    )
    df = df[df["room_type"].isin(selected_room)]

# -----------------------
# KPIs
# -----------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Listings", len(df))

with col2:
    if "price" in df.columns:
        st.metric("Avg price", f"${df['price'].mean():.2f}")

with col3:
    if "minimum_nights" in df.columns:
        st.metric("Avg min nights", f"{df['minimum_nights'].mean():.1f}")

with col4:
    if "availability_365" in df.columns:
        st.metric("Avg availability", f"{df['availability_365'].mean():.0f}")

# -----------------------
# Tabs for plots
# -----------------------
tab1, tab2, tab3 = st.tabs(["📊 Distributions", "🗺️ Location", "📈 Correlations"])

# -----------------------
# Tab 1 — Distributions
# -----------------------
with tab1:
    st.subheader("Price distribution")

    if "price" in df.columns:
        fig, ax = plt.subplots()
        sns.histplot(df["price"], bins=50, kde=True, ax=ax)
        ax.set_xlabel("Price")
        ax.set_ylabel("Count")
        st.pyplot(fig)

# -----------------------
# Tab 2 — Location
# -----------------------
with tab2:
    st.subheader("Listings by neighbourhood")

    if "neighbourhood" in df.columns:
        fig, ax = plt.subplots(figsize=(10, 5))
        df["neighbourhood"].value_counts().head(20).plot(
            kind="bar", ax=ax
        )
        ax.set_ylabel("Listings")
        ax.set_xlabel("")
        st.pyplot(fig)

# -----------------------
# Tab 3 — Correlations
# -----------------------
with tab3:
    st.subheader("Correlation heatmap")

    numeric_df = df.select_dtypes(include="number")

    if len(numeric_df.columns) > 1:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(
            numeric_df.corr(),
            cmap="coolwarm",
            center=0,
            ax=ax
        )
