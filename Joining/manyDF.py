# Merging many DF
# Single merge
grants.merge(license, on=["address", "zip"])

# Multiple Table merge
grants_license_wards = grants.merge(license, on=["address", "zip"]) \ 
                        .merge(wards, on="ward", suffixes=("_bus", "_ward"))
