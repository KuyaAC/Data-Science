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

#Challenge 4:
# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat(
    [inv_jul, inv_aug, inv_sep],
    keys=['7Jul', '8Aug', '9Sep']
)

# Group invoices by index keys and calculate average
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg(
    {'total': 'mean'}
)

# Bar plot
avg_inv_by_month.plot(kind='bar')
plt.show()

#Verifying Data in pd.concat() means checking the concatenated DataFrame to all rows and columns are correctly combined, no unexpected duplicates or missing values exist, and the resulting data is accurate and consistent.
tracks.merge(specs, on='tid', validate='one_to_one')
#This check the duplicate and give error message
df.concat(verify_integrity=True)

#Show the duplicates rows in the table
pd.concat([inv_feb,inv_mar], verify_integrity=False












































