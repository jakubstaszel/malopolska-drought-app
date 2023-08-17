import streamlit as st

from imagery.stats import get_means_normalized


st.cache_data(ttl=3600)


def get_means_normalized_cache():
    return get_means_normalized()


st.title("Dependencies Between Indexes")

st.write(
    "Before creating the charts, each index was normalized separately, resulting in values ranging from 0 to 1. Additionally, except for MSI, NMDI, and NDWI v2, there was a sign change, so in every case a higher value indicates a more intense drought."
)

first_key = get_means_normalized_cache().keys()[0]
# options = list(get_means_normalized_cache()[first_key].keys())
# selected = st.multiselect("Indexes to be displayed", options, options)
# st.line_chart(get_means_normalized_cache()[selected])

st.subheader("All Indexes")
list_with_indexes = list(get_means_normalized_cache().keys())
chosen_indexes = st.multiselect(
    label="Choose visible indexes:",
    options=list_with_indexes,
    default=list_with_indexes,
)
st.line_chart(get_means_normalized_cache()[chosen_indexes])
st.subheader("Indexes Based on NIR and SWIR")
st.line_chart(get_means_normalized_cache()[["ndwi1", "nmdi", "ndmi", "msi"]])
st.subheader("Indexes Based on NIR and Red")
st.line_chart(get_means_normalized_cache()[["ndvi", "wdrvi", "msavi2"]])
st.subheader("Other Indexes")
st.line_chart(get_means_normalized_cache()[["ndwi2", "evi"]])

st.subheader("Indexes in Different Periods")
data = get_means_normalized_cache()
list_with_indexes_2 = list(data.keys())
chosen_indexes_2 = st.multiselect(
    label="Choose visible indexes:",
    options=list_with_indexes_2,
    default=list_with_indexes_2,
    key="choose_v2",
)
row1_col1, row1_col2 = st.columns([1, 1])
row2_col1, row2_col2 = st.columns([1, 1])
with row1_col1:
    st.subheader("Period 1 - end of March and April")
    period1 = [
        "2018-04-20",
        "2019-03-31",
        "2020-04-09",
        "2021-04-09",
        "2022-03-25",
        "2023-04-23",
    ]
    data_period1 = data[data.index.isin(period1)]
    st.line_chart(data_period1[chosen_indexes_2])
with row1_col2:
    st.subheader("Period 2 - June")
    period2 = [
        "2018-06-19",
        "2019-06-09",
        "2020-06-13",
        "2021-06-18",
        "2022-06-03",
        "2023-06-03",
    ]
    data_period2 = data[data.index.isin(period2)]
    st.line_chart(data_period2[chosen_indexes_2])
with row2_col1:
    st.subheader("Period 3 - end of August and beginning of September")
    period3 = ["2018-08-23", "2019-08-28", "2020-08-22", "2021-09-06", "2022-08-27"]
    data_period3 = data[data.index.isin(period3)]
    st.line_chart(data_period3[chosen_indexes_2])
with row2_col2:
    st.subheader("Period 4 - end of October and November")
    period4 = ["2018-11-06", "2019-10-27", "2020-11-25", "2021-10-31", "2022-10-31"]
    data_period4 = data[data.index.isin(period4)]
    st.line_chart(data_period4[chosen_indexes_2])
