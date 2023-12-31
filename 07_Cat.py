print("Using while loop:")
i1 = 0
while (i1 < 3):          # while loop
    print("Meow")
    i1 += 1

# ---For loop---
print("\nUsing for loop:")
for i in range(3):
    print("Meow")

# for _ in range(3):      # this works when you don't need to use the variable
#     print("Meow")       #       this is generally better for the programmer (and this won't generate any error)

print("\nWithout using the loops:")
print("Meow\n" * 3, end="")     # without using the for loop

while True:         # this will make the loop to iterate forever
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("Meow")

# ---Using functions---
print("\nUsing functions:")
def main():
    number = get_number()
    meow(number)

def get_number():
    while True: 
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()
