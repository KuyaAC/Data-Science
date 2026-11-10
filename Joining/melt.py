#melt
#melt allows us to unpivot our dataset.
social_fin_tall = social_fin.melt(id_vars=['financial', 'company'], value_vars=['2018', '2017'] var_name='year', value_name='revenue')

#Challenge 1:

# Unpivot everything except the year column
ur_tall = ur_wide.melt(
    id_vars=['year'],
    var_name='month',
    value_name='unempl_rate'
)

# Create a date column using year and month
ur_tall['date'] = pd.to_datetime(
    ur_tall['year'].astype(str) + '-' + ur_tall['month']
)

# Sort ur_tall by date
ur_sorted = ur_tall.sort_values('date')

# Plot unemployment rate by date
ur_sorted.plot(x='date', y='unempl_rate')
plt.show()