"""Conditional statements in Python: beginner examples.

Conditional statements run different code depending on whether a condition is
True or False.
"""

# 1. if statement
age = 18
if age >= 18:
	print("You are an adult.")
# Explanation: The indented code runs only when the condition is True.


# 2. if-else statement
number = 7
if number % 2 == 0:
	print("The number is even.")
else:
	print("The number is odd.")
# Explanation: if handles the True case; else handles the False case.


# 3. if-elif-else statement
score = 85
if score >= 90:
	grade = "A"
elif score >= 80:
	grade = "B"
else:
	grade = "C or below"
print("Grade:", grade)
# Explanation: elif checks another condition if the previous one was False.


# 4. Nested if statement
logged_in = True
is_admin = True
if logged_in:
	if is_admin:
		print("You can access the admin page.")
# Explanation: A nested if is an if statement inside another if statement.


# Challenge 1:
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else :
    print("pretty small.")