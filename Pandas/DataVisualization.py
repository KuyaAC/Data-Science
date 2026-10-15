#Visualizing data:
#Histogram:
import matplotlib.pyplot as plt
dogpack["height_cm"].hist()
plt.show()

# Adding bins
dogpack["height_cm"].hist(bins=20)
plt.show()

# Bar Plot:
average_weight_per_breed = dog_pack.groupby("breed")["weight_kg"].mean()
print(average_weight_per_breed)

average_weight_per_breed.plot(kind="bar", title="Average weight of the dog per breed")
plt.show()

# Line Plot (rotate 45 degree for better visual):
sully.head()
sully.plot(x="date", y="weight_kg", kind="line", rot=45)
plt.show()

# Scatter plot, better for comparing 2 numeric data
dog_pack.plot(x="height_cm", y="weight_kg", kind="scatter")
plt.show()

# Layering plot and adding legend, making chart translucent
dog_pack[dog_pack["sex"]=="F"]["height_cm"].hist(alpha=0.7)
dog_pack[dog_pack["sex"]=="M"]["height_cm"].hist(alpha=0.7)
plt.legend(["F", "M"])
plt.show()

# Challenge 1:
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar")

# Show the plot
plt.show()


