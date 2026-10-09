# Using Group BY
dogs.groupby("color")["weight_kg"].mean()
dogs.groupby("color")["weight_kg"].agg([min,max,sum])

# Grouping multiple variable
dogs.groupby(["color", "breed"])["weight_kg"].mean()
dogs.groupby(["color", "breed"])[["weight_kg", "height_cm"]].mean()
