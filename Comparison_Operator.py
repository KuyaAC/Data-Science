"""Comparison operators compare two values and return True or False."""

first_number = 10
second_number = 5

# Equal to (==): checks whether two values are the same.
print(first_number == second_number)  # False

# Not equal to (!=): checks whether two values are different.
print(first_number != second_number)  # True

# Greater than (>): checks whether the left value is larger.
print(first_number > second_number)  # True

# Less than (<): checks whether the left value is smaller.
print(first_number < second_number)  # False

# Greater than or equal to (>=): checks whether the left value is larger
# or the same.
print(first_number >= 10)  # True

# Less than or equal to (<=): checks whether the left value is smaller
# or the same.
print(second_number <= 5)  # True

# Challenge 1:
# Comparison of integers
x = -3 * 6
print(x > -10)

# Comparison of strings
y = "test"
print("test" <= y)

# Comparison of booleans
print(True > False)

# Challenge 2:
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)