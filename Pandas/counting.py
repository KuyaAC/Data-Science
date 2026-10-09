# Dropping duplicates
df.drop_duplicates(subset="name")

# Creating a unique list of names and breeds that visit the vet
unique_dogs = vet_visits.drop_duplicates(subset=["names", "breed"])
print(unique_dogs)
