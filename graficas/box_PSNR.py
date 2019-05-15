# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    shivani2017 = [
        39.412400,37.953329,39.405832,38.916522,38.439209,37.999932,38.835189,37.935623,38.755422,37.274261,38.235718,37.396278,37.745851,37.487157,37.877802,37.422671,37.066242,38.170408,37.704153,37.574749,37.589621,37.812069,37.548741,37.335278,37.162564,37.086484,37.729254,37.735927,38.254805,38.744720,37.203511,37.621834,36.762054,38.031645,36.726871,37.931698,37.911517,39.595517,38.034024,37.400031,38.340388,37.830170,38.160768,39.374882,37.688412,37.946189,37.771573,37.482753,36.664810,36.918083,37.218706,37.204875,37.825845,36.613349,36.749791,38.279079,37.347104,36.789668,36.474545,36.135333]
    
    liu2018 = [
        32.942211,32.482750,32.873229,32.250052,32.192542,32.289131,32.175604,32.163622,32.280870,32.387490,32.261490,32.295386,32.478652,32.299353,32.189106,32.484635,32.173200,32.682220,32.192177,32.326366,32.212692,32.401887,32.145518,32.230704,32.637898,32.307429,32.256415,32.500181,32.908275,32.394803,32.270795,32.465574,32.069685,32.199538,32.341669,32.522166,32.380163,32.472673,32.094687,32.034447,32.271921,32.487768,32.567326,32.664959,32.422300,32.170887,31.997221,32.130697,32.202558,32.075111,32.463362,32.002566,32.181643,32.185171,32.096452,32.209672,32.296958,32.123008,32.168209,31.892561
    ]

    avila2018 = [
        44.265707,44.676721,45.411788,44.531670,44.694593,44.252413,45.035256,44.493173,45.007116,44.376873,45.185017,44.943083,44.801391,44.854296,44.900670,44.581012,44.560070,45.088821,44.661495,44.690536,44.719412,44.512057,45.017194,44.697061,44.582661,44.674387,45.198149,44.845690,45.022010,45.046487,44.577858,45.003475,44.808285,44.826332,44.977428,44.758299,44.846555,45.587070,44.693239,44.678502,45.128010,44.642840,44.997605,45.267579,44.823783,44.874219,44.804761,44.596934,43.971378,44.644823,44.543947,44.587669,44.738352,44.536479,44.649925,45.459403,44.884012,44.586786,44.753116,44.195675
    ]

    proposed = [
        45.369442,45.947478,47.024037,45.730454,45.986061,45.371383,46.584632,45.811163,46.471469,45.554522,46.815913,46.457573,46.293523,46.259346,46.321463,45.785345,45.778517,46.601330,45.984213,45.977060,46.147375,45.702016,46.558657,45.901613,45.785495,46.071789,46.859379,46.293357,46.495370,46.509776,45.822967,46.465836,46.197865,46.129732,46.412059,46.213322,46.353495,47.422084,45.968513,46.007451,46.622761,45.934078,46.449579,46.922754,46.259729,46.254851,46.242444,45.729350,45.045943,45.976057,45.951304,45.876765,46.145755,45.756572,46.015646,47.219347,46.242926,45.890379,46.148057,45.409471
    ]

    data = [shivani2017, liu2018, avila2018, proposed]

    fig, ax1 = plt.subplots(figsize=(6, 6))
    fig.canvas.set_window_title('PSNR')
    fig.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.05)

    bp = ax1.boxplot(data, notch=0, sym='+', vert=1, whis=1.5)
    plt.setp(bp['boxes'], color='blue')
    plt.setp(bp['whiskers'], color='black')
    plt.setp(bp['fliers'], marker='+', color='blue')

    # Add a horizontal grid to the plot, but make it very light in color
    # so we can use it for reading data values but not be distracting
    ax1.yaxis.grid(
        True, linestyle='-', which='major', color='lightgrey',
        alpha=0.5)
    
    # Hide these grid behind plot objects
    ax1.set_axisbelow(True)
    ax1.set_title('Saint Gall database (60 images)')
    ax1.set_xlabel('Schemes')
    ax1.set_ylabel('PSNR')

    # Now fill the boxes with desired colors
    numDists = 4
    boxColors = ['darkkhaki', 'green', 'blue', 'red']
    for i in range(numDists):
        box = bp['boxes'][i]
        boxX = []
        boxY = []
        for j in range(5):
            boxX.append(box.get_xdata()[j])
            boxY.append(box.get_ydata()[j])
        boxCoords = np.column_stack([boxX, boxY])
        boxPolygon = Polygon(boxCoords, facecolor=boxColors[i])
        ax1.add_patch(boxPolygon)
        # Now draw the median lines back over what we just filled in
        med = bp['medians'][i]
        # Finally, overplot the sample averages, with horizontal alignment in the center of each box
        ax1.plot([np.average(med.get_xdata())], [np.average(data[i])],
                color='w', marker='*', markeredgecolor='k')

    ax1.set_xticklabels(
        [
            '[13]', '[9]', '[2]', 'Proposed'
        ],
        rotation=0, fontsize=14)
    plt.show()


if __name__ == "__main__":
    run_main()