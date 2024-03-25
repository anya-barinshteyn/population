import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def get_subplot(subplots, ax_idx1, ax_idx2, file_name, area, debug=0):
    '''
    Places an area population chart to a subplot.
    Supports files with different scaling,
    but loads the whole 2D array first from the file passed
    and filters it afterwards.

    Parameters:
    - subblots: subplots object created outside
    - ax_idx1: 1-st index of the chart in the figure
    - ax_idx2: 2-nd index of the chart in the figure
    - file_name: input data set file name
    - area: an area description to draw needed
        The format is: (
            'Area description',
            longitude1,
            longitude2,
            latitude1,
            latitude2
            )
        For example:
        ('Плотность населения Африки, чел/кв.км.', -30, 60, 40, -40)
    - debug: flag to output debug messages if needed
    '''

    arr = np.loadtxt(file_name, skiprows=6)  # load data skipping header info
    # change -9999 to nan (for absent data)
    data = np.where(arr == -9999, np.nan, arr)
    cellsize = 360/data.shape[1]  # cell size (in degrees)
    if debug:  # debug output
        print("Max: {}, Min: {}".format(np.nanmax(data), np.nanmin(data)))
        print("Rows: {}, Columns: {}, Cellsize: {}".format(data.shape[0],
                                                           data.shape[1],
                                                           cellsize))

    # Compute min & max indexes for longitudes and latitues
    # to show just the area needed

    # Longitudes
    x_lon_min = area[1] if area[1] < area[2] else area[2]
    x_lon_max = area[1] if area[1] > area[2] else area[2]

    x_ind_min = int((x_lon_min + 180)/cellsize)  # minimum x index computation
    x_ind_max = int((x_lon_max + 180)/cellsize)  # maximum x index computation

    # just in case for erroneous input
    x_ind_min = x_ind_min if x_ind_min > 0 else 0
    x_ind_max = x_ind_max if x_ind_max < data.shape[1] else data.shape[1]

    # Latitudes
    y_lat_min = area[3] if area[3] < area[4] else area[4]
    y_lat_max = area[3] if area[3] > area[4] else area[4]

    y_ind_min = int((90 - y_lat_max)/cellsize)
    y_ind_min = y_ind_min if y_ind_min > 0 else 0
    y_ind_max = int((90 - y_lat_min)/cellsize)
    y_ind_max = y_ind_max if y_ind_max < data.shape[0] else data.shape[0]

    if debug:  # Debug output
        print("x_ind_min: {}, x_ind_max: {}".format(x_ind_min, x_ind_max))
        print("y_ind_min: {}, y_ind_max: {}".format(y_ind_min, y_ind_max))

    fig = subplots[0]
    ax = (subplots[1])[ax_idx1, ax_idx2]
    pcm = ax.pcolormesh(data[y_ind_min:y_ind_max, x_ind_min:x_ind_max],
                        cmap='turbo', norm=matplotlib.colors.LogNorm(vmin=1))
    # ax.set_ylabel('Широта', fontsize=18)
    # ax.set_xlabel('Долгота', fontsize=18)
    ax.set_title(area[0])

    # Supressing ticks
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())

    ax.set_aspect('equal', adjustable='box')
    # Y axis invertion because of the structure of a data file
    ax.invert_yaxis()
    fig.colorbar(pcm, ax=ax)  # Placing a colorbar to the chart
