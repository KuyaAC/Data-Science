# Setting Index:
movies = pd.read_csv('movies.csv', index_col=['id'])
print(movies.head())

movies_taglines = movies.merge(taglines, on='id', how='left')
print(movies_taglines.head())

