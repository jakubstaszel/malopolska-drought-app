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

st.subheader("All indexes")
list_with_indexes = list(get_means_normalized_cache().keys())
chosen_indexes = st.multiselect(label="Choose visible indexes:", options=list_with_indexes, default=list_with_indexes)
st.line_chart(get_means_normalized_cache()[chosen_indexes])
st.subheader("Indexes based on NIR and SWIR")
st.line_chart(get_means_normalized_cache()[["ndwi1", "nmdi", "ndmi", "msi"]])
st.subheader("Indexes based on NIR and Red")
st.line_chart(get_means_normalized_cache()[["ndvi", "wdrvi", "msavi2"]])
st.subheader("Other indexes")
st.line_chart(get_means_normalized_cache()[["ndwi2", "evi"]])
