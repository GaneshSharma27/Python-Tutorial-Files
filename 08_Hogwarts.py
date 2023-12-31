students = ["Hermione", "Harry", "Ron"]     # lists

# for student in students:        # as you noticed we're not naming the _ in place of student
#     print(student)              #       because we're using it in this command line

for i in range(len(students)):      # len(list_name) ---> this returns the length of the elements in the list
    print(i + 1, students[i])

# ---Dictionary---
students1 = {"Hermione": "Gryffindor", 
             "Harry": "Gryffindor", 
             "Ron": "Gryffindor",
             "Draco": "Slytherin"}

# print(students1["Hermione"])
# print(students1["Harry"])
# print(students1["Ron"])
# print(students1["Draco"])

for student1 in students1:
    print(student1, students1[student1], sep=", ")

students2 = [
    {"Name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
    {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
    {"Name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russell Terrier"},
    {"Name": "Draco", "House": "Slytherin", "Patronus": None},
]

for student2 in students2:
    print(student2["Name"], student2["House"], student2["Patronus"], sep=", ")
