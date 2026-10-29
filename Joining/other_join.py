#other join notes

#Right Join
tv_movies = movies.merge(tv_genre, how='right', left_on='id', right_on='movie_id')