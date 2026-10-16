# Missing value
# Detecting Missing Value
dogs.isna()
# Detect any missing value
dogs.isna().any()
# Counting Missing Value
dogs.isna().sum()

# Plotting Missing Value
import matplotlib.pyplot as plt
dogs.isna().sum().plot(kind="bar")
plt.show()

# Remove missing Value
dogs.dropna()

# Replace Missing Value
dogs.fillna(0)

# Challenge 1:
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind="bar")

# Show plot
plt.show()



