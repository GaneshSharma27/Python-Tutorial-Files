x = int(input("What's x? "))
y = int(input("What's y? "))

# -----------If-else statements-----------
if (x < y):
    print("x is less than y")
elif (x > y):
    print("x is greater than y")
else:
    print("x is equal to y")

# ----Simpler and faster than the previous ones----
if (x < y or x > y):
    print("x is not equal to y")
else:
    print("x is equal to y")

# ----Most simplest and fastest way to compare----
if (x != y):
    print("x is not equal to y")
else:
    print("x is equal to y")


score = int(input("Score: "))

# This also works!
if (score >= 90 and score <= 100):
    print("Grade: A")
elif (score >= 80 and score < 90):
    print("Grade: B")
elif (score >= 70 and score < 80):
    print("Grade: C")
elif (score >= 60 and score < 70):
    print("Grade: D")
else:
    print("Grade: F")

# ----Tidy way of writing the code (this works in python)----
if (90 <= score <= 100):
    print("Grade: A")
elif (80 <= score < 90):
    print("Grade: B")
elif (70 <= score < 80):
    print("Grade: C")
elif (60 <= score < 70):
    print("Grade: D")
else:
    print("Grade: F")
