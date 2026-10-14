#Working Pivot Tables
# Create a pivot table
pivot = dogs.pivot_table(values='height', index='breed', columns='color', aggfunc='mean')

# Subset the pivot table
subset = pivot.loc['Labrador']

# Calculate mean height across breeds
mean_height = pivot.mean(axis='columns')