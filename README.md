# NYC Airbnb Listings Analysis

## Project Overview

This project analyzes Airbnb listings in New York City using SQL, pandas, visualization libraries, and Streamlit in Databricks. The goal of the project is to explore patterns in Airbnb activity across boroughs, neighborhoods, and room types.

The project includes:
- Data cleaning
- SQL analysis
- Pandas analysis
- Data visualization
- Interactive Streamlit dashboard

---

## Dataset

Dataset: NYC Airbnb Listings

The dataset contains information about Airbnb properties in New York City, including:
- Listing name
- Borough
- Neighborhood
- Room type
- Price
- Availability
- Reviews
- Reviews per month

---

## Data Cleaning

Several cleaning steps were performed before analysis:

### 1. Duplicate Removal
Duplicate listings were removed using SQL window functions and `ROW_NUMBER()`.

### 2. NULL Handling
Missing values in `reviews_per_month` were replaced with `0` using `COALESCE()`.

### 3. Validation
The cleaned dataset was verified to ensure:
- Unique listing IDs
- No remaining NULL values in cleaned review columns

---

## SQL Analysis

The project includes multiple SQL analyses:

### Listings by Borough
Calculated the number of Airbnb listings in each NYC borough.

### Neighborhood Activity
Analyzed neighborhoods with the highest average reviews per month.

### Room Type Availability
Compared average yearly availability across different room types.

---

## Pandas Analysis

Pandas was used for additional analysis including:
- Grouping and aggregation
- Correlation analysis
- Data transformation

A correlation matrix was created to analyze relationships between:
- Availability
- Reviews per month

---

## Visualizations

The project includes visualizations such as:
- Bar charts of average reviews by borough
- Room type distribution charts
- Neighborhood activity comparisons

These visualizations help identify patterns and trends in Airbnb activity across NYC.

---

## Streamlit Dashboard

An interactive Streamlit dashboard was created with:
- Sidebar borough filter
- KPI metric cards
- Interactive charts
- Filtered listing tables

The dashboard allows users to explore Airbnb trends dynamically.

---

## Key Findings

- Manhattan had the highest concentration of Airbnb listings.
- Some neighborhoods showed significantly higher review activity than others.
- Entire homes and apartments tended to have lower availability, suggesting stronger demand.
- Airbnb activity varies substantially across boroughs and room types.

---

## Technologies Used

- SQL
- Python
- Pandas
- Matplotlib
- Streamlit
- Databricks

---

## Repository Contents

- `app.py` — Streamlit dashboard application
- `airbnb_clean.csv` — cleaned dataset
- Notebook with SQL, pandas, and visualizations
- README documentation

---

## Author

Final Project for Week 9 — Advanced SQL and Databricks Applications
