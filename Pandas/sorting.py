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