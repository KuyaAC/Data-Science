# Merging many DF
# Single merge
grants.merge(license, on=["address", "zip"])

# Multiple Table merge
grants_license_wards = grants.merge(license, on=["address", "zip"]) \ 
                        .merge(wards, on="ward", suffixes=("_bus", "_ward"))

import matplotlib.pyplot as plt 
grants_license_wards.groupby("ward").agg("sum").plot(kind='bar', y='grant')
plt.show()

#Challenge 1:
# Merge the ridership and cal tables
ridership_cal = ridership.merge(cal, on=['day', 'month', 'year'])

#Challenge 2:
# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
            				.merge(stations, on='station_id')

#Challenge 3:
# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
							.merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7) 
                   & (ridership_cal_stations['day_type'] == 'Weekday') 
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())
















