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
