#melt
#melt allows us to unpivot our dataset.
social_fin_tall = social_fin.melt(id_vars=['financial', 'company'], value_vars=['2018', '2017'])
