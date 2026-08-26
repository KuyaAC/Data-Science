# for loop in a dictionary
world = {"afghanistan":32.0, "albania":2.9, "algeria":39.0, "andorra":0.7, "angola":124.0}

for country, population in world.items():
    print(f"{country} has a population of {population} million.")

# for loop in an numpy array
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
# Repeat once for each BMI value
for i in range(len(bmi)):
    # Print the person number and BMI rounded to two decimals
    print(f"Person {i+1} has a BMI of {bmi[i]:.2f}.")

