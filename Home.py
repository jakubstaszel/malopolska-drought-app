import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize page title
st.title("Welcome to Waterpix")
st.subheader("Let's inspect your water in every pixel!")


st.header("How to check water quality in your area of interest?")

markdown = """
1. Check if all areas are added to your account,
2. Get familiar with meaning of each index,
3. Check what are the newest values and how they change within your area,
4. If you need it, use timeline to see how water quality changed in time.
"""

st.markdown(markdown)

st.subheader("Your Areas of Interest")
m = leafmap.Map(minimap_control=True, center=[49.73907, 20.68443], zoom=12)
m.add_geojson(
    "https://magisterkacog.blob.core.windows.net/aois/jezioro_roznowskie.json"
)
m.to_streamlit(height=500)
