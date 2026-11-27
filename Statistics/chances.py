#Measuring Chances:
#What is the probability of an event happening?
#Probability = number of favorable outcomes / total number of outcomes

#Setting random seed for reproducibility
np.random.seed(10)
sales_counts.sample()
#Output: random name selected from the sales_counts DataFrame


#Sampling with/without replacement in python:
sales_counts.sample(5, replace = True) #with replacement
sales_counts.sample(5, replace = False) #without replacement

# SAMPLING METHODS

# 1. WITH REPLACEMENT
# - Selected items are returned to the population.
# - The same item can be selected multiple times.
# Examples: Flipping a coin 3 times, rolling a die twice.

# 2. WITHOUT REPLACEMENT
# - Selected items are NOT returned to the population.
# - The same item cannot be selected again.
# Examples: Picking 3 people from 20, dealing cards, selecting products.

# PYTHON FUNCTIONS
import random

# With replacement
random.choices([1, 2, 3, 4, 5], k=3)

# Without replacement
random.sample([1, 2, 3, 4, 5], k=3)

# KEY DIFFERENCE:
# choices() = With replacement
# sample()  = Without replacement


#Kind of events:
#Independent events: the outcome of one event does not affect the outcome of another event.
#Dependeeeeent events: the outcome of one event affects the outcome of another event.

#Challenge 1:
# Count the deals for each product
counts = amir_deals['product'].value_counts()

# Calculate probability of picking a deal with each product
probs = counts / amir_deals.shape[0]
print(probs)

 #Challenge 2:
 # Set random seed
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5, replace = False)
print(sample_without_replacement)

# Challenge 2.5:
# Set random seed
np.random.seed(24)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5, replace = True)
print(sample_with_replacement)





