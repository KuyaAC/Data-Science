"""
Boolean expressions evaluate to either ``True`` or ``False``.  Python's
Boolean operators are ``and``, ``or``, and ``not``.
"""

# and: True only when both conditions are true.
has_ticket = True
is_old_enough = True
can_enter = has_ticket and is_old_enough
print(can_enter)  # True

# or: True when at least one condition is true.
is_weekend = False
is_holiday = True
day_off = is_weekend or is_holiday
print(day_off)  # True

# not: reverses a Boolean value.
is_raining = False
can_play_outside = np.logical_not(is_raining)
print(can_play_outside)  # True


# Functions that demonstrate the same logical operations.
def logical_and(first, second):
	"""Return True only when both values are true."""
	return np.logical_and(first, second)


def logical_or(first, second):
	"""Return True when at least one value is true."""
	return np.logical_or(first, second)


def logical_not(value):
	"""Return the opposite Boolean value."""
	return np.logical_not(value)


print(logical_and(True, False))  # False: both values are not true.
print(logical_or(False, True))   # True: at least one value is true.
print(logical_not(False))        # True: not False is True.


# Challenge 1:
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print((my_kitchen*2) < (your_kitchen*3))


#Challenge 2:
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))

