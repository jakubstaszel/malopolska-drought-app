import streamlit as st

from imagery.stats import get_means_normalized


st.cache_data(ttl=3600)


def get_means_normalized_cache():
    return get_means_normalized()


st.title("Overall Results")

st.write(
    "Before creating the charts, each index was normalized separately, resulting in values ranging from 0 to 1. Additionally, except for MSI, NMDI, and NDWI v2, there was a sign change, so in every case a higher value indicates a more intense drought."
)

first_key = get_means_normalized_cache().keys()[0]
# options = list(get_means_normalized_cache()[first_key].keys())
# selected = st.multiselect("Indexes to be displayed", options, options)
# st.line_chart(get_means_normalized_cache()[selected])

st.header("Validation using Combined Drought Indicator")
st.write(
    "To validate the obtained results, the Combined Drought Indicator (CDI) was used. It was implemented in the European Drought Observatory (EDO) and is created by combination of three main traditional drought indicators:"
)
st.markdown("- Standardized Precipitation Index (SPI),")
st.markdown("- Soil Moisture Anomaly (SMA),")
st.markdown(
    "- Fraction of Absorbed Photosynthetically Active Radiation Anomaly (FAPAR Anomaly)."
)
st.subheader("NMDI and CDI Warning or Alert Class Share Across Time")
st.write(
    "CDI Warning or Alert Class Share - calculated as a share of pixels for Małopolska region that have values 1 or 2, meaning that they were classified as Warning or Alert."
)
data = get_means_normalized_cache()[["nmdi"]]
data["CDI Warning or Alert class share"] = [
    0.724960254372019,
    0.8441971383147854,
    0.2988871224165342,
    0.8744038155802861,
    0.7758346581875993,
    0.15421303656597773,
    0.4069952305246423,
    0.5135135135135135,
    0.9014308426073132,
    0.5230524642289348,
    0.492845786963434,
    0.0,
    0.02066772655007949,
    0.8235294117647058,
    0.1287758346581876,
    0.2718600953895072,
    0.7583465818759937,
    0.8426073131955485,
    0.6073131955484896,
    0.09220985691573927,
    0.012718600953895072,
    0.4944356120826709,
]
data["testowe"] = [
    0.13990857016276603,
    0.053164892734017526,
    0.11922936143273741,
    0.10469643959275568,
    0.25923548889301024,
    0.06015207986343365,
    0.10867015724313134,
    0.1163725618401091,
    0.18703635126006715,
    0.053829228381561796,
    0.09450397669236095,
    0.1379678454669266,
    0.2745727746755356,
    0.06472882983179512,
    0.0771058263104008,
    0.14468811068170984,
    0.9657739090354843,
    0.20145193275759685,
    0.3415961053579793,
    0.7841668298322721,
    0.6902790728800099,
    0.22830149297714955,
]
st.line_chart(data[["CDI Warning or Alert class share", "testowe"]])

st.header("Comparision between indexes")
st.subheader("All indexes")
st.line_chart(get_means_normalized_cache())
st.subheader("Indexes based on NIR and SWIR")
st.line_chart(get_means_normalized_cache()[["ndwi1", "nmdi", "ndmi", "msi"]])
st.subheader("Indexes based on NIR and Red")
st.line_chart(get_means_normalized_cache()[["ndvi", "wdrvi", "msavi2"]])
st.subheader("Other indexes")
st.line_chart(get_means_normalized_cache()[["ndwi2", "evi"]])
