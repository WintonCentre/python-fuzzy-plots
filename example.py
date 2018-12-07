import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

points = [0.025, 0.2, 0.35, 0.5, 0.65, 0.8, 0.975]

# qnorm(p, mean = 0, sd = 1)
# scipy.stats.norm.ppf(q, loc=0, scale=1)

q = norm.ppf(points, loc=0, scale=1)
print(q)
# # std=2
# q2 = norm.ppf(points, loc=0, scale=2)
# q_double = q * 2
# print(q2==q_double)

# # mean=10, std=2
q_mean_10 = norm.ppf(points, loc=10, scale=2)

fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = norm.stats(moments='mvsk')

# # Display the probability density function (pdf):
# x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
# ax.plot(x, norm.pdf(x), 'r-', lw=5, alpha=0.6, label='norm pdf')

# Display the probability density function (pdf):
x_cdf = np.linspace(norm.cdf(0.01), norm.cdf(0.99), 100)
ax.plot(x_cdf, norm.pdf(x_cdf), 'r-', lw=5, alpha=0.6, label='norm cdf')

# plt.show()

e = 0.001
points_boundaries = [0.025-e, 0.025, 0.025+e,
                     0.2-e, 0.2, 0.2+e,
                     0.35-e, 0.35, 0.35+e,
                     0.5-e, 0.5, 0.5+e,   # use this to indicate the width of the central median line
                     0.65-e, 0.65, 0.65+e,
                     0.8-e, 0.8, 0.8+e,
                     0.975-e, 0.975, 0.975+e]
'''
# To draw these bands, layer them on top of each other from the (95 + e)% band upwards.
# We will also need to know what fill colour to apply to each band...more on this later.

[-1.97736843, -1.95996398, -1.94313375,
-0.84519854, -0.84162123,-0.83805467,
-0.38802167, -0.38532047,-0.38262208,
-0.00250663,   0.        ,  0.00250663,
0.38262208,  0.38532047,  0.38802167,
0.83805467,  0.84162123,  0.84519854,
1.94313375,  1.95996398, 1.97736843]
'''
q_boundaries = norm.ppf(points_boundaries, loc=0, scale=1)
