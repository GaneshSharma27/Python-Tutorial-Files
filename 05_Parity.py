def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# ---Simple using if-else statement---
# if (x % 2 == 0):
#     print("Even")
# else:
#     print("Odd")

# ---Boolean expression function---
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# ---Short hand if-else---
# def is_even(n):
#     return True if (n % 2 == 0) else False

# def is_even(n):
#     return n % 2 == 0

main()
