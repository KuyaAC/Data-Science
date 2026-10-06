# Sort by weight and height
dogs_sorted = dogs.sort_values(['weight_kg', 'height_cm'], ascending=[True, False])

# Subset rows where height > 50 and breed is Labrador
tall_labradors = dogs[(dogs['height_cm'] > 50) & (dogs['breed'] == 'Labrador')]

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)

print(homelessness_fam.head())

# Sort homelessness by region (ascending),
# then by family_members (descending)
homelessness_reg_fam = homelessness.sort_values(
    ["region", "family_members"],
    ascending=[True, False]
)

# Print the top few rows
print(homelessness_reg_fam.head())

# subsetting (getting the columns you want)
variable = dataframe[["column1", "column2"]]

nding family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)

print(homelessness_fam.head())

# Sort homelessness by region (ascending),
# then by family_members (descending)
homelessness_reg_fam = homelessness.sort_values(
    ["region", "family_members"],
    ascending=[True, False]
)

# Print the top few rows
print(homelessness_reg_fam.head())

# subsetting (getting the columns you want)
variable = dataframe[["column1", "column2"]]
print(variable.head())

mountain_reg = dataframe[dataframe["region"] == "Mountain"]
print(mountain_reg)

# filtering in subsetting
greaterthan10k = dataframe[dataframe["volume"] > 10000]
print(greaterthan10k)

# Using AND (&) operator
basketball_player = player[(player["height"] > 180) & (player["weight"] < 90)]
print(basketball_player.head())

# Using OR (|) operator
tall_basketball_player = player[(player["height"] > 190) | (player["consider"] == "tall")]
print(tall_basketball_player)

# Using ISIN instead of OR operator
sweet = ("Cookies", "Candy", "Chocolate")
my_sweet_food = myFood[myFood["food"].isin(sweet)]
print(my_sweet_food)