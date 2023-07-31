from typing import Final

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# this should be the same as dict used for classification
# values are rather ints and there should be add first item
# (which is the min value in raster before classification)
classes: Final = {
    "cdom": [0, 10, 20, 30, 40, 50, 100],
    "chla": [0.0, 5.0, 7.5, 10.0, 15.0, 25.0, 100.0],
    "cya": [0.0, 2.5, 5.0, 7.5, 10.0, 50.0, 100.0, 300.0],
    "doc": [0, 10, 20, 30, 40, 50, 100],
    "turb": [0.0, 2.5, 5.0, 7.5, 10.0, 20.0, 50.0, 100.0],
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

index_names: Final = {
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


def cdi_colormap():
    data = {}
    index = "cdi"
    classes: Final = {"cdi": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]}
    max_in_classified_raster = len(classes[index])

    scalar_mappable = [
        [1.0, 1.0, 0.8, 1.0],  # yellow
        [0.99529412, 0.66901961, 0.2854902, 1.0],  # orange
        [0.83058824, 0.06117647, 0.1254902, 1.0],  # red
        [0.0, 0.278, 0.671, 1.0],  # blue
        [0.667, 0.2, 0.416, 1.0],  # purple
        [0.314, 0.784, 0.471, 1.0],  # green
    ]
    colors_dict = {}
    pixel_values = list(range(1, max_in_classified_raster + 1))
    for idx, pixel in enumerate(pixel_values):
        colors_dict[pixel] = mpl.colors.rgb2hex(scalar_mappable[idx], keep_alpha=False)
    data[index] = colors_dict
    return data[index]


def cdi_legend_colormap():
    colormap = cdi_colormap()
    index_names_cdi = {
        "cdi": "CDI",
    }
    index = "cdi"
    data = {}
    classes: Final = {"cdi": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]}
    no_classes = len(classes[index])

    colors = list(colormap.values())
    fig, ax = plt.subplots(figsize=(1, 4))
    norm = mpl.colors.Normalize(vmin=min(classes[index]), vmax=max(classes[index]))
    col_map = mpl.colors.ListedColormap(
        name=index_names_cdi[index], colors=list(colors), N=no_classes
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
    val_final = []
    for value in val:
        val_final.append(value - 0.4)
    labels = ["No Drought", "Watch", "Warning", "Alert", "Recovery", "TSMR", "TVR"]
    ax.set_yticks(val_final, labels=labels)

    data[index] = fig
    return data[index]


def nmdi_interp_colormap():
    data = {}
    index = "nmdi_interp"
    classes: Final = {"nmdi_interp": [1.0, 2.0, 3.0, 4.0]}
    max_in_classified_raster = len(classes[index])

    scalar_mappable = [
        [0.0, 0.278, 0.671, 1.0],  # blue
        [0.678, 0.847, 0.902, 1.0],  # light blue
        [0.99529412, 0.66901961, 0.2854902, 1.0],  # orange
        [0.83058824, 0.06117647, 0.1254902, 1.0],  # red
    ]
    colors_dict = {}
    pixel_values = list(range(1, max_in_classified_raster + 1))
    for idx, pixel in enumerate(pixel_values):
        colors_dict[pixel] = mpl.colors.rgb2hex(scalar_mappable[idx], keep_alpha=False)
    data[index] = colors_dict
    return data[index]


def nmdi_interp_legend_colormap():
    colormap = nmdi_interp_colormap()
    index_names_interp = {
        "nmdi_interp": "NMDI Interpreted",
    }
    index = "nmdi_interp"
    data = {}
    classes: Final = {"nmdi_interp": [1.0, 2.0, 3.0, 4.0]}
    no_classes = len(classes[index])

    colors = list(colormap.values())
    fig, ax = plt.subplots(figsize=(1, 4))
    norm = mpl.colors.Normalize(vmin=min(classes[index]), vmax=max(classes[index]))
    col_map = mpl.colors.ListedColormap(
        name=index_names_interp[index], colors=list(colors), N=no_classes
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
    val_final = []
    for value in val:
        val_final.append(value - 0.4)
    labels = ["No Data", "Very Wet", "Wet", "Dry", "Very Dry"]
    ax.set_yticks(val_final, labels=labels)

    data[index] = fig
    return data[index]
