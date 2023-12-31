def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x        # commented-out else statement, then tightening the code if there's no exception 
            #                 it'll run this line and if there's an exception then 
            #                 it'll directly jump to except statement by skipping this line
        except ValueError:
            pass    # it'll prevent program from crashing if there's an exception, but it won't do anything
            #         it'll catch the exception but won't do anything
            # print("x is not an integer")
        # else:
        #     # break   # if there's no exception then it'll break out of the loop
        #     return x    # commented-out break since if there's no exception then
        #     #             instead of first break-out of loop then returning instead directly return the variable

main()
