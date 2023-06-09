import json
from typing import Final

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

import streamlit as st
import leafmap.foliumap as leafmap
from streamlit_folium import st_folium

from imagery.colormaps import get_colormap, get_legend_colormap
from imagery.imagery_files import get_available_layers
from imagery.display_map import display_map
from imagery.stats import get_stats

index: Final = "doc"


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


st.title("Dissolved Organic Carbon")

st.write(
    "Dissolved Organic Carbon (DOC) significantly affects the structure and functions of lake ecosystems. There are similar sources of organic carbon as for the CDOM. Due to the dark colour of most DOC particles, it affects thermal structure of reservoirs and becomes a driver in water mixing. Organic carbon’s absorption properties make photosynthesis more difficult, it protects elements of the ecosystem against harmful UV radiation. DOC can also affect the fate of other dissolved substances (e.g. metals). The range of DOC effects on the water ecosystem is so large that it has a  great interest among researchers (Sobek et al., 2007)."
)
st.subheader("DOC Statistics Across Time")
st.line_chart(get_stats_cache()[index])

if not "map_secrets" in st.session_state:
    st.session_state["map_secrets"] = {"coords": [49.73907, 20.68443], "zoom": 12}
    st.session_state["map_secrets_new"] = st.session_state.map_secrets

available_layers = get_layers_cache()[index]
layers = list(available_layers.keys())

if not "layer" in st.session_state:
    st.session_state["layer"] = layers[len(layers) - 1]

st.subheader("DOC Spatial Variability")
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

    # st.write(map)

with row1_col2:
    st.write(get_legend_cache()[index])
    st.write("DOC [mg/l]")
