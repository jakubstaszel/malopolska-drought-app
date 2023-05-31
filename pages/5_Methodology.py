import streamlit as st

from imagery.stats import get_means_normalized


st.cache_data(ttl=3600)
def get_means_normalized_cache():
    return get_means_normalized()


st.title("Satellite Imagery Technologies Behind Drought Monitoring")

st.line_chart(get_means_normalized_cache())
