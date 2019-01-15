import os
import pandas as pd
import numpy as np
from scipy.stats import norm

from fuzzy.core import FuzzyPlotly, DensPlotly, StandardErrorPlot, FanPlotly

# Utility function to generate confidence intervals
def generate_interval_point(p, center, std):
    point = [p]
    boundary_point = norm.ppf(point, loc=center, scale=std)
    return boundary_point[0]


# Takes CSV with median and standard deviation and generate confidence intervals.
def create_data():
    my_csv = os.path.join(os.path.dirname(__file__), 'uk_unemployment_2013-2018.csv')
    df = pd.read_csv(my_csv)

    # Finds std from given 95% CI. Assumes it follows normal curve
    df['std'] = df['95%CI'] / 1000 / 1.96

    # print(list(df.dtypes.index))

    std = list(df['std'])

    # Scale to be in thousands
    y = list(df['Number of unemployed people']/1000)

    y_n_95 = []
    y_p_95 = []

    y_n_60 = []
    y_p_60 = []

    y_n_30 = []
    y_p_30 = []

    y_median = []

    for i in range(len(y)):
        y_n_95.append(generate_interval_point(0.025, y[i], std[i]))
        y_p_95.append(generate_interval_point(0.975, y[i], std[i]))

        y_n_60.append(generate_interval_point(0.2, y[i], std[i]))
        y_p_60.append(generate_interval_point(0.8, y[i], std[i]))

        y_n_30.append(generate_interval_point(0.35, y[i], std[i]))
        y_p_30.append(generate_interval_point(0.65, y[i], std[i]))

        y_median.append(generate_interval_point(0.5, y[i], std[i]))

    # Improving data label.
    df['DateLabel'] = df['DateLabel'].replace(np.nan, '', regex=True)

    x = list(df['Date'])
    x_label = list((df['DateLabel']))

    return x, x_label, y_median, y_p_95, y_n_95, y_p_30, y_n_30, y_p_60, y_n_60


if __name__ == '__main__':
    color = '#4286f4'
    median_line_color = '#004C99'
    median_line_width = 2

    x, x_label, y_median, y_p_95, y_n_95, y_p_30, y_n_30, y_p_60, y_n_60 = create_data()

    # for ticks, change step size. so it only plots ticks on those parts.
    x_new = x[0::2]
    x_label_new = x_label[0::2]
    # Add in new line between month and year
    x_label_new = [x_label.replace('-', '<br>20') for x_label in x_label_new]

    layout = {
        'showlegend': False,
        'title': 'UK Migration figures (2013-2018)',
        'xaxis': {
            'title': 'Date',
            'titlefont': {
                'family': 'Arial, sans-serif',
                'size': 18,
                'color': 'black',
            },
            'tickfont': {
                'family': 'Arial, sans-serif',
                'size': 15,
                'color': 'black',
            },
            'ticktext':x_label_new,
            'tickvals':x_new,
            'showgrid':False,
            'showline': True,

            'tickmode':'array',
            'ticks': 'outside',
            'tickangle': 0,
            'showticklabels': True,
            'tickwidth': 2,
            'tickcolor': '#000',

            'mirror': True,
        },
        'yaxis': {
            'title': 'Unemployment (in thousands)',
            'titlefont': {
                'family': 'Arial, sans-serif',
                'size': 18,
                'color': 'black',
            },
            'tickfont': {
                'family': 'Arial, sans-serif',
                'size': 15,
                'color': 'black',
            },
            'showgrid':False,
            'range': [1000000/1000, 2600000/1000],
            'showline': True,
            'tickmode': 'array',
            'ticks': 'outside',
            'mirror': True,
            'tickwidth': 2,

        },
        'margin': {
            # 'l':50,
            # 'r':50,
            # 'b':100,
            # 't':100,
            'pad':14,
        }
    }

    median_only = FuzzyPlotly(
        x, y_median,
        ci95p=y_median, ci95n=y_median,
        ci60p=y_median, ci60n=y_median,
        ci30p=y_median, ci30n=y_median,
        fuzz_size=0.01, color_levels=1,
        color=median_line_color,
        median_line_color=median_line_color,
        median_line_width=median_line_width,
        layout=layout,
    )

    solid_ci = FanPlotly(
        x, y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        ci60p=y_p_60, ci60n=y_n_60,
        ci30p=y_p_30, ci30n=y_n_30,
        color=color,
        median_line_color=median_line_color,
        median_line_width=median_line_width,
        layout=layout,
    )

    standard_error = StandardErrorPlot(
        x, y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        color='#e9f1fe',
        median_line_color=median_line_color,
        median_line_width=median_line_width,
        layout=layout,
    )

    fuzzy_fan = FuzzyPlotly(
        x, y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        ci60p=y_p_60, ci60n=y_n_60,
        ci30p=y_p_30, ci30n=y_n_30,
        fuzz_size=1, color_levels=50,
        color=color,
        median_line_color=median_line_color,
        median_line_width=median_line_width,
        layout=layout,
    )

    dens_chart = DensPlotly(
        x=x, y=y_median,
        ci95p=y_p_95,
        color_levels=20,
        output='offline',
        color=color,
        median_line_color=median_line_color,
        median_line_width=median_line_width,
        layout=layout,
    )

    # median_only.plot()
    # solid_ci.plot()
    # standard_error.plot()
    dens_chart.plot()
    # fuzzy_fan.plot()
