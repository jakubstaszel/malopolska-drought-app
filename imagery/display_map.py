import json

import leafmap.foliumap as leafmap
from leafmap.stac import cog_bounds, cog_tile
import folium
import folium.plugins
from streamlit_folium import st_folium

import streamlit as st


def display_map(map_secrets, layer_name, layer_url, colors):
    m = leafmap.Map(minimap_control=True, layers_control=True)

    m.add_cog_layer(
        layer_url,
        name=str(layer_name),
        nodata=0,
        colormap=f"{json.dumps(colors)}",
        bidx=1,
        rescale="0,255",
    )

    m.add_layer_control()

    folium_map = st_folium(
        m,
        width=None,
        height=500,
        center=map_secrets["coords"],
        zoom=map_secrets["zoom"],
    )

    return folium_map


def display_map_swipe_meteo(
    map_secrets, layer1_name, layer2_name, layer1_url, layer2_url, colors1, colors2, key
):
    m = folium.plugins.DualMap(tiles="openstreetmap", layout="vertical")
    tile_url_1 = cog_tile(
        layer1_url, colormap=f"{json.dumps(colors1)}", rescale="0,255", bidx=1, nodata=0
    )
    tile_url_2 = cog_tile(
        layer2_url, colormap=f"{json.dumps(colors2)}", rescale="0,255", bidx=1, nodata=0
    )

    folium.raster_layers.TileLayer(
        tiles=tile_url_1,
        attr=".",
        name=str(layer1_name),
        overlay=True,
        control=True,
        show=True,
        opacity=1.0,
    ).add_to(m.m1)

    folium.raster_layers.TileLayer(
        tiles=tile_url_2,
        attr=".",
        name=str(layer2_name),
        overlay=True,
        control=True,
        show=True,
        opacity=1.0,
    ).add_to(m.m2)

    folium_map = st_folium(
        m,
        width=None,
        height=600,
        center=map_secrets["coords"],
        zoom=map_secrets["zoom"],
        key=key,
    )

    return folium_map


def display_map_swipe(
    map_secrets, layer1_name, layer2_name, layer1_url, layer2_url, colors, key
):
    m = folium.plugins.DualMap(tiles="openstreetmap")
    tile_url_1 = cog_tile(
        layer1_url, colormap=f"{json.dumps(colors)}", rescale="0,255", bidx=1, nodata=0
    )
    tile_url_2 = cog_tile(
        layer2_url, colormap=f"{json.dumps(colors)}", rescale="0,255", bidx=1, nodata=0
    )

    folium.raster_layers.TileLayer(
        tiles=tile_url_1,
        attr=".",
        name=str(layer1_name),
        overlay=True,
        control=True,
        show=True,
        opacity=1.0,
    ).add_to(m.m1)

    folium.raster_layers.TileLayer(
        tiles=tile_url_2,
        attr=".",
        name=str(layer2_name),
        overlay=True,
        control=True,
        show=True,
        opacity=1.0,
    ).add_to(m.m2)

    folium_map = st_folium(
        m,
        width=None,
        height=500,
        center=map_secrets["coords"],
        zoom=map_secrets["zoom"],
        key=key,
    )

    return folium_map
