from typing import Final

import streamlit as st
import leafmap.foliumap as leafmap

from imagery.colormaps import get_colormap, get_legend_colormap
from imagery.imagery_files import get_available_layers
from imagery.display_map import display_map_swipe
from imagery.stats import get_stats

title: Final = "Compare Different Map Layers"

st.cache_data(ttl=3600)
def get_stats_cache():
    return get_stats()


st.cache_data(ttl=3600)
def get_layers_cache():
    return get_available_layers()


st.cache_data(ttl=3600)
def get_colormap_cache():
    return get_colormap()


st.cache_data(ttl=3600)
def get_legend_cache():
    return get_legend_colormap()


st.title(title)

if not "map_secrets" in st.session_state:
    st.session_state["map_secrets"] = {"coords": [49.8663, 20.1654], "zoom": 9}
    st.session_state["map_secrets_new"] = st.session_state.map_secrets

if not "index_for_compare" in st.session_state:
    st.session_state["index_for_compare"] = list(get_available_layers().keys())[0]

available_layers = get_layers_cache()[st.session_state.index_for_compare]
layers = list(available_layers.keys())

if not "layer1" in st.session_state:
    st.session_state["layer1"] = layers[len(layers) - 1]
if not "layer2" in st.session_state:
    st.session_state["layer2"] = layers[len(layers) - 1]

row1_col1, row1_col2, row1_col3 = st.columns([1, 1, 1])
with row1_col1:
    st.session_state["index_for_compare"] = st.selectbox(
        label="Choose index", options=get_available_layers().keys(), index=0
    )

with row1_col2:
    st.session_state["layer1"] = st.selectbox(
        label="Choose layer displayed on the left", options=layers, index=len(layers)-1
    )
with row1_col3:
    st.session_state["layer2"] = st.selectbox(
        label="Choose layer displayed on the right", options=layers, index=len(layers)-1
    )

row2_col1, row2_col2 = st.columns([1, 7])

with row2_col1:
    st.write(get_legend_cache()[st.session_state.index_for_compare])

with row2_col2:
    st.write(st.session_state.index_for_compare, st.session_state.layer1, st.session_state.layer2)
    map = display_map_swipe(
        st.session_state.map_secrets,
        st.session_state.layer1,
        st.session_state.layer2,
        available_layers[st.session_state.layer1],
        available_layers[st.session_state.layer2],
        get_colormap_cache()[st.session_state.index_for_compare],
    )

    if "center" in map:
        st.session_state["map_secrets_new"] = {
            "coords": [map["center"]["lat"], map["center"]["lng"]],
            "zoom": map["zoom"],
        }
