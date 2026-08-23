# Sample code in the video:
import numpy as np

np.logical_and(brics['area'] > 8, brics['area'] < 10) 
brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)]

# Challenge 1:
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)

# Challenge 2:
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)