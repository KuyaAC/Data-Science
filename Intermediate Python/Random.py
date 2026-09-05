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
