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

# for loop in 2D numpy array(using the array above)
meas = np.array([np_height, np_weight])
for val in np.nditer(meas):
    print(val)

# Challenge 1:
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for x, y in europe.items():
    print("the capital of " + x +" is " + y)

# Challenge 2:
# Import numpy as np
import numpy as np

# For loop over np_height
for x in np_height:
    print(str(x) + " inches")

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)
# ----------------------- PART 2 -----------------------
# for loop in a pandas dataframe
import pandas as pd
brics = pd.read_csv("brics.csv", index_col=0)
for label, row in brics.iterrows():
    brics.loc[label, "name_lenght"] = len(row["country"])
print(brics)



