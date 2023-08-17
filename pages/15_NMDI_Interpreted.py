from typing import Final

import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

from imagery.colormaps import (
    cdi_colormap,
    cdi_legend_colormap,
    nmdi_interp_colormap,
    nmdi_interp_legend_colormap,
)
from imagery.imagery_files import get_cdi_layers, get_nmdi_interp_layers
from imagery.display_map import display_map_swipe_meteo
from imagery.stats import get_means_normalized

index: Final = "nmdi_interp"
title: Final = "Interpreted NMDI"
index_name: Final = "NMDI Interpreted"


def get_means_normalized_cache():
    return get_means_normalized()


st.title(title)

st.write(
    "Values of Normalized Multi-band Drought Index were interpreted according to the classification proposed in the arcticle Remote Sensing of Soil and Vegetation Moisture from Space for Monitoring Drought and Forest Fire Events by Lingli Wang, John J. Qu and Xianjun Hao (DOI: [10.1201/b11279-27](http://dx.doi.org/10.1201/b11279-27))."
)
st.write("Classification: ")
col1 = "Vegetation - NDVI > 0.4"
col2 = "Soil - NDVI < 0.4"
satellite_images = {
    "Very Dry": {
        col1: "< 0.2",
        col2: "0.7 - 0.9",
    },
    "Dry": {
        col1: "< 0.4",
        col2: "> 0.5",
    },
    "Wet": {
        col1: "0.4 - 0.6",
        col2: "0.3 - 0.5",
    },
    "Very Wet": {
        col1: "> 0.6",
        col2: "< 0.3",
    },
}
st.write(pd.DataFrame.from_dict(satellite_images, orient="index"))

if not "map_secrets" in st.session_state:
    st.session_state["map_secrets"] = {"coords": [49.8663, 20.1654], "zoom": 9}
    st.session_state["map_secrets_new"] = st.session_state.map_secrets


available_layers = get_nmdi_interp_layers()
layers = list(available_layers["nmdi_interp"].keys())

if not "date" in st.session_state:
    st.session_state["date"] = layers[len(layers) - 1]

st.subheader("Share of Pixels Indicating Drought Across Time")
st.write(
    "For CDI - share of pixels with class Warning or Alert. For NMDI Interpreted - share of pixels with class Dry or Very Dry."
)
data = get_means_normalized_cache()[["nmdi"]]
data["CDI"] = [
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
data["NMDI Interp 20 m"] = [
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

data["NMDI Interp 5 km"] = [
    0.03002309468822171,
    0.0024096385542168677,
    0.046189376443418015,
    0.018475750577367205,
    0.22685185185185186,
    0.006944444444444444,
    0.016166281755196306,
    0.018518518518518517,
    0.10392609699769054,
    0.004618937644341801,
    0.013856812933025405,
    0.1320754716981132,
    0.23433874709976799,
    0.0023094688221709007,
    0.002304147465437788,
    0.1175115207373272,
    1.0,
    0.07852193995381063,
    0.34651162790697676,
    0.9953596287703016,
    0.969047619047619,
    0.07834101382488479,
]
data.rename(
    columns={
        "NMDI Interp 20 m": "1 NMDI Interp 20 m",
        "NMDI Interp 5 km": "2 NMDI Interp 5 km",
        "CDI": "3 CDI",
    },
    inplace=True,
)
st.line_chart(
    data[["1 NMDI Interp 20 m", "2 NMDI Interp 5 km", "3 CDI"]],
)

with st.form("compare_map_form"):
    generate = st.form_submit_button("Generate")

    row1_col1, row1_col2 = st.columns([1, 4])
    with row1_col1:
        st.session_state["date"] = st.selectbox(
            label="Choose date",
            options=layers,
            index=len(layers) - 1,
        )
    with row1_col2:
        versions_dict = {
            "NMDI Interp Downscaled 5 Km": "nmdi_interp_5km",
            "NMDI Interp 20 M": "nmdi_interp",
        }
        nmdi_version = st.selectbox(
            label="Choose version of interpreted NMDI", options=versions_dict, index=0
        )

    if generate:
        row2_col1, row2_col2 = st.columns([7, 1])
        with row2_col1:
            row3_col1, row3_col2 = st.columns([1, 1])
            with row3_col1:
                st.subheader(nmdi_version)
            with row3_col2:
                st.subheader("CDI")
            map_var_name = f"map_nmdi_interp_cdi_{st.session_state.date}_{versions_dict[nmdi_version]}"
            map = display_map_swipe_meteo(
                st.session_state.map_secrets,
                versions_dict[nmdi_version] + "_" + st.session_state.date,
                "cdi" + "_" + st.session_state.date,
                available_layers[versions_dict[nmdi_version]][st.session_state.date],
                get_cdi_layers()[st.session_state.date],
                nmdi_interp_colormap(),
                cdi_colormap(),
                map_var_name,
            )

            st.write(
                "TVR - Temporary Vegetation Recovery, TSMR - Temporary Soil Moisture Recovery"
            )

        if "center" in map:
            st.session_state["map_secrets_new"] = {
                "coords": [map["center"]["lat"], map["center"]["lng"]],
                "zoom": map["zoom"],
            }

        with row2_col2:
            st.write(f"For NMDI Interp")
            legend1 = st.write(nmdi_interp_legend_colormap())
            st.write(f"For CDI")
            legend2 = st.write(cdi_legend_colormap())
