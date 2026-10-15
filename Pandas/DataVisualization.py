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

# Layering plot and adding legend
dog_pack[dog_pack["sex"]=="F"]["height_cm"].hist()
dog_pack[dog_pack["sex"]=="M"]["height_cm"].hist()
plt.legend(["F", "M"])
plt.show()


