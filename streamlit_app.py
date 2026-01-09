import streamlit as st

from analysis.data import load_data
from analysis.filters import apply_filters
from analysis.overview import render_overview
from analysis.occupancy import render_occupancy
from analysis.pricing import render_pricing
from analysis.amenities import render_amenities

st.set_page_config(page_title="Airbnb Dashboard", layout="wide")
st.title("🏠 Airbnb Analytics Dashboard")

df = load_data()
df = apply_filters(df)

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "🏠 Occupancy",
    "💰 Pricing",
    "🛋️ Amenities"
])

with tab1:
    render_overview(df)

with tab2:
    render_occupancy(df)

with tab3:
    render_pricing(df)

with tab4:
    render_amenities(df)
