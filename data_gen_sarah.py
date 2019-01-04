import pandas as pd
import numpy as np
from scipy.stats import norm


def generate_interval_point(p, center, std):
    point = [p]
    boundary_point = norm.ppf(point, loc=center, scale=std)
    # print(f'point: {point}, p: {p}, center: {center}, std: {std}, offset: {offset} ==> boundary_point: {boundary_point}')
    return boundary_point[0]


# Another one is to take median and std.

# Takes csv with CI and create data.
def create_data():
    df = pd.read_csv("csv/uk_unemployment_sarah.csv")

    # Creates std from given 95% CI. Assumes it follows normal curve
    df['std'] = df['95%CI'] /1000 / 1.96

    # print(list(df.dtypes.index))

    std = list(df['std'])
    # print(df['Number of unemployed people'])
    # print(df['Number of unemployed people']/1000)

    y = list(df['Number of unemployed people']/1000)
    # print(y)

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

    # print(y_median)
    # print("")
    #
    # print(y_p_95)
    # print(y_n_95)
    #
    # print(y_p_30)
    # print(y_n_30)
    #
    # print(y_p_60)
    # print(y_n_60)

    df['DateLabel'] = df['DateLabel'].replace(np.nan, '', regex=True)

    x = list(df['Date'])
    x_label = list((df['DateLabel']))

    return x, x_label, y_median, y_p_95, y_n_95, y_p_30, y_n_30, y_p_60, y_n_60


if __name__ == '__main__':
    date, date_label, y_median, y_p_95, y_n_95, y_p_30, y_n_30, y_p_60, y_n_60 = create_data()

    print('y_p_95')
    print(y_p_95)
    print('y_n_95')
    print(y_n_95)

    print('y_p_30')
    print(y_p_30)
    print('y_n_30')
    print(y_n_30)

    print('y_p_60')
    print(y_p_60)
    print('y_n_60')
    print(y_n_60)

    print()

    print('date')
    print(date)
    print('date_label')
    print(date_label)

    print()
    print('y_median')
    print(y_median)
