import csv

students = []

with open("19_students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

    # for line in file:
    #     name, home = line.rstrip().split(",")
    #     # students.append(f"{name} is in {house}")      # for sorting first created list named "students"
    #     # print(f"{name} is in {house}")                # this is before sorting directly printing the names from "19_students.csv"

    #     student = {}                                    # declaring dictionary named "student"
    #     student = {"name": name, "home": home}
    #     # dictionaries are indexed by using strings
    #     students.append(student)

# for student in sorted(students):
#     print(student)

# def get_name(student):              # defining function to sort according to the "name"
#     return student["name"]

# def get_house(student):              # defining function to sort according to the "house"
#     return student["house"]

for student in sorted(students, key=lambda student: student["name"]):  # "key" keyword in sorted() function is used to
    print(f"{student['name']} is from {student['home']}")              # sort according to the key's value
# `key=lambda student: student["name"]` is equivalent of the function `get_name`

# -------Another important thing is-------
# Using `get_name` (without function's parenthesis) -----> passes the function object itself and doesn't return any value
# Using `get_name()` -----> this means calling function
