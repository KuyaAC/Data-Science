# Dropping duplicates
df.drop_duplicates(subset="name")

# Creating a unique list of names and breeds that visit the vet
unique_dogs = vet_visits.drop_duplicates(subset=["names", "breed"])
print(unique_dogs)

unique_dogs["breed"].value_counts(sort=True)

unique_dogs["breed"].value_counts(normalize=True)

# Filter out all the holiday dates without duplicate
holiday_dates = sale[sale["is_holiday"]].drop_duplicates(subset="date")
print(holiday_dates["date"].value_counts(sort=True, normalize=True))