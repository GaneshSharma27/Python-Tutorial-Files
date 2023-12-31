import sys
# sys.argv() ---> This is command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# else:
#     print("Hello, My name is", sys.argv([1]))

for arg in sys.argv[1:]:
    print("Hello, My name is", arg)
