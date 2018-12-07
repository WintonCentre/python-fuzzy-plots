# https://www.datacamp.com/community/tutorials/pandas-read-csv

import pandas as pd
from random import randint

df = pd.read_csv("csv/unemployment 2012-2017.csv")
# print([i for i in range(len(list(df['People'])))])
# print(list(df['People']))
# print()
# print(df.mean())
# print(df.std())

print(list(df['sd']))


# upper 01
# print(list((df['People']+(randint(5, 15)/10))))
# lower 01
# print(list((df['People']-(randint(1, 15)/10))))


# upper 02
# print(list((df['People']+(randint(15, 55)/10))))
# lower 02
# print(list((df['People']-(randint(15, 25)/10))))
