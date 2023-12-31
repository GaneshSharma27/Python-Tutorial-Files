name = input("What's your name? ")

# ---Using if-else statement---
# if (name == "Harry" or name == "Hermione" or name == "Ron"):
#     print("Gryffindor")
# elif (name == "Draco"):
#     print("Slytherin")
# else:
#     print("Who?")

# ---Using match-case statement---
#       Just like switch-case in C/C++
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
