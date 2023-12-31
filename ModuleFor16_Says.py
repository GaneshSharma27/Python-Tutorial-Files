def main():
    hello("World")
    goodbye("World")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"GoodBye, {name}")

if __name__ == "__main__":
    main()

# __name__ 
# Special Python construct: __name__ is a built-in variable that indicates the script's namespace
# When this script is run, if it is the main program (not imported as a module), __name__ is set to "__main__"
