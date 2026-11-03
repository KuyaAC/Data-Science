#Filtering Join
#Starting with Semi Join
genres_tracks = genres.merge(track, on='gid')
#Check if there is matching values
genres['gid'].isin(genres_track['gid'])

genres_tracks = genres.merge(track, on='gid')
top_genres = genres[genres['gid].isin(genres_tracks['gid])]
print(top_genres.head())























