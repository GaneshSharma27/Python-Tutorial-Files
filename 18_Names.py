# For writing and appending the names in 18_names.txt
name = input("What's your name? ")
# file = open("18_names.txt", "a")       # here "w" means open file in write mode and "a" means open in append mode
#                                     "w" will keep on rewrite the name in the file
#                                     "a" will keep on appending the name in the file
with open("18_names.txt", "a") as file:    # using "with" keyword which directly closes the file as done executing
    file.write(f"{name}\n")
# file.close()      # this helps in closing the file after executing the line

# For sorting the names (from file) not in file but in a newly declared list
names = []

with open("18_names.txt", "r") as file:     # "r" means open the file in read mode
#                                          you can also not write "r" by default when you open file it'll be in read mode
    for line in file:
        names.append(line.rstrip())

# # For directly sorting the names in the file
# with open("18_names.txt") as file:
#     for line in sorted(file):
#         print("Hello,", line.rstrip())

# For reading the names from newly declared list
for name in sorted(names, reverse=True):      # "reverse=True" in for sorting it in reverse
    print(f"Hello, {name}")
