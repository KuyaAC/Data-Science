#Pivot tables using pandas
dogs.pivot_table(values="weight_kg", index ="color")

#Using agg function
dogs.pivot_table(values="weight_kg", index ="color", aggfunc="median")
dogs.pivot_table(values="weight_kg", index ="color", aggfunc=["median", "mean"])








