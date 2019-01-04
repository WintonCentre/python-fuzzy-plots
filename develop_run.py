from fuzzy.core import FuzzyPlotly
from data_gen_sarah import create_data


if __name__ == '__main__':
    color = '#ff0000'

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

    fuzzy_fan = FuzzyPlotly(
        x, y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        ci60p=y_p_60, ci60n=y_n_60,
        ci30p=y_p_30, ci30n=y_n_30,
        fuzz_size=0.7, fuzz_n=70, color=color,
        layout=layout,
    )
    fuzzy_fan.create_data()

    fuzzy_fan.plot()
