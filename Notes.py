"""
Python Notes for Beginners
=========================

Topics covered:
1. Python Basics
2. Python List
3. Functions and Packages
4. NumPy

How to use this file:
- Read the comments and examples.
- Run the code in Python to see the output.
- Try changing the values to practice.
"""

# =====================================================
# 1. PYTHON BASICS
# =====================================================

# Python uses variables to store data.
name = "Alice"
age = 25

# You can print values to see the output.
print("Name:", name)
print("Age:", age)

# Python has different data types.
number = 10
pi = 3.14
is_student = True

print("Number:", number)
print("Pi:", pi)
print("Is student:", is_student)

# Simple math operations.
print("Addition:", 5 + 3)
print("Subtraction:", 10 - 4)
print("Multiplication:", 6 * 2)
print("Division:", 8 / 2)

# Conditional statements help make decisions.
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# =====================================================
# 2. PYTHON LIST
# =====================================================

# A list stores multiple items in one variable.
fruits = ["apple", "banana", "orange"]
print("Fruits:", fruits)

# You can access items by index.
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# You can add items to a list.
fruits.append("grape")
print("Updated fruits:", fruits)

# You can remove items.
fruits.remove("banana")
print("After removing banana:", fruits)

# You can loop through a list.
for fruit in fruits:
    print("I like", fruit)


# =====================================================
# 3. FUNCTIONS AND PACKAGES
# =====================================================

# A function is a reusable block of code.
def greet(name):
    return "Hello, " + name

print(greet("Bob"))

# A function can also do simple calculations.
def add_numbers(a, b):
    return a + b

print("Sum:", add_numbers(3, 7))

# Packages are collections of useful code.
# Example: math package provides math functions.
import math

print("Square root of 16:", math.sqrt(16))
print("Pi value:", math.pi)


# =====================================================
# 4. NUMPY
# =====================================================

# NumPy is a package used for working with arrays and numbers.
# It is very useful in data science.
try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Install it with: pip install numpy")
else:
    # Create a NumPy array.
    arr = np.array([1, 2, 3, 4, 5])
    print("NumPy array:", arr)

    # Perform math on arrays.
    print("Array + 2:", arr + 2)
    print("Array squared:", arr ** 2)

    # Get the mean of the array.
    print("Mean:", np.mean(arr))

    # Create a 2D array.
    matrix = np.array([[1, 2], [3, 4]])
    print("Matrix:\n", matrix)


# Problem1:
# The baseball data is available as a 2D numpy array with 3 columns (height, weight, age) and 1015 rows. 
# The name of this numpy array is np_baseball. 
# After restructuring the data, however, you notice that some height values are abnormally high. 
# Follow the instructions and discover which summary statistic is best suited if you're 
# dealing with so-called outliers. np_baseball is available.

import numpy as np

# Create np_height_in from np_baseball
np_height_in = np.array(np_baseball[:, 0])

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))

# TIPS:(Getting columns from a 2D array)
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

column = matrix[:, 1]   # all rows, column index 1
print(column)  # [2 5 8]

# Multiple columns at once
cols = matrix[:, [0, 2]]  # columns 0 and 2

# TIPS: (Getting rows from a 2D array)
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

row = matrix[1]           # single row  → [4 5 6]
rows = matrix[0:2]        # row slice   → [[1,2,3],[4,5,6]]
rows = matrix[[0, 2]]     # specific rows by index → [[1,2,3],[7,8,9]]
