#Merge_ordered
#Using fill method to fill value
import pandas as pd
pd.merge(table1, table2, on='id', suffixes=('_1','_2'), fill_method='fill')


#Challenge 1:
# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left')

# Print gdp_sp500
print(gdp_sp500)









