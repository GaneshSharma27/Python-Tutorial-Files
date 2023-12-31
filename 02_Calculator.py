x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

x1 = float(input("What's x? "))
y1 = float(input("What's y? "))

z1 = x / y
print(f"{z1:.2f}")      # from documentation, .2f denotes how many decimal ploces to print

# round(number[, ndigits]) ---> for rounding off the float number
#       it takes one argument and whatever inside the [] is optional and it is number of digits to round off
# round(x / y, 2)

# ----------Functions----------
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to = "world"):
    print("Hello,", to)
# if you assign any string, int, float to function argument then it's a default value
#       in case if it user doesn't provide any function parameter then function will by default take the value assigned

main()      # inorder to run code even if function call is made before defining the function
#       here hello() is called before defining the hello() function then this trick can be used
