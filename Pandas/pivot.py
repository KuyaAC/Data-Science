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

#Challenge 2:
# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=["mean", "median"])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

#Challenge 3:
# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

#Challenge 4:
# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="type", columns="department", fill_value=0, margins=True))

#Challenge 5:
# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))

























