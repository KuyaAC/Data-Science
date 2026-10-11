# Slicing list
breeds = ["Labrador Retriever", "Beagle", "Chihuahua", "Pug", "Golden Retriever"]
# Slicing the first three elements
print(breeds[0:3]) 
# slicing the last two elements
print(breeds[-2:])
# Slicing from the third element to the end
print(breeds[2:])
# Slicing the first three elements using shorthand
print(breeds[:3])
# Slicing all elements
print(breeds[:])

# Slicing DataFrames
#But first you need to sort the DataFrame by the index
dogs_ind = dogs.set_index("breeds").sort_index()

dogs_ind.loc["Beagle":"Chihuahua"] # Slicing from Beagle to Chihuahua

# Slicing inner level of a multi-level index
dogs_ind2 = dogs.set_index(["breed", "color"]).sort_index()
dogs_ind2.loc[("Beagle", "Tri-color"):("Chihuahua", "Fawn")] # Slicing from Beagle, Tri-color to Chihuahua, Fawn   


# Slicing columns
dogs_ind.loc[:, "height":"weight"] # Slicing from height to weight columns

# Slicing rows and columns
dogs_ind.loc["Beagle":"Chihuahua", "height":"weight"] # Slicing from Beagle to Chihuahua rows and height to weight columns
dogs_ind.loc[("Beagle","brown"):("Chihuahua","fawn"), "height":"weight"]
