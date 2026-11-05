#How to concatenate two table vertically
#Basic Concatination (Vertically combined table)
pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=True, 
            keys=['Jan', 'Feb', 'Mar'])
            
