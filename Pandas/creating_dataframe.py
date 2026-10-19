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
