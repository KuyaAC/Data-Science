#When do we need a self join:
#A self join in Python (Pandas) is used when you need to join a DataFrame with itself to identify relationships or compare records within the same dataset.

#Common examples:

#* Matching employees with their managers.
#* Finding relationships between students or customers.
#* Comparing records within the same dataset.
#* Finding related transactions.

#Example:

df.merge(df, left_on='manager_id', right_on='employee_id')

#Remember: Use a self join when one row references another row in the same DataFrame.

#More sample:
original_sequel = sequels.merge(sequels, left_on="id", right_on="seque",suffixes('_org', '_seq'))

#Format Result:
print(original_sequel[,['title_org', 'title_seq']].head()

#Challenge 1:
# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir','_crew'))

# Create a boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & 
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())


