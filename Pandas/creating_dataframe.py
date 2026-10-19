#Data frame creation
#List of dictionaries (by row)
students = [
    {"name": "Alice", "age": 21, "course": "Computer Science"},
    {"name": "Bob", "age": 22, "course": "Information Technology"},
    {"name": "Charlie", "age": 20, "course": "Data Science"}
]

new_students = pd.DataFrames(students)
print(new_students)

#Dictionaries of list(by columns)
students = [
    {"name": ["Alice", "Bob", "Charlie"]},
    {"age": [21, 22, 20]},
    {"course": ["Computer Science", "IT", "Data Science"]}
]

new_students = pd.DataFrames(students)
print(new_students)

# Challenge 1:

# Create a list of dictionaries with new data
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-0", "small_sold": 10717154, "large_sold": 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)

#Challenge 2:
# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17", "2019-12-01"],
  "small_sold": [10859987,9291631],
  "large_sold": [7674135, 6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)

#Challenge in Reading CSV
# From previous steps
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Print airline_totals
print(airline_totals)











