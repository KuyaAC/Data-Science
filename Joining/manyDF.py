# Merging many DF
# Single merge
grants.merge(license, on=["address", "zip"])

# Multiple Table merge
grants_license_wards = grants.merge(license, on=["address", "zip"]) \ 
                        .merge(wards, on="ward", suffixes=("_bus", "_ward"))

import matplotlib.pyplot as plt 
grants_license_wards.groupby("ward").agg("sum").plot(kind='bar', y='grant')
plt.show()

