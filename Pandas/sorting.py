# Sort by weight and height
dogs_sorted = dogs.sort_values(['weight_kg', 'height_cm'], ascending=[True, False])

# Subset rows where height > 50 and breed is Labrador
tall_labradors = dogs[(dogs['height_cm'] > 50) & (dogs['breed'] == 'Labrador')]