from fuzzy.core import FuzzyPlotly, DensPlotly, StandardErrorPlot, FanPlotly
from data_gen_sarah import create_data


if __name__ == '__main__':
    color = '#4286f4'
    median_color = '#004C99'
    median_width = 2

    x, x_label, y_median, y_p_95, y_n_95, y_p_30, y_n_30, y_p_60, y_n_60 = create_data()

    # x_label[0] = 'hello'
    # x_label[1] = 5

    # x_test = x[0:15]
    # x_label_test = x_label[0:15]

    # for ticks, change step size. so it only plots ticks on those parts.
    x_test = x[0::2]
    x_label_test = x_label[0::2]
    # x_label_test[2] = 'aaaaa <br> a'
    x_label_test = [x_label.replace('-', '<br>20') for x_label in x_label_test]

    print(x_test)
    print(x_label_test)

    layout = {
        'showlegend': False,
        'xaxis': {
            'title': 'Date',
            'titlefont': {
                'family': 'Arial, sans-serif',
                'size': 18,
                'color': 'black',
            },
            # 'ticktext':x_label,
            # 'tickvals':x,
            'ticktext':x_label_test,
            'tickvals':x_test,
            'showgrid':False,
            'showline': True,

            'tickmode':'array',
            'ticks': 'outside',
            'tickangle': 0,
            'showticklabels': True,
            # 'ticklen': 3,
            'tickwidth': 2,
            'tickcolor': '#000',

            'mirror': True,

            # 'nticks': 5, #tickmode has to be auto

            # 'tick0': 'hello',
            # 'dtick': 0.5,

            # 'tickformat': '%{n}f'
            # '':,
        },
        'yaxis': {
            'title': 'Unemployment (in thousands)',
            'titlefont': {
                'family': 'Arial, sans-serif',
                'size': 18,
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
        color=median_color,
        median_color=median_color,
        median_width=median_width,
        layout=layout,
    )

    solid_ci = FuzzyPlotly(
        x, y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        ci60p=y_p_60, ci60n=y_n_60,
        ci30p=y_p_30, ci30n=y_n_30,
        fuzz_size=0, fuzz_n=1,
        color=color,
        median_color=median_color,
        median_width=median_width,
        layout=layout,
    )

    #StandardErrorPlot StandardErrorPlot
    ci_95_only = StandardErrorPlot(
        x, y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        fuzz_size=1, fuzz_n=1,
        color='#e9f1fe',
        median_color=median_color,
        median_width=median_width,
        layout=layout,
    )

    # Fuzzy Fan
    fuzzy_fan = FuzzyPlotly(
        x, y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        ci60p=y_p_60, ci60n=y_n_60,
        ci30p=y_p_30, ci30n=y_n_30,
        fuzz_size=1, fuzz_n=100,
        color=color,
        median_color=median_color,
        median_width=median_width,
        layout=layout,
    )

    # DensPlotly. plotting pdf.
    # Full fuzz
    full_fuzz = DensPlotly(
        x_list=x, y_list=y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        fuzz_size=1, fuzz_n=100,
        output='offline',
        color=color,
        median_color=median_color,
        median_width=median_width,
        layout=layout,
    )

    # median_only.plot()
    solid_ci.plot()
    # ci_95_only.plot()
    # full_fuzz.plot()
    # fuzzy_fan.plot()

    # fan_test = FanPlotly(
    #     x, y_median,
    #     ci95p=y_p_95, ci95n=y_n_95,
    #     ci60p=y_p_60, ci60n=y_n_60,
    #     ci30p=y_p_30, ci30n=y_n_30,
    #     color=color,
    #     median_line_color=median_color,
    #     median_line_width=median_width,
    #     # layout=layout,
    # )
    #
    # print(y_p_95)
    # # fan_test.plot()
    #
    # # print(fan_test.data)
