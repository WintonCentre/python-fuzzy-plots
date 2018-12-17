import pandas as pd
from scipy.stats import norm


df = pd.read_csv("csv/unemployment 2012-2017.csv")
# print(list(df['sd']))

# probability is between 0-1
# example p = [0.025, 0.2, 0.35, 0.5, 0.65, 0.8, 0.975]
def generate_interval_point(p, center, std, offset=0):
    point = [p+offset]
    boundary_point = norm.ppf(point, loc=center, scale=std)
    # print(f'point: {point}, p: {p}, center: {center}, std: {std}, offset: {offset} ==> boundary_point: {boundary_point}')
    return boundary_point[0]


std = list(df['sd'])
y = list(df['People'])
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


print(y_n_95)
print(y_median)
print(y_p_95)
