import json

import leafmap.foliumap as leafmap
from streamlit_folium import st_folium

def display_map(map_secrets, layer_name, layer_url, colors):
    m = leafmap.Map(
        minimap_control=True,
        layers_control = True
    )

    m.add_cog_layer(
        layer_url,
        name=str(layer_name),
        nodata=0,
        colormap=f"{json.dumps(colors)}",
        bidx=1,
        rescale="0,255",
    )

    folium_map = st_folium(
        m,
        width=None,
        height=500,
        center=map_secrets["coords"],
        zoom=map_secrets["zoom"],
    )

    return folium_map