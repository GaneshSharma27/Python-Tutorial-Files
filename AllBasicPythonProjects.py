# --------------Program to calculate compound interest--------------
print("\nProgram to calculate compound interest")

principal = float(input("Enter the amount: "))
interestRate = float(input("Enter the rate of interest (annually): "))
time = float(input("Enter the time period: "))
bracesTerm = (1 + (interestRate/100))
raisedToTime = bracesTerm ** time
amount = principal * raisedToTime
print(f"\nYour Amount is {amount}")



# --------------Program to list down all the prime numbers between given interval--------------
print("\nProgram to list down all the prime numbers between given interval")

initial = int(input("Enter the initial interval: "))
final = int(input("Enter the final interval: "))

for num in range(initial, final + 1):
    if num == 2 or num == 3 or num == 5:
        print(num)
    else:
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                break
        if (num % j != 0):
            print(num)
        else:
            continue



# --------------Program to convert any decimal number into binary number--------------
print("\nProgram to convert any decimal number into binary number")

decimal_num = int(input("Enter a decimal number: "))
binary_num = bin(decimal_num)[2:]
print(f"Binary representation: {binary_num}")



# --------------Program to find out the cube of any number--------------
print("\nProgram to find out the cube of any number")
def getNumber():                                # made a function so that it can be used multiple times
    return int(input("Enter any number: "))     # part of the function :) just call "getNumber()"

def cube(num1):
    return num1 ** 3
print(f"The cube is {cube(getNumber())}")



# --------------Program to check if the given number is prime or not--------------
print("\nProgram to check if the given number is prime or not")

primeNumber = int(input("Enter the number: "))

def checkPrime(primeNumber):
    if (primeNumber == 2 or primeNumber == 3 or primeNumber == 5):
        print("Prime")
    elif (primeNumber % 2 == 0 or primeNumber % 3 == 0):
        print("Not prime")
    else:
        for i in range(2, primeNumber // 2):
            break
        if (primeNumber % i == 0):
            print("Not prime")
        else:
            print("Prime")

checkPrime(primeNumber)



# -----------------Program to find out factorial of a number-----------------
print("\nProgram to find out factorial of a number")
def factorial(number):
    if (number == 0 or number == 1):
        return 1
    elif (number == 2):
        return 2
    else:
        return number * factorial(number - 1)
print(factorial(getNumber()))



# ------------------Program to find out the area of any shape------------------
print("Which shape you want to find the area of (Type in the Option):")
print("1. Rectangle")
print("2. Square")
print("3. Circle")
print("4. Cylinder")
print("5. Sphere")
print("6. Triangle")
x = int(input(">>> "))

match(x):
    case 1:
        rectangleLength = int(input("Enter the length of the rectangle: "))
        rectangleBreadth = int(input("Enter the breadth of the rectangle: "))
        print(f"Area of the rectangle: {rectangleLength * rectangleBreadth}")
    case 2:
        squareSide = int(input("Enter the length of the side: "))
        print(f"Area of the square: {squareSide * squareSide}")
    case 3:
        circleRadius = int(input("Enter the radius of the circle: "))
        print(f"Area of the circle: {3.14 * circleRadius * circleRadius}")
    case 4:
        cylinderRadius = int(input("Enter the radius of the cylinder: "))
        cylinderHeight = int(input("Enter the height of the cylinder: "))
        print(f"Area of the cylinder: {(2 * 3.14 * cylinderRadius * cylinderHeight) + (2 * 3.14 * cylinderRadius * cylinderRadius)}")
    case 5:
        sphereRadius = int(input("Enter the radius of the sphere: "))
        print(f"Area of the sphere: {4 * 3.14 * sphereRadius * sphereRadius}")
    case 6:
        triangleBase = int(input("Enter the base of the triangle: "))
        triangleHeight = int(input("Enter the height of the triangle: "))
        print(f"Area of the triangle: {1/2 * triangleBase * triangleHeight}")
    case _:
        print("Enter valid input!")



# ------------------Program to keep check on the expenses------------------
print("\nProgram to keep check on the expenses:")
# Roadmap 
#       Ask what is there income per month
#       Take input on amount they spend on food, commute, subscriptions, bills, utilities, clothes, miscellaneous
#       Calculate money left after their spending -- if savings < 10 % of their then they're low on their savings
#       Suggest things on which they can cut the expenses -- after calculating which of the thing is taking the most in the expenses

income = int(input("Enter what you make/month: "))

food = int(input("Enter the amount spend on food/month: "))
percentageFood = ((food / income) * 100)

commute = int(input("Enter the amount spend on commute/month: "))
percentageCommute = ((commute / income) * 100)

subscriptions = int(input("Enter the amount spend on subscriptions (Netflix/Amazon Prime/Gym/Coursera/etc.): "))
percentageSubscription = ((subscriptions / income) * 100)

bills = int(input("Enter the amount spend on bills (Mobile Recharge/Electricity bills/Maintanance/etc.): "))
percentageBills = ((bills / income) * 100)

utilities = int(input("Enter the amount spend on utilities: "))
percentageUtilities = ((utilities / income) * 100)

clothes = int(input("Enter the amount spend on clothes: "))
percentageClothes = ((clothes / income) * 100)

misc = int(input("Enter the amount spend on miscellaneous: "))
percentageMisc = ((misc / income) * 100)

percentageSavings = 100 - percentageFood - percentageCommute - percentageSubscription - percentageBills - percentageUtilities - percentageClothes - percentageMisc

if (percentageFood > 20):
    print(f"You spent {percentageFood}% of your income. You need to look upon your food expenses try to buy things which are more cost effective.")

if (percentageCommute > 10):
    print(f"You spent {percentageCommute}% of your income. You need to look upon your commute expenses try to use public transit and use sharing cabs instead.")

if (percentageSubscription > 15):
    print(f"You spent {percentageSubscription}% of your income. You need to seriously look upon stuff you're subscribing to. If you're not actively using any subscription-based OTT platform then don't subscribe to it! If you're spending these on upskilling courses then try to look for free courses.")

if (percentageBills > 15):
    print(f"You spent {percentageBills}% of your income. Probably you keep forgeting switching off the electrical appliances after using it! Make a habit of switching off the appliances after you've used it!")

if (percentageClothes > 20):
    print(f"You spent {percentageClothes}% of your income. You may've bought clothes to look cool and which are trendy. You should buy things which are more suitable for everywhere wear.")

if (percentageUtilities > 5):
    print(f"You spent {percentageUtilities}% of your income. These are maybe some of your money spent on reparing things try to buy things which are more durable so you would save on these expenses.")
    
if (percentageMisc > 5):
    print(f"{percentageMisc}")

if (percentageSavings < 10):
    print(f"You're too low on savings! It's less than {percentageSavings}")

print(f"Your savings are: {(percentageSavings / 100) * income}")
print(f"Your savings are: {percentageSavings}")



# -------------Python program that accepts the user's first and last name and prints them in reverse order with a space between them-------------
print("\nProgram that accepts the user's first and last name and prints them in reverse order with a space between them")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hey,", last_name, first_name)



# ---------Python program that accepts a sequence of comma-separated numbers from the user and generates a list of those numbers---------
print("\nProgram that accepts a sequence of comma-separated numbers from the user and generates a list of those numbers")
commaNumber = input("Enter numbers seperated by commas: ")
print("Comma-separated numbers in lists:", commaNumber.split(","))



# ------------------Python program that accepts a filename from the user and prints the extension of the file------------------
print("\nProgram that accepts a filename from the user and prints the extension of the file")
fileName = input("Enter the file name: ")
fileExtensionSplit = fileName.split(".")
if(fileExtensionSplit[-1] == "py"):
    print("The extension of the file: Python")
elif(fileExtensionSplit[-1] == "cpp"):
    print("The extension of the file: C++")
elif(fileExtensionSplit[-1] == "c"):
    print("The extension of the file: C")
elif(fileExtensionSplit[-1] == "java"):
    print("The extension of the file: Java")
elif(fileExtensionSplit[-1] == "html"):
    print("The extension of the file: HTML")
elif(fileExtensionSplit[-1] == "css"):
    print("The extension of the file: CSS")
elif(fileExtensionSplit[-1] == "js"):
    print("The extension of the file: Javascript")
elif(fileExtensionSplit[-1] == "php"):
    print("The extension of the file: PHP")
elif(fileExtensionSplit[-1] == "doc" or fileExtensionSplit == "docx"):
    print("The extension of the file: Word Document")
elif(fileExtensionSplit[-1] == "pdf"):
    print("The extension of the file: PDF (Portable Document File)")
elif(fileExtensionSplit[-1] == "txt"):
    print("The extension of the file: Text File")
elif(fileExtensionSplit[-1] == "xls" or fileExtensionSplit[-1] == "xlsx"):
    print("The extension of the file: Excel Document")



# ------------------Python program that accepts an integer (n) and computes the value of n+nn+nnn------------------
print("\nProgram that accepts an integer (n) and computes the value of n+nn+nnn")
intInput = int(input("Enter the number: "))
n = intInput
nn = str(intInput) + str(intInput)
nnn = str(intInput) + str(intInput) + str(intInput)
print(f"The value of (n + nn + nnn) is {int(n) + int(nn) + int(nnn)}")



# --------------------------Python program that prints the calendar for a given month and year--------------------------
print("\nProgram that prints the calendar for a given month and year")
import calendar
year = int(input("Enter the year of the calendar you want: "))
month = int(input("Enter the month of the calendar you want: "))
print("\nThe calendar for " + str(month) + "/" + str(year) + " is" + "\n" + calendar.month(year, month))



# -------------------Program to print characters from a string that are present at an even index number-------------------
stringInput = input("Enter the string: ")
for i in range(0, len(stringInput)):
    if (i % 2 == 0):
        print(stringInput[i])



# ---------------------------Program to remove first n characters from a string---------------------------
stringInput1 = input("Enter the string: ")
removeFirstN = int(input("Enter the first n number to be removed from a string: "))
print(f"After removing first {removeFirstN} characters the string is \"{stringInput1[removeFirstN:]}\"")



# --------------------Program to print a pattern of numbers increasing with each line--------------------
numberPattern = int(input("Enter the number you want to see the pattern of: "))
for i in range(1, numberPattern + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print("")



# --------------------Program to print a pattern of numbers increasing with each line--------------------
numberPattern1 = int(input("Enter the number you want to see the pattern of: "))
for i in range(1, numberPattern1 + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")



# -------------------Program to print multiplication table from 1 to 10-------------------
print("\t\t", end="")
for i in range(1, 11):
    print(i, end="\t")
print("\n")
for i in range(1, 11):
    print(f"{i}  ---> \t", end="")
    for j in range(1, 11):
        print(i * j, end="\t")
    print("")


