import streamlit as st
import pandas as pd

st.title("NYC Airbnb Listings Analysis")

# Load CSV
pdf = pd.read_csv("airbnb_clean.csv")

# Sidebar filter
boroughs = (
    pdf["neighbourhood_group"]
    .dropna()
    .astype(str)
    .unique()
)

borough = st.sidebar.selectbox(
    "Select Borough",
    sorted(boroughs)
)

# Filter data
filtered = pdf[pdf["neighbourhood_group"] == borough]

# Metrics
st.subheader(f"{borough} Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Listings",
    len(filtered)
)

col2.metric(
    "Avg Reviews/Month",
    round(filtered["reviews_pm_clean"].mean(), 2)
)

col3.metric(
    "Avg Availability",
    round(filtered["availability_365"].mean(), 0)
)

# Chart 1
st.subheader("Top Neighborhoods by Reviews")

reviews_chart = (
    filtered.groupby("neighbourhood")["reviews_pm_clean"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(reviews_chart)

# Chart 2
st.subheader("Room Type Distribution")

room_counts = filtered["room_type"].value_counts()

st.bar_chart(room_counts)

# Table
st.subheader("Sample Listings")

st.dataframe(filtered.head(50))
