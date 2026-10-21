# Which NYC schools have the best math results?

#     The best math results are at least 80% of the *maximum possible score of 800* for math.
#     Save your results in a pandas DataFrame called best_math_schools, including "school_name" and "average_math" columns, sorted by "average_math" in descending order.

# What are the top 10 performing schools based on the combined SAT scores?

#     Save your results as a pandas DataFrame called top_10_schools containing the "school_name" and a new column named "total_SAT", with results ordered by "total_SAT" in descending order ("total_SAT" being the sum of math, reading, and writing scores).

# Which single borough has the largest standard deviation in the combined SAT score?

#     Save your results as a pandas DataFrame called largest_std_dev.
#     The DataFrame should contain one row, with:
#         "borough" - the name of the NYC borough with the largest standard deviation of "total_SAT".
#         "num_schools" - the number of schools in the borough.
#         "average_SAT" - the mean of "total_SAT".
#         "std_SAT" - the standard deviation of "total_SAT".
#     Round all numeric values to two decimal places.



# Importing Data:
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# How to approach the project
# 1. Finding schools with the best math scores
best_math_schools = schools.copy()
best_math_schools["math_percent"] = best_math_schools["average_math"] / 800 * 100
# Atleast > 80%
best_math_schools = best_math_schools[best_math_schools["math_percent"] > 80]
best_math_schools = best_math_schools.sort_values("math_percent", ascending=False)
best_math_schools[["school_name", "average_math"]]

# 2. Identifying the top 10 performing schools
# Step 2:
# Identifying SAT Score
top_10_schools = schools.copy()
top_10_schools["total_SAT"] = top_10_schools["average_math"] + top_10_schools["average_reading"] + top_10_schools["average_writing"]
top_10_schools = top_10_schools.sort_values("total_SAT", ascending=False)
# printing top 10 school based on total SAT
top_10_schools[["school_name", "total_SAT"]].head(10)

# 3. Locating the NYC borough with the largest standard deviation in SAT performance



