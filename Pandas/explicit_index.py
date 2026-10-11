# Setting a column as index
dogs_ind = dogs.set_index("name")
print(dogs_ind.head())

# Resetting the index
dogs_reset = dogs_ind.reset_index()
print(dogs_reset.head())

# Setting index makes subsetting easier
print(dogs_ind.loc[["Fido", "Buddy"]])

#Multi level index
dogs_ind2 = dogs.set_index(["breed", "color"])
print(dogs_ind2.head())

#Inner level index
dogs_ind2.loc[[("Labrador Retriever", "Golden Retriever"), ("Beagle", "Tri-color")]]

#Controling sorting of index
dogs_ind2 = dogs.set_index(["breed", "color"], ascending=[True, False])
