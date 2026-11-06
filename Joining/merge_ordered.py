#Merge_ordered
#Using fill method to fill value
import pandas as pd
pd.merge(table1, table2, on='id', suffixes=('_1','_2'), fill_method='fill')




