import streamlit as st

def apply_filters(df):
    st.sidebar.header("Filters")

    if "accommodates" in df.columns:
        mn, mx = int(df.accommodates.min()), int(df.accommodates.max())
        cap = st.sidebar.slider("Capacity", mn, mx, (mn, mx))
        df = df[df.accommodates.between(*cap)]

    if "price" in df.columns:
        pmin, pmax = int(df.price.min()), int(df.price.quantile(0.95))
        price = st.sidebar.slider("Price (€)", pmin, pmax, (pmin, pmax))
        df = df[df.price.between(*price)]

    if "room_type" in df.columns:
        rooms = df.room_type.dropna().unique()
        selected = st.sidebar.multiselect("Room type", rooms, rooms)
        df = df[df.room_type.isin(selected)]

    if "neighbourhood" in df.columns:
        neigh = df.neighbourhood.dropna().unique()
        selected = st.sidebar.multiselect("Neighbourhood", neigh, neigh)
        df = df[df.neighbourhood.isin(selected)]

    return df
