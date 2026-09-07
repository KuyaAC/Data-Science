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

# Solution:
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

# instruction:
# Make a list random_walk that contains the first step, which is the integer 0.
# Finish the for loop:
# The loop should run 100 times.
# On each iteration, set step equal to the last element in the random_walk list. You can use the index -1 for this.
# Next, let the if-elif-else construct update step for you.
# The code that appends step to random_walk is already coded.
# Print out random_walk.

# Solution:
# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Intruction:
# Use max() in a similar way to make sure that step doesn't go below zero if dice <= 2.
# Hit Submit Answer and check the contents of random_walk.


# Solution:
# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)

# Making the plot to the random walk
# NumPy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()


# Sample:
import numpy as np                    # Import NumPy for random numbers
import matplotlib.pyplot as plt       # Import Matplotlib for plotting

np.random.seed(123)                   # Set a fixed random seed
final_tails = []                      # Create an empty list for results

for x in range(10000):                # Repeat the experiment 10,000 times
    tails = [0]                       # Start the count at 0

    for x in range(10):               # Flip the coin 10 times
        coin = np.random.randint(0, 2) # Randomly generate 0 or 1
        tails.append(tails[x] + coin) # Add the coin result to the total

    final_tails.append(tails[-1])     # Save the final number of 1s

plt.hist(final_tails, bins=10)        # Create a histogram of the results
plt.show()                            # Display the histogram

# Challenge: Simulate multiple random walks
# NumPy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk five times
for i in range(5) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)

# Start plotting the results and transposing all_walks
# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(5) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()


# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()


# Implementing a clumsiness factor
# numpy and matplotlib imported, seed set

# clear the plot so it doesn't get cluttered if you run this many times
plt.clf()

# Simulate random walk 20 times
all_walks = []
for i in range(20) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.005 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()


# creating a histogram
# NumPy and Matplotlib are imported, and the random seed is set

# Simulate the random walk 500 times
all_walks = []  # Create an empty list to store all random walks

for i in range(500):  # Repeat the random walk 500 times

    random_walk = [0]  # Start each random walk at position 0

    for x in range(100):  # Make 100 steps in each random walk

        step = random_walk[-1]  # Get the current/last position

        dice = np.random.randint(1, 7)  # Roll a dice, generating a number from 1 to 6

        if dice <= 2:  # If the dice is 1 or 2
            step = max(0, step - 1)  # Move down 1 step, but never go below 0

        elif dice <= 5:  # If the dice is 3, 4, or 5
            step = step + 1  # Move up 1 step

        else:  # If the dice is 6
            step = step + np.random.randint(1, 7)  # Move up by a random number from 1 to 6

        if np.random.rand() <= 0.001:  # 0.1% chance of falling
            step = 0  # If you fall, go back to position 0

        random_walk.append(step)  # Add the new position to the random walk

    all_walks.append(random_walk)  # Store this completed random walk


# Convert all_walks to a NumPy array and transpose it
np_aw_t = np.transpose(np.array(all_walks))  # Turn rows into columns and columns into rows

# Select the last row from np_aw_t
ends = np_aw_t[-1, :]  # Get the final position of all 500 random walks

# Plot a histogram of the final positions
plt.hist(ends)  # Create a histogram showing how often each final position occurs

plt.show()  # Display the histogram