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

#Challenge 2:
# Use merge_ordered() to merge gdp and sp500, and forward fill missing values
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp', 'returns']]

# Print gdp_returns correlation
print (gdp_returns.corr())

#Challenge 3:
# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, unemployment, on='date', how='inner',)

# Print inflation_unemploy 
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi
inflation_unemploy.plot(
    kind='scatter',
    x='unemployment_rate',
    y='cpi'
)
plt.show()

#Challenge 4:
# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp, pop, on=('date', 'country'), 
                             fill_method='ffill')

# Print ctry_date
print(ctry_date)

# Reverse the order of the merge and notice rows 2 and 3
# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=('country', 'date'), 
                             fill_method='ffill')

# Print date_ctry
print(date_ctry)








