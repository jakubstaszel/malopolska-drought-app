from typing import Final

import streamlit as st
import leafmap.foliumap as leafmap

from imagery.colormaps import (
    get_colormap,
    get_legend_colormap,
    cdi_colormap,
    cdi_legend_colormap,
)
from imagery.imagery_files import get_available_layers, get_cdi_layers
from imagery.display_map import display_map_swipe_meteo

title: Final = "Validation using Combined Drought Indicator"


def get_layers_cache():
    return get_available_layers()


st.cache_data(ttl=3600)


def get_colormap_cache():
    return get_colormap()


st.cache_data(ttl=3600)


def get_legend_cache():
    return get_legend_colormap()


st.title(title)

st.write(
    "Combined Drought Indicator (CDI) - it was implemented in the European Drought Observatory (EDO) and is created by combination of three main traditional drought indicators:"
)
st.markdown("- Standardized Precipitation Index (SPI),")
st.markdown("- Soil Moisture Anomaly (SMA),")
st.markdown(
    "- Fraction of Absorbed Photosynthetically Active Radiation Anomaly (FAPAR Anomaly)."
)

if not "map_secrets" in st.session_state:
    st.session_state["map_secrets"] = {"coords": [49.8663, 20.1654], "zoom": 9}
    st.session_state["map_secrets_new"] = st.session_state.map_secrets

if not "index_for_compare" in st.session_state:
    st.session_state["index_for_compare"] = list(get_available_layers().keys())[0]
if not "meteo" in st.session_state:
    st.session_state["meteo"] = "cdi"

available_layers = get_layers_cache()[st.session_state.index_for_compare]
layers = list(available_layers.keys())

if not "date" in st.session_state:
    st.session_state["date"] = layers[len(layers) - 1]

with st.form("compare_map_form"):
    row1_col1, row1_col2, row1_col3 = st.columns([1, 1, 1])
    with row1_col1:
        st.session_state["index_for_compare"] = st.selectbox(
            label="Choose satellite-derived index",
            options=get_available_layers().keys(),
            index=0,
        )

    with row1_col2:
        meteo_indexes = ["cdi"]
        st.session_state["meteo"] = st.selectbox(
            label="Choose alternative drought index",
            options=meteo_indexes,
            index=0,
        )
    with row1_col3:
        st.session_state["date"] = st.selectbox(
            label="Choose date",
            options=layers,
            index=len(layers) - 1,
        )
    generate = st.form_submit_button("Generate")
    if generate:
        row2_col1, row2_col2 = st.columns([7, 1])
        with row2_col1:
            map_var_name = f"map_{st.session_state.index_for_compare}_{st.session_state.meteo}_{st.session_state.date}"
            map = display_map_swipe_meteo(
                st.session_state.map_secrets,
                st.session_state.index_for_compare + "_" + st.session_state.date,
                st.session_state.meteo + "_" + st.session_state.date,
                available_layers[st.session_state.date],
                get_cdi_layers()[st.session_state.date],
                get_colormap_cache()[st.session_state.index_for_compare],
                cdi_colormap(),
                map_var_name,
            )

        if "center" in map:
            st.session_state["map_secrets_new"] = {
                "coords": [map["center"]["lat"], map["center"]["lng"]],
                "zoom": map["zoom"],
            }

        st.write(
            "TVR - Temporary Vegetation Recovery, TSMR - Temporary Soil Moisture Recovery"
        )

        with row2_col2:
            st.write(f"For {st.session_state.index_for_compare}")
            legend1 = st.write(get_legend_cache()[st.session_state.index_for_compare])
            st.write(f"For {st.session_state.meteo}")
            legend2 = st.write(cdi_legend_colormap())
