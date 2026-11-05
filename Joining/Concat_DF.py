#How to concatenate two table vertically
#Basic Concatination (Vertically combined table)
pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=False, 
            keys=['Jan', 'Feb', 'Mar'])


#Concat tables with different columns names
pd.concat([inv_jan, inv_feb, inv_mar], join='inner')


