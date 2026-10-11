#Pivot tables using pandas
dogs.pivot_table(values="weight_kg", index ="color")

#Using agg function
dogs.pivot_table(values="weight_kg", index ="color", aggfunc="median")
dogs.pivot_table(values="weight_kg", index ="color", aggfunc=["median", "mean"])

#groupby in pivot table, fill value is to avoid NaN output in the table, margin give last column a mean of the entire row
dogs.pivot_table(values="weight_kg", index ="color", columns="breed", fill_value=0, margins=True)

#Challenge 1:
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

# Print mean_sales_by_type
print(mean_sales_by_type)






