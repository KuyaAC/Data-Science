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
