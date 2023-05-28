import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize page title
st.title("Drought Monitoring for Malopolska region")
st.subheader(
    "Drought have severe consequences for ecosystems, agriculture, economies, and human well-being. Monitoring drought conditions is crucial and here is why:"
)

markdown = """
1. Water resource management - Drought monitoring informs decisions on water allocation, reservoir management, and restrictions to ensure sustainable water management.
2. Agriculture and food security: Drought monitoring enables farmers to adjust strategies, anticipate water stress, and address food shortages for vulnerable populations.
3. Environmental impact: Drought monitoring helps identify areas of ecological stress and implement measures to protect ecosystems, wildlife, and natural resources.
4. Risk assessment and planning: Drought monitoring data aids in evaluating vulnerabilities, developing contingency plans, and reducing the impact of drought-related disasters.
5. Climate change adaptation: Drought monitoring enhances understanding of how droughts are influenced by climate change, informing adaptation strategies and policies."""
st.markdown(markdown)

st.subheader("Malopolska region in Poland")

m = leafmap.Map(minimap_control=True, center=[49.8663, 20.1654], zoom=8)
m.add_geojson(
    "https://magisterkacog.blob.core.windows.net/aois/malopolska.json",
    layer_name="Malopolska Simplified 1km",
    info_mode="on_click",
)
m.to_streamlit(height=500)
