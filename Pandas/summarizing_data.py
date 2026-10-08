# Average
df["height_cm"].mean().median().max().min().mode().std().var()
print(height_cm)

# Using aggregate:
def pct30(column):
    return.column.quantile(0.3)

df["weight_kg"].agg(pct30)
# Result: 30% of the weight_kg

df[["weight_kg", "height_cm"]].agg(pct30)
# Result: 30% of the weight_kg & height_cm

def pct30(column):
    return.column.quantile(0.4)

df["weight_kg"].agg([pct30, pct40])
# PCT30    22.5 (30% of the weight_kg)
# PCT40    12.8 (40% of the wight_kg)

# Cumulutative Sum
df["numbers"].cumsum()

# Can also use .cummax() .cummin() .cumprod()




