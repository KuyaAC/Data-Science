# Setting Index:
movies = pd.read_csv('movies.csv', index_col=['id'])
print(movies.head())

#Merging Index:
movies_taglines = movies.merge(taglines, on='id', how='left')
print(movies_taglines.head())

# Multi indexing:
samuel = pd.read_csv('samuel.csv', index_col=['movie_id', 'cast_id'])

cast = pd.read_csv('cast.csv', index_col=['movie_id', 'cast_id'])

samuel_cast = samuel.merge(cast, on=['movie_id', 'cast_id'])

# Index merge with left_on and right_on:
samuel_cast = samuel.merge(cast, left_on=['movie_id', 'cast_id']
                        left_index=True, right_on=['movie_id', 'cast_id'], 
                        right_index=True)

#CHallenge no 1:
# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, on='id', how='left')

# Print the first few rows of movies_ratings
print(movies_ratings.head())
