def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n
    # return n ** 2         # double astrick means n raised to 2
    # return pow(n, 2)      # pow() function here first argument is the base and other argument is the power

main()
