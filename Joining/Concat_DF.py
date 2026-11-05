#How to concatenate two table vertically
#Basic Concatination (Vertically combined table)
pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=False, 
            keys=['Jan', 'Feb', 'Mar'])


#Concat tables with different columns names
pd.concat([inv_jan, inv_feb, inv_mar], join='inner')

#Challenge 1:
# Concatenate the tracks (sorted)
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               sort=True)
print(tracks_from_albums)

# Challenge 2:
# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums)

# Challenge 3:
# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               ignore_index=False,
                               sort=True, join='inner')
print(tracks_from_albums)