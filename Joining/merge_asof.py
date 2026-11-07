#ASOF- match on the nearest key rather than equal keys. 
#This is useful for ordered data like time series.
pd.merge_asof(visa, ibm, on='date', suffixes=('_visa', '_ibm'))





