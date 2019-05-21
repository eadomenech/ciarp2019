# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    shivani2017 = [
        0.328963,0.331113,0.332800,0.326988,0.328321,0.329482,0.329277,0.330123,0.328896,0.329195,0.329847,0.326490,0.328295,0.327473,0.325586,0.327319,0.324525,0.327057,0.335886,0.325018,0.324353,0.325489,0.326397,0.327363,0.326276,0.327278,0.326139,0.327206,0.323977,0.326438,0.330886,0.331413,0.329536,0.328447,0.328266,0.329313,0.330754,0.332751,0.327500,0.330971,0.329291,0.326580,0.328341,0.329267,0.334490,0.326500,0.328765
    ]
    
    liu2018 = [
        0.280697,0.287461,0.299688,0.290062,0.270812,0.283039,0.278616,0.267950,0.258065,0.267690,0.271332,0.268991,0.267950,0.265088,0.273933,0.269251,0.286160,0.266909,0.255723,0.272373,0.277575,0.268470,0.268470,0.268210,0.281998,0.271852,0.290583,0.274454,0.273933,0.262747,0.269511,0.284079,0.264048,0.284860,0.278356,0.274974,0.258845,0.292404,0.260146,0.271592,0.263788,0.263788,0.284599,0.261707,0.280697,0.276015,0.264308
    ]

    avila2018 = [
        0.016649,0.022112,0.018470,0.020031,0.017170,0.017950,0.015609,0.015869,0.017690,0.020031,0.025494,0.017430,0.019251,0.017690,0.020552,0.017430,0.017950,0.020812,0.021852,0.014308,0.014828,0.013788,0.013528,0.015609,0.016129,0.019251,0.020031,0.018730,0.017690,0.015869,0.019251,0.016389,0.011446,0.017690,0.018730,0.018730,0.020291,0.019511,0.017430,0.021852,0.018991,0.014308,0.013007,0.017430,0.016129,0.016129,0.020812,0.021332,0.020291,0.017950,0.021072,0.016389,0.019251,0.016129,0.021072,0.021072,0.017430,0.015349,0.016649,0.018210
    ]

    proposed = [
        0.094173,0.078824,0.078304,0.078044,0.069979,0.065817,0.092612,0.080385,0.073881,0.088189,0.073881,0.067638,0.094693,0.087409,0.084547,0.071280,0.070760,0.063476,0.082206,0.079865,0.074662,0.072060,0.063476,0.076743,0.070499,0.088450,0.081686,0.083247,0.069459,0.070239,0.081165,0.081165,0.073101,0.072060,0.078824,0.082726,0.077784,0.091311,0.070760,0.073881,0.083507,0.083507,0.077784,0.081426,0.090531,0.091051,0.060094
    ]

    data = [shivani2017, liu2018, avila2018, proposed]

    fig, ax1 = plt.subplots(figsize=(6, 6))
    fig.canvas.set_window_title('BER')
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
    ax1.set_title('ParzivalSaint Gall database (60 images)')
    ax1.set_xlabel('Schemes')
    ax1.set_ylabel('BER')

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
            '[13]', '[9]', '[2]+FW', 'Proposed'
        ],
        rotation=0, fontsize=14)
    plt.show()


if __name__ == "__main__":
    run_main()