from typing import Final

import streamlit as st
import leafmap.foliumap as leafmap

from imagery.colormaps import get_colormap, get_legend_colormap
from imagery.imagery_files import get_available_layers
from imagery.display_map import display_map
from imagery.stats import get_stats

index: Final = "msi"
title: Final = "Moisture Stress Index"
index_name: Final = "MSI"

@st.cache_data
def get_stats_cache():
    return get_stats()


@st.cache_data
def get_layers_cache():
    return get_available_layers()


@st.cache_data
def get_colormap_cache():
    return get_colormap()


@st.cache_data
def get_legend_cache():
    return get_legend_colormap()


st.title(title)

st.write(
    "MSI can be utilized for assessing soil moisture during drought conditions and serves as a reliable indicator for agricultural drought. It ranges from 0 to 4. As the index value increases, the level of water stress associated with drought also increases."
)
st.subheader(f"{index_name} Statistics Across Time")
st.line_chart(get_stats_cache()[index])

if not "map_secrets" in st.session_state:
    st.session_state["map_secrets"] = {"coords": [49.8663, 20.1654], "zoom": 9}
    st.session_state["map_secrets_new"] = st.session_state.map_secrets

available_layers = get_layers_cache()[index]
layers = list(available_layers.keys())

if not "layer" in st.session_state:
    st.session_state["layer"] = layers[len(layers) - 1]

st.subheader(f"{index_name} Spatial Variability")
widget = st.empty()

if st.button("Next layer"):
    st.session_state["map_secrets"] = st.session_state.map_secrets_new
    if st.session_state.layer == layers[len(layers) - 1]:
        st.session_state["layer"] = layers[0]
    else:
        st.session_state["layer"] = layers[layers.index(st.session_state.layer) + 1]

st.session_state["layer"] = widget.select_slider(
    label="Choose displayed date", options=layers, value=st.session_state.layer
)

row1_col1, row1_col2 = st.columns([7, 1])

with row1_col1:
    map = display_map(
        st.session_state.map_secrets,
        st.session_state.layer,
        available_layers[st.session_state.layer],
        get_colormap_cache()[index],
    )

    if "center" in map:
        st.session_state["map_secrets_new"] = {
            "coords": [map["center"]["lat"], map["center"]["lng"]],
            "zoom": map["zoom"],
        }

with row1_col2:
    st.write(get_legend_cache()[index])
