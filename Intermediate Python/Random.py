# Random coin flip
import numpy as np
# Set the seed
np.random.seed(123)
# Randomly generate a 0 or 1
coin = np.random.randint(0, 2) 
if coin == 1:
    print("Tao")
else:
    print("Ibon")

# Challenge 1: Print random float number
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)
rannum = np.random.rand()
# Generate and print random float
print(rannum)

# ----------------------------------------- Roll a dice challenge -----------------------------------------------
# Challenge 1: roll a dice
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
dice = np.random.randint(1,7)
dice2 = np.random.randint(1,7)
# Use randint() again
print(dice)
print(dice2)


# Instruction:
# Roll the dice. Use randint() to create the variable dice.
# Finish the if-elif-else construct by replacing ___:
# If dice is 1 or 2, you go one step down.
# if dice is 3, 4 or 5, you go one step up.
# Else, you throw the dice again. The number on the dice is the number of steps you go up.
# Print out dice and step. Given the value of dice, was step updated correctly?

# Code:
# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 and dice >= 3:
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)


