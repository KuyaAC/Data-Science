#Measuring the spread of data
# Variance - average distance from each data point to the data's mean.
# To calculate variance:
# Subtract mean from each data point.
dists =msleep['sleep_total'] - msleep['sleep_total'].mean()
#Then square each distance.
sq_dist = dist ** 2
#then sum the square distances
sum_sq_dist = np.sum(sq_dist)
#Finally, divide by the number of data points minus 1.
variance = sum_sq_dist / (len(msleep['sleep_total']) - 1)

#OR use:
np.var(msleep['sleep_total'], ddof=1)


#Standard Deviation - square root of variance.
np.sqrt(np.var(msleep['sleep_total'], ddof=1))
#OR use:
np.std(msleep['sleep_total'], ddof=1)


#Mean absolute deviation - average distance from each data point to the data's mean.
#Calculate mean absolute deviation:
dist = msleep['sleep_total'] - msleep['sleep_total'].mean()
abs_dist = np.abs(dist)
mean_abs_dist = np.mean(abs_dist)

#Quantiles - values that divide the data into equal parts.
np.quantile(msleep['sleep_total'], 0.5) #0.5 quantile is the median

#Quartiles - values that divide the data into four equal parts.
np.quantile(msleep['sleep_total'], [0, 0.25, 0.5, 0.75, 1])

import matplotlib.pyplot as plt
plt.boxplot(msleep['sleep_total'])
plt.show()

#Quantiles using np.linspace()
np.linspace(start, stop, num)

np.quantile(msleep['sleep_total'], [0, 0.2, 0.4, 0.6, 0.8, 1])

#is same as:

np.quantile(msleep['sleep_total'], np.linspace(0, 1, 6))
