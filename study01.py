from fuzzy.core import FuzzyPlotly, FuzzPlotly
from data_gen_sarah import create_data


if __name__ == '__main__':
    color = '#dfe9fb'

    x, x_label, y_median, y_p_95, y_n_95, y_p_30, y_n_30, y_p_60, y_n_60 = create_data()

    # x_label[0] = 'hello'
    # x_label[1] = 5

    # x_test = x[0:15]
    # x_label_test = x_label[0:15]

    # for ticks, change step size. so it only plots ticks on those parts.
    x_test = x[0::2]
    x_label_test = x_label[0::2]

    # print(x_test)
    # print(x_label_test)

    layout = {
        'showlegend': False,
        'xaxis': {
            'title': 'Date',
            'titlefont': {
                'family': 'Arial, sans-serif',
                'size': 18,
                'color': 'grey',
            },
            # 'ticktext':x_label,
            # 'tickvals':x,
            'ticktext':x_label_test,
            'tickvals':x_test,
            'showgrid':False,

            'tickmode':'array',
            'ticks': 'outside',
            'tickangle': 45,
            'showticklabels': True,
            # 'ticklen': 3,
            'tickwidth': 2,
            'tickcolor': '#000',


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
                'color': 'grey',
            },
            'showgrid':False,
            'range': [1000000/1000, 2600000/1000],

        }
    }

    test_plot = FuzzyPlotly(
        x, y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        ci60p=y_p_95, ci60n=y_n_95,
        ci30p=y_p_95, ci30n=y_n_95,
        fuzz_size=1, fuzz_n=30,
        # color=color,
        layout=layout,
    )
    test_plot.create_data()

    test_plot_fuzzy = FuzzyPlotly(
        x, y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        ci60p=y_p_60, ci60n=y_n_60,
        ci30p=y_p_30, ci30n=y_n_30,
        fuzz_size=0.4, fuzz_n=10,
        # color=color,
        layout=layout,
    )
    test_plot_fuzzy.create_data()

    ci_95_only = FuzzyPlotly(
        x, y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        ci60p=y_p_95, ci60n=y_n_95,
        ci30p=y_p_95, ci30n=y_n_95,
        fuzz_size=0, fuzz_n=1,
        color=color,
        layout=layout,
    )
    ci_95_only.create_data()

    median_only = FuzzyPlotly(
        x, y_median,
        ci95p=y_median, ci95n=y_median,
        ci60p=y_median, ci60n=y_median,
        ci30p=y_median, ci30n=y_median,
        fuzz_size=0.01, fuzz_n=1,
        # color=color,
        layout=layout,
    )
    median_only.create_data()

    solid_ci = FuzzyPlotly(
        x, y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        ci60p=y_p_60, ci60n=y_n_60,
        ci30p=y_p_30, ci30n=y_n_30,
        fuzz_size=0, fuzz_n=1,
        # color=color,
        layout=layout,
    )
    solid_ci.create_data()

    fuzzy_fan = FuzzyPlotly(
        x, y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        ci60p=y_p_60, ci60n=y_n_60,
        ci30p=y_p_30, ci30n=y_n_30,
        fuzz_size=1, fuzz_n=50,
        # color=color,
        layout=layout,
    )
    fuzzy_fan.create_data()

    # Full fuzz
    full_fuzz = FuzzPlotly(
        x_list=x, y_list=y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        fuzz_size=1, fuzz_n=100,
        output='offline',
        # color=color,
        layout=layout,
    )
    full_fuzz.create_data()

    ### This is done by all lines being at center only. Pull this logic out and improve for publishing.
    # median_only.plot()

    ### Done by fuzz_size being so small and fuzz_n being 1 so no divisions. (or maybe 2 but fuzz is soooooo small eye can't see without impossible zooming)
    # solid_ci.plot()

    ### Only need ci_95, color to be same only. (Make fuzz_size=1, fuzz_n=1?). Changing color inside Fuzzy class currently. Capture that logic.
    # ci_95_only.plot()
    fuzzy_fan.plot()
    # full_fuzz.plot()

    # test_plot_fuzzy.plot()
    # test_plot.plot()

    # print('x')
    # print(x)
    # print('y_median')
    # print(y_median)
    # print('y_p_95')
    # print(y_p_95)
    # print('y_n_95')
    # print(y_n_95)


