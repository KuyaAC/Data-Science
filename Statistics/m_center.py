#Challenge 1:
# Import numpy with alias np
import numpy as np

# Subset country for USA: usa_consumption
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Calculate mean consumption in USA
print(np.mean(usa_consumption['consumption']))

# Calculate median consumption in USA
print(np.median(usa_consumption['consumption']))

#Challenge 2:
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Subset food_consumption to get rows where food_category is 'rice'
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Create a histogram of co2_emission
rice_consumption['co2_emission'].hist()

# Display the plot
plt.show()

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption['co2_emission'].agg(['mean', 'median']))


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

