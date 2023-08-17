import streamlit as st
import pandas as pd

from meteo.data import (
    get_avg_monthly_rainfall_whole_period,
    get_avg_yearly_rainfall_whole_period,
    get_avg_monthly_temp_whole_period,
    get_avg_yearly_temp_whole_period,
)

st.header("Meteorological Data Used to Evaluate Drought Indexes")
st.write(
    "Based on data provided by Polish Institute of Meteorology and Water Management - National Research Institute"
)
st.cache_data(ttl=3600)


def get_rainfall_whole_period_cache():
    return get_avg_monthly_rainfall_whole_period()


st.cache_data(ttl=3600)


def get_temp_monthly_whole_period_cache():
    return get_avg_monthly_temp_whole_period()


months_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
years_int = [2018, 2019, 2020, 2021, 2022, 2023]
months = st.multiselect(
    label="Choose visible months:", options=months_int, default=months_int
)
chosen_months = []
for year in years_int:
    for month in months:
        chosen_months.append(f"{year}-{month:02d}")
st.subheader(
    "Average Monthly and Annual Rainfall for Meteorological Stations in Małopolska Region"
)
row1_col1, row1_col2 = st.columns([3, 1])
with row1_col1:
    rainfall_whole = get_rainfall_whole_period_cache()
    st.bar_chart(rainfall_whole[rainfall_whole.index.isin(chosen_months)])
with row1_col2:
    st.bar_chart(get_avg_yearly_rainfall_whole_period())

st.subheader(
    "Average Monthly and Annual Temperature for Meteorological Stations in Małopolska Region"
)
row1_col1, row1_col2 = st.columns([3, 1])
with row1_col1:
    temp_whole = get_temp_monthly_whole_period_cache()
    st.bar_chart(temp_whole[temp_whole.index.isin(chosen_months)])
with row1_col2:
    st.bar_chart(get_avg_yearly_temp_whole_period())

data_periods = {
    "Period 1": [
        {"year": 2018, "Rainfall [mm]": 63.10},
        {"year": 2019, "Rainfall [mm]": 75.86},
        {"year": 2020, "Rainfall [mm]": 131.00},
        {"year": 2021, "Rainfall [mm]": 106.48},
        {"year": 2022, "Rainfall [mm]": 85.21},
        {"year": 2023, "Rainfall [mm]": 134.29},
    ],
    "Period 2": [
        {"year": 2018, "Rainfall [mm]": 232.87},
        {"year": 2019, "Rainfall [mm]": 228.51},
        {"year": 2020, "Rainfall [mm]": 345.96},
        {"year": 2021, "Rainfall [mm]": 202.83},
        {"year": 2022, "Rainfall [mm]": 103.24},
    ],
    "Period 3": [
        {"year": 2018, "Rainfall [mm]": 266.17},
        {"year": 2019, "Rainfall [mm]": 218.11},
        {"year": 2020, "Rainfall [mm]": 207.81},
        {"year": 2021, "Rainfall [mm]": 407.59},
        {"year": 2022, "Rainfall [mm]": 242.29},
    ],
    "Period 4": [
        {"year": 2018, "Rainfall [mm]": 132.88},
        {"year": 2019, "Rainfall [mm]": 135.74},
        {"year": 2020, "Rainfall [mm]": 260.66},
        {"year": 2021, "Rainfall [mm]": 113.03},
        {"year": 2022, "Rainfall [mm]": 173.06},
    ],
}

st.subheader(
    "Average Rainfall for Meteorological Stations in Małopolska Region for Different Periods"
)
st.markdown(
    """- Period 1 - February and March
- Period 2 - May and June
- Period 3 - July and August
- Period 4 - September and October
"""
)
period = st.selectbox(
    "Choose period:", ["Period 1", "Period 2", "Period 3", "Period 4"]
)
st.subheader(period)
st.bar_chart(pd.DataFrame.from_dict(data_periods[period]).set_index("year"))
