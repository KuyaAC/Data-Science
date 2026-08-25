"""Examples of the main loop patterns available in Python.

Each section contains a small example and an explanation in comments.
"""


# 1. ``for`` loop: repeats once for every item in an iterable.
for fruit in ["apple", "banana", "cherry"]:
	print(fruit)
# The loop visits each list item in order, assigning it to ``fruit``.


# 2. ``for`` loop with ``range``: repeats a known number of times.
for number in range(1, 4):
	print(f"Number: {number}")
# ``range(1, 4)`` produces 1, 2, and 3; the stop value is excluded.


# 3. ``while`` loop: repeats while its condition remains True.
count = 3
while count > 0:
	print(f"Countdown: {count}")
	count -= 1
# Updating ``count`` is essential; otherwise the condition could stay True forever.


# 4. Nested loop: a loop inside another loop.
for row in range(2):
	for column in range(3):
		print(f"({row}, {column})")
# The inner loop completes all its iterations for each outer-loop iteration.


# 5. ``break``: stops the nearest loop immediately.
for number in range(1, 6):
	if number == 3:
		break
	print(number)
# Only 1 and 2 are printed because the loop ends when number becomes 3.


# 6. ``continue``: skips the rest of the current iteration.
for number in range(1, 6):
	if number % 2 == 0:
		continue
	print(number)
# Even numbers are skipped, so only odd numbers are printed.


# 7. ``else`` with a loop: runs when the loop finishes without ``break``.
for number in range(3):
	print(number)
else:
	print("The loop completed normally.")
# If a ``break`` occurred, the loop's ``else`` block would not run.


# 8. Looping through a dictionary with ``items``.
scores = {"Ada": 95, "Linus": 88}
for name, score in scores.items():
	print(f"{name}: {score}")
# ``items()`` provides each key and value together.


# 9. Comprehension: a compact loop that creates a new collection.
squares = [number * number for number in range(1, 4)]
print(squares)
# This is equivalent to a ``for`` loop that appends each square to a list.


# Challenge 1: (while loop)
# Initialize offset
offset = 8


# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)