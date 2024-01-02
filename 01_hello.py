# Ask user for their name
name = input("What's your name? ")
# name = input("What's your name? ").strip().title()        # also works

# Say hello to user
print("Hello,", name)
# print("Hello, " + name)               # this is concatenation
# print(*object, sep=" ", end='\n')       ----> actual print function's documentation

print("Hello, ", end="")                # end="" ---> tells how the string ends
print(name)

print("Hello,", name, sep="???")        # sep="" ---> tells how the words in string are seperated

print("Hello, \"friend\"")          # if we want to add quotations in a string

print(f"Hello, {name}")             # format string

name = name.strip()                 # remove whitespace from string
#           strip function removes the whitespaces from beginning and ending of the string & not from the middle of the string
print(f"Hello, {name}")

# name = name.strip().title()         # you can create chain of the functions (and all that works!)
name = name.capitalize()            # capitalize the string (only capitalizes the first word)
print(f"Hello, {name}")
name = name.title()                 # titlize the string (all the starting letter of the words are capitalized)
print(f"Hello, {name}")

# Split user's name into first name and last name
first, last = name.split(" ")
print(f"Hello, {first}")

print("\n\nThis is for checking whether all the changes are made to the GitHub or not.")
print("Hello! Again")