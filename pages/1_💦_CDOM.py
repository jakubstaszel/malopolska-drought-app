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

index: Final = "cdom"


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


st.title("Colored Dissolved Organic Matter")

st.write(
    "Colourful Dissolved Organic Matter (CDOM) is a water quality parameter that examines optically active organic matter. The value of this parameter depends on two sources of organic matter. The first is the material that develops inside the reservoir (e.g. phytoplankton), and the second is the matter originating from the outside (e.g. coal leaked from the soil). Studies show that the second source is dominant (Sobek et al., 2007). Photo- and biodegradation of organic matter can lead to increased CO2 values ​​in lake systems (Tranvik et al., 2009). CDOM also regulates the amount of light available for net primary production and trophic structure. It has also been shown that, for rivers, there is a correlation between content of methylmercury and CDOM (Fichot et al., 2015)."
)
st.subheader("CDOM Statistics Across Time")
st.line_chart(get_stats_cache()[index])

if not "map_secrets" in st.session_state:
    st.session_state["map_secrets"] = {"coords": [49.73907, 20.68443], "zoom": 12}
    st.session_state["map_secrets_new"] = st.session_state.map_secrets

available_layers = get_layers_cache()[index]
layers = list(available_layers.keys())

if not "layer" in st.session_state:
    st.session_state["layer"] = layers[len(layers) - 1]

st.subheader("CDOM Spatial Variability")
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
    st.write("CDOM [mg/l]")
