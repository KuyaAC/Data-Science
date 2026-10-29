#other join notes

#Right Join (return data matches the unique(id) on the right table)
tv_movies = movies.merge(tv_genre, how='right', left_on='id', right_on='movie_id')


#Outer Join (Return all rows data from both table regarding if there is a match on the data)
family_comedy = family.merge(comedy, on='movie_id', how='outer', suffixes=('_fam', '_com'))

#Challenge 1:
# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                suffixes=('_act', '_sci'))

# Print the first few rows of action_scifi to see the structure
print(action_scifi.head())
 













