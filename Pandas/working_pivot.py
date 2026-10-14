#Working Pivot Tables
# Create a pivot table
pivot = dogs.pivot_table(values='height', index='breed', columns='color', aggfunc='mean')

# Subset the pivot table
subset = pivot.loc['Labrador']

# Calculate mean height across breeds
mean_height = pivot.mean(axis='columns')

#Challenge 1:

# Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(
    values="avg_temp_c",
    index=["country", "city"],
    columns="year"
)

# See the result
print(temp_by_country_city_vs_year)
