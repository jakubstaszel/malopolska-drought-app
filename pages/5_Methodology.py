import streamlit as st
import pandas as pd


st.title("Satellite Imagery Technologies Behind Drought Monitoring")
st.subheader("Indexes' Equations")
latext1 = r"""
$$ 
\text{NDWI v1} = \frac{{\text{B8A} - \text{B12}}}{{\text{B8A} + \text{B12}}}
$$
$$
\text{NDWI v2} = \frac{{\text{B03} - \text{B08}}}{{\text{B03} + \text{B08}}}
$$
$$
\text{NMDI} = \frac{{\text{B08} - (\text{B11} - \text{B12})}}{{\text{B08} + (\text{B11} - \text{B12})}}
$$
$$
\text{NDMI} = \frac{{\text{B08} - \text{B11}}}{{\text{B08} + \text{B11}}}
$$
$$
\text{NDVI} = \frac{{\text{B08} - \text{B04}}}{{\text{B08} + \text{B04}}}
$$
"""
latex2 = r"""
$$
\text{WDRVI} = \frac{{0.1 \cdot \text{B08} - \text{B04}}}{{0.1 \cdot \text{B08} + \text{B04}}}
$$
$$
\text{EVI} = \frac{{2.5 \cdot (\text{B08} - \text{B04})}}{{\text{B08} + 6 \cdot \text{B04} - 7.5 \cdot \text{B02} + 1}}
$$
$$
\text{MSAVI2} = \frac{{2 \cdot \text{B08} + 1 - \sqrt{{(2 \cdot \text{B08} + 1)^2 - 8 \cdot (\text{B08} - \text{B04})}}}}{2}
$$
$$
\text{MSI} = \frac{{\text{B11}}}{{\text{B8A}}}
$$
"""
row1_col1, row1_col2 = st.columns([1, 1])
with row1_col1:
    st.write(latext1)
with row1_col2:
    st.write(latex2)

st.subheader("Satellite Imagery Selection")
st.write(
    "The images were primarily selected in a manner to minimize cloud coverage over the area of interest. Despite the removal of clouds-covered areas during data processing, the appropriate selection of images also enhances the representativeness of the results and statistics. Attention was also paid to choosing images from a similar period within each year, with four dates selected for each year - exact dates presented in table below. Almost all data (exceptions described below the table) were acquired by the Sentinel-2 satellites within relative orbit number 036, utilizing measurements from both satellites."
)
satellite_images = {
    "2018": {
        "Date 1": "20 April",
        "Date 2": "19 June",
        "Date 3": "23 August",
        "Date 4": "6 November",
    },
    "2019": {
        "Date 1": "31 March",
        "Date 2": "9 June",
        "Date 3": "28 August",
        "Date 4": "27 October",
    },
    "2020": {
        "Date 1": "9 April",
        "Date 2": "12 June",
        "Date 3": "22 August",
        "Date 4": "25 November",
    },
    "2021": {
        "Date 1": "9 April",
        "Date 2": "18 June",
        "Date 3": "6 September",
        "Date 4": "31 October",
    },
    "2022": {
        "Date 1": "25 March",
        "Date 2": "3 June",
        "Date 3": "27 August",
        "Date 4": "31 October",
    },
    "2023": {"Date 1": "23 April", "Date 2": "3 June", "Date 3": "-", "Date 4": "-"},
}
st.write(pd.DataFrame.from_dict(satellite_images, orient="index"))
st.write(
    "In the case of data from 23 April 2023, it was not possible to select images from the exact date. Therefore, images from 22 and 24 April 2023, were used instead. The images from 22 April had a sufficiently low cloud coverage level. However, orbit number 79 does not fully cover the area of Małopolska, resulting in data gaps that were filled with the data from 24 April."
)
st.write(
    "For the date of 3 June 2023, one of the images was unavailable in the Open Access Hub for processing level 2A. As a workaround, an image of processing level 1C was downloaded, and then the Sen2Cor plugin for the SNAP program was utilized through the command line interface to process the available image."
)
