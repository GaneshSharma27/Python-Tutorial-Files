class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # # return (name, house)        # this is not a two values but a tuple, if you don't add parenthesis then also it is tuple
    # return [name, house]

    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return {"name": name, "house": house}       # making it more compact

    # ---------Using classes---------
    # student = Student()                 # here `student` is a object/instance
    student = Student(name, house)      # another way of writing it, making it more compact
    # student.name = input("Name: ")      # and `name` & `house` are its attributes/instance variables
    # student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()