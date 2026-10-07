# Adding Columns to a DataFrame
dogs["bmi"] = dogs["weight_kg"] / (dogs["height_cm"] / 100) ** 2
print(dogs.head())
