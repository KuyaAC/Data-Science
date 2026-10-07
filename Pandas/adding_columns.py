# Adding Columns to a DataFrame
dogs["bmi"] = dogs["weight_kg"] / (dogs["height_cm"] / 100) ** 2
print(dogs.head())


# Multiple  Manipulations
bmi_lt_100 = dogs[(dogs["bmi"] < 100)]
bmi_lt_100_height = bmi_lt_100.sort_values("height_cm", ascending=False)
bmi_lt_100_height[["name", "height_cm", "bmi"]]

# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_homeless col as proportion of total homeless population to the state population
homelessness["p_homeless"] = homelessness["total"] / homelessness["state_pop"]

# See the result
print(homelessness)