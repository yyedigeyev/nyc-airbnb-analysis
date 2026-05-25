import streamlit as st
import pandas as pd

st.title("NYC Airbnb Listings Analysis")

pdf = spark.sql("SELECT * FROM airbnb_clean").toPandas()

borough = st.sidebar.selectbox(
    "Select Borough",
    sorted(pdf["neighbourhood_group"].unique())
)

filtered = pdf[pdf["neighbourhood_group"] == borough]

st.subheader(f"{borough} Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Listings", len(filtered))

col2.metric(
    "Avg Reviews/Month",
    round(filtered["reviews_pm_clean"].mean(), 2)
)

col3.metric(
    "Avg Availability",
    round(filtered["availability_365"].mean(), 0)
)

reviews_chart = (
    filtered.groupby("neighbourhood")["reviews_pm_clean"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(reviews_chart)

room_counts = filtered["room_type"].value_counts()

st.bar_chart(room_counts)

st.dataframe(filtered.head(50))
