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


# Challenge 2:
# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())

# Challenge 3:
# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].plot(kind="hist")

# Show the plot
plt.show()


