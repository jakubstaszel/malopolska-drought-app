from typing import Final

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# this should be the same as dict used for classification
# values are rather ints and there should be add first item
# (which is the min value in raster before classification)
classes: Final = {
    "cdom": [0, 5, 20, 50, 100, 1000],
    "chla": [0, 10, 100, 1000, 5000, 15000],
    "cya": [0, 5, 10, 20, 50, 100, 300, 1000, 10000],
    "doc": [0, 10, 30, 50, 200, 1000],
    "turb": [0, 5, 20, 50, 500, 40000],
    "ndwi1": [-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    "ndwi2": [-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    "nmdi": [0.0, 0.2, 0.6, 0.7, 0.8, 0.9, 1.0],
    "ndmi": [-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    "ndvi": [-1.0, -0.1, 0.1, 0.3, 0.5, 0.8, 1.0],
    "wdrvi": [-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    "evi": [-10.0, -1.0, -0.2, 0.0, 0.2, 0.8, 1.0, 2.0, 7.0, 10.0],
    "msavi2": [-1.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    "msi": [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0],
}


def get_colormap():
    data = {}
    for index in classes.keys():
        max_in_classified_raster = len(classes[index])

        cmap = mpl.cm.YlOrRd
        scalar_mappable = mpl.cm.ScalarMappable(cmap=cmap).to_rgba(
            np.arange(1, max_in_classified_raster, 1), alpha=True, bytes=False
        )
        colors_dict = {}
        pixel_values = list(range(1, max_in_classified_raster))
        for idx, pixel in enumerate(pixel_values):
            colors_dict[pixel] = mpl.colors.rgb2hex(
                scalar_mappable[idx], keep_alpha=False
            )
        data[index] = colors_dict
    return data


def get_legend_colormap():
    colormaps = get_colormap()
    index_names = {
        "cdom": "CDOM",
        "chla": "Chl A",
        "cya": "Cyanobacteria",
        "doc": "DOC",
        "turb": "Turbidity",
        "ndwi1": "NDWI v1",
        "ndwi2": "NDWI v2",
        "nmdi": "NMDI",
        "ndmi": "NDMI",
        "ndvi": "NDVI",
        "wdrvi": "WDRVI",
        "evi": "EVI",
        "msavi2": "MSAVI2",
        "msi": "MSI",
    }

    data = {}
    for index in classes.keys():
        no_classes = len(classes[index]) - 1

        colors = list(colormaps[index].values())
        fig, ax = plt.subplots(figsize=(1, 4))
        norm = mpl.colors.Normalize(vmin=min(classes[index]), vmax=max(classes[index]))
        col_map = mpl.colors.ListedColormap(
            name=index_names[index], colors=list(colors), N=no_classes
        )
        cb = mpl.colorbar.ColorbarBase(ax, norm=norm, cmap=col_map)

        ranges = range(no_classes + 1)
        val = list(
            np.interp(
                ranges,
                (min(ranges), max(ranges)),
                (min(classes[index]), max(classes[index])),
            )
        )
        ax.set_yticks(val, labels=classes[index])

        data[index] = fig
    return data
