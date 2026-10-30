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