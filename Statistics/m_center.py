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


