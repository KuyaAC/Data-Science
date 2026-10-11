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

# Subsetting rows and columns number using .iloc[]
print(dogs_ind.iloc[1:4, 0:2]) # Slicing rows 1 to 3 and columns 0 to 1

# Challenge 1:
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Philippines
print(temperatures_srt.loc["Pakistan":"Philippines"])

# Try to subset rows from Lahore to Manila
print(temperatures_srt.loc["Lahore":"Manila"])

# Subset rows from Pakistan, Lahore to Philippines, Manila
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Philippines", "Manila")])



# Challenge 2:
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,"date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad"),"date":"avg_temp_c"])

# Challenge 3: Slicing date
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])

# Challenge 4: slicing using .iloc[]
# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22:22,1:1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[0:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:,2:4])

# Use slicing in both directions at once
print(temperatures.iloc[0:5,2:4])


