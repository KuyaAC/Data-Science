# Setting a column as index
dogs_ind = dogs.set_index("name")
print(dogs_ind.head())

# Resetting the index
dogs_reset = dogs_ind.reset_index()
print(dogs_reset.head())

#ressetting and dropping the index
dogs_reset_drop = dogs_ind.reset_index(drop=True)
print(dogs_reset_drop.head())

# Setting index makes subsetting easier
print(dogs_ind.loc[["Fido", "Buddy"]])

#Multi level index
dogs_ind2 = dogs.set_index(["breed", "color"])
print(dogs_ind2.head())

#Inner level index
dogs_ind2.loc[[("Labrador Retriever", "Golden Retriever"), ("Beagle", "Tri-color")]]

#Controling sorting of index
dogs_ind2 = dogs.set_index(["breed", "color"], ascending=[True, False])

# Challenge 1:
# Look at temperatures
print(temperatures)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

# Challenge 2:
# Make a list of cities to subset on
cities = ["London", "Paris"]

# Subset temperatures using square brackets(using isin())
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

# Challenge 3" Setting multi level index
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

# Challenge 4: Sorting a multi level index
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))

# Sort temperatures_ind by ascending country then descending city
print(temperatures_ind.sort_index(level=["country", "city"], ascending=[True, False]))
