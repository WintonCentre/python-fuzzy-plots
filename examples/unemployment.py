from fuzzy.core import FuzzyPlotly, DensPlotly, StandardErrorPlot, FanPlotly
from examples.generate_data import create_data


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
        # 'title': 'UK Migration figures (2013-2018)',
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
        fuzz_size=0.01, fuzz_n=1,
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
        fuzz_size=1, fuzz_n=50,
        color=color,
        median_line_color=median_line_color,
        median_line_width=median_line_width,
        layout=layout,
    )

    # DensPlotly. plotting pdf.
    # Full fuzz
    dens_chart = DensPlotly(
        x_list=x, y_list=y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        fuzz_n=100,
        output='offline',
        color=color,
        median_line_color=median_line_color,
        median_line_width=median_line_width,
        layout=layout,
    )

    # median_only.plot()
    # solid_ci.plot()
    # standard_error.plot()
    # dens_chart.plot()
    fuzzy_fan.plot()
