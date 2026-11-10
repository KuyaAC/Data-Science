#ASOF- match on the nearest key rather than equal keys. 
#This is useful for ordered data like time series.
pd.merge_asof(visa, ibm, on='date', suffixes=('_visa', '_ibm'), direction='forward')

# In Python's pd.merge_asof(), the direction parameter has 3 possible values:
# Direction	Short description
# 'backward'	Matches the last row with a key less than or equal to the left key.
# 'forward'	Matches the first row with a key greater than or equal to the left key.
# 'nearest'	Matches the row with the closest key, either before or after.

#Challenge 1:
# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on='date_time', direction='nearest', suffixes=('', '_wells'))


# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time', direction='nearest', suffixes=('_jpm', '_bac'))


# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm', 'close_wells', 'close_bac'])
plt.show()





