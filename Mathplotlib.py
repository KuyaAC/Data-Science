#Mathplotlib Exercise
# Print the last item from year and pop
print(year[-1])
print(pop[-1])


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()

# Exercise 2 (already imported matplotlib.pyplot as plt)
# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])


# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()

# Using Scatter Plots
import matplotlib.pyplot as plt

plt.scatter(gdp_cap, life_exp)
plt.show()


# Histograms
# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()

# exercise 2(histograms)
# Build histogram with 5 bins
plt.hist(life_exp, bins=5)

# Show and clean up plot and to start fresh again
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins=20)

# Show and clean up again
plt.show()
plt.clf()

# Customizing Plots
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)


# Add title
plt.title(title)

# After customizing, display the plot
plt.show()



