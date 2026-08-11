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
