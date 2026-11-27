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
