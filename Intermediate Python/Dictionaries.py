# Simple Dictionary Applications for Beginners

# 1. Student Information
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics", "Chemistry"]
}

print("Student Info:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Grade: {student['grade']}\n")

# 2. Product Inventory
inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 45,
    "grape": 20
}

print("Inventory:")
for fruit, quantity in inventory.items():
    print(f"{fruit}: {quantity} units")
print()

# 3. Phone Contacts
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

print("Contacts:")
print(f"Alice's number: {contacts['Alice']}")
print(f"Bob's number: {contacts['Bob']}\n")

# 4. Adding and Updating Dictionary Items
car = {"brand": "Toyota", "year": 2020}
car["color"] = "red"  # Add new key
car["year"] = 2021    # Update existing key

print(f"Car: {car}\n")

# 5. Checking if Key Exists
if "brand" in car:
    print("Brand is in the car dictionary")

# 6. Removing Items
del car["color"]
print(f"Car after deletion: {car}")

# Exercise ------------------------------------------------------------------------------
# Example of not having a dictionary
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

# Syntax:
my_dict = {
   "key1":"value1",
   "key2":"value2",
}

# Exercise 2
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

#ADDING TO DICTIONARY
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)

# DICTIONARY MANIPULATION (UPDATE, REMOVE)
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del europe['australia']

# Print europe
print(europe)

# DICTIONARY OF DICTIONARIES
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome', 'population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)

# PANDAS(high level data manipulation tool built on top of NumPy)
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = { 'country':names,
            'drives_right':dr,
            'cars_per_cap':cpc
            }

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# DATA FRAME (Specifying Row Labels)
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

# Importing Data from a CSV
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)

# Set index_col to 0 to use the first column as row labels
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)


# Dataframe Columns Accessing
Comlumns Accessing [ 'column_name' or ["column_name"] ]
# Sample
brics['country'] # returns a Series
brics[['country']] # returns a DataFrame

Row Accessing []
# Sample
brics[1:4] # returns rows 1 to 3

# Pandas DataFrame Indexing with loc and iloc
# LOC
# loc is label-based, which means that you have to specify rows and columns based on their row and column labels.

# Example: 
brics.loc['RU'] 
# returns the row corresponding to Russia, and brics.loc['RU', 'capital'] returns the capital of Russia.

brics.loc[['RU']]
# returns a DataFrame containing the row corresponding to Russia, and brics.loc[['RU'], ['country', 'capital']] 
#returns a DataFrame with the country and capital of Russia.

brics.loc[['RU', 'IN'], ['country', 'capital']]
# returns a DataFrame with the country and capital of Russia and India.

brics.loc[:, ['country', 'capital']]
# returns a DataFrame with the country and capital columns of all countries.


#ILOC
# iloc is integer position-based, so you have to specify rows and columns by their integer position values (0-based integer position).

brics.iloc[2]
# returns the row corresponding to Brazil, and brics.iloc[2, 3] returns the capital of Brazil.

brics.iloc[[1, 2, 3]]
# returns a DataFrame containing the rows corresponding to India, Brazil, and China.

brics.iloc[[1, 2, 3], [0, 2]]
# returns a DataFrame containing the country and area of India, Brazil, and China.

brics.iloc[:, [0, 2]]
# returns a DataFrame containing the country and area columns of all countries.


# Challenge 1:
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Challenge 2:
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

# Challenge 3: (loc and iloc)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JPN'])
print(cars.iloc[2])
# Print out observations for Australia and Egypt
print(cars[:])
print(cars.loc[['AUS', 'EG']])

# Challenge 4:
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR'],['drives_right'])

# Print sub-DataFrame
# print(cars[:])
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Challenge 5:
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])

