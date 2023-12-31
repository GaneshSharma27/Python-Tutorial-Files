import csv

students = []
with open("19_students.csv", newline='') as file:  # Add newline='' for compatibility
    reader = csv.reader(file)
    # next(reader)  # Skip the header row
    for row in reader:
        students.append({"name": row[0], "home": row[1]})  # Access full address

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")