#other join notes

#Right Join (return data matches the unique(id) on the right table)
tv_movies = movies.merge(tv_genre, how='right', left_on='id', right_on='movie_id')


#Outer Join (Return all rows data from both table regarding if there is a match on the data)
family_comedy = family.merge(comedy, on='movie_id', how='outer', suffixes=('_fam', '_com'))
 













