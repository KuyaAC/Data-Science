#Filtering Join
#Starting with Semi Join (Semi Join = Keep matching rows.)
genres_tracks = genres.merge(track, on='gid')
#Check if there is matching values
genres['gid'].isin(genres_track['gid'])

genres_tracks = genres.merge(track, on='gid')
top_genres = genres[genres['gid].isin(genres_tracks['gid])]
print(top_genres.head())

#Anti-join = Keep non matching rows
genres_track = genres.merge(tracks, on='gid', how='left', indicator=True)
gid_list = genres_tracks.loc[genres_tracks['_merge'] == 'left_only', 'gid']
non_top_genres = genres[genres['gid'].isin(gid_list)]
























