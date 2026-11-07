#ASOF- match on the nearest key rather than equal keys. 
#This is useful for ordered data like time series.
pd.merge_asof(visa, ibm, on='date', suffixes=('_visa', '_ibm'), direction='forward')

# In Python's pd.merge_asof(), the direction parameter has 3 possible values:
# Direction	Short description
# 'backward'	Matches the last row with a key less than or equal to the left key.
# 'forward'	Matches the first row with a key greater than or equal to the left key.
# 'nearest'	Matches the row with the closest key, either before or after.





