def main():
    print_column(3)
    print_rows(4)
    print_square(3)

def print_column(height):
    print("#\n" * height, end="")

def print_rows(width):
    print("#" * width)

def print_square(size):
    print("For square:")
    for i in range(size):
        print_rows(size)

main()
