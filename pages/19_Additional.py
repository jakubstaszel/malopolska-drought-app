import streamlit as st
import altair as alt
import pandas as pd

from imagery.stats import (
    get_normalized_means_before_after,
    get_normalized_means_periods,
)

st.subheader("Observed Changes from 2022")
st.write("Compared to previous years (2018 - 2021)")
st.write(
    "Before creating the charts, each index was normalized separately, resulting in values ranging from 0 to 1. Additionally, except for MSI, NMDI, and NDWI v2, there was a sign change, so in every case a higher value indicates a more intense drought."
)
st.write(
    "Average values for indexes for two periods: 2018 - 2021 and 2022 - 2023. In the table averages' changes in %."
)
row3_col1, row3_col2 = st.columns([1, 4])
with row3_col1:
    data = get_normalized_means_before_after()
    before = data[data["Date"] == "1 - Before 2022-01"]
    after = data[data["Date"] == "2 - After 2022-01"]
    before["After - Value"] = list(after["Average Index Value"])
    before["% Change"] = before["After - Value"] / before["Average Index Value"] * 100
    before = before.set_index("Index")
    st.table(before["% Change"])
with row3_col2:
    st.altair_chart(
        alt.Chart(get_normalized_means_before_after())
        .mark_bar()
        .encode(x="Date:O", y="Average Index Value:Q", color="Date:N", column="Index:N")
    )

st.subheader("Observed Changes Over the Months")
st.write(
    "Average values for indexes for different periods. In the table average value for all indexes."
)
row4_col1, row4_col2 = st.columns([1, 7])
with row4_col1:
    data = get_normalized_means_periods()
    p1 = list(data[data["Period"] == "P1"]["Average Index Value"])
    p2 = list(data[data["Period"] == "P2"]["Average Index Value"])
    p3 = list(data[data["Period"] == "P3"]["Average Index Value"])
    p4 = list(data[data["Period"] == "P4"]["Average Index Value"])
    for_df = [
        {"1": "P1", "Period": sum(p1) / len(p1)},
        {"1": "P2", "Period": sum(p2) / len(p2)},
        {"1": "P3", "Period": sum(p3) / len(p3)},
        {"1": "P4", "Period": sum(p4) / len(p4)},
    ]
    # before = before.set_index('Index')
    st.table(pd.DataFrame(for_df).set_index("1"))
with row4_col2:
    st.altair_chart(
        alt.Chart(get_normalized_means_periods())
        .mark_bar()
        .encode(
            x="Period:O", y="Average Index Value:Q", color="Period:N", column="Index:N"
        )
    )
