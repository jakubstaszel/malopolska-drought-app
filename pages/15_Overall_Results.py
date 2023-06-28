import streamlit as st

from imagery.stats import get_means_normalized


st.cache_data(ttl=3600)
def get_means_normalized_cache():
    return get_means_normalized()

st.title("Overall Results")

st.write("Before creating the charts, each index was normalized separately, resulting in values ranging from 0 to 1. Additionally, except for MSI, NMDI, and NDWI v2, there was a sign change, so in every case a higher value indicates a more intense drought.")

first_key = get_means_normalized_cache().keys()[0]
print(first_key)
# options = list(get_means_normalized_cache()[first_key].keys())
# selected = st.multiselect("Indexes to be displayed", options, options)
# st.line_chart(get_means_normalized_cache()[selected])

st.write("Oparte na NIR i SWIR")
st.line_chart(get_means_normalized_cache()[['ndwi1', 'nmdi', 'ndmi', 'msi']])
st.write("Oparte na NIR i R")
st.line_chart(get_means_normalized_cache()[['ndvi', 'wdrvi', 'msavi2']])
st.write("Inne")
st.line_chart(get_means_normalized_cache()[['ndwi2', 'evi']])