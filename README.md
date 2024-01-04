**Below is the documentation of all the tutorial files these were programs that I wrote when I was learning every concept, I'm going to explain what I learned in each of the programs**

### 1) In `01_hello.py`
* Used `print()`, `input()`, `split()`, `strip()`, `capitalize()`, `title()`, etc. functions.<br/>
You can find more such functions in the `print()` function's documentation available at [Python Documentation](https://docs.python.org/3/library/functions.html#print).
* Used formatted strings.
* Used functions parameters like `sep=""` and `end=""`.
* Learned how `print("Hello", name)` is different from `print("Hello " + name)`, the last one is the concatenation of the string.

### 2) In `02_Calculator.py`
* Declared variables which take integer input using `int(input())` function.
* Declared variables that take decimal/float input using the `float(input())` function.
* How `a / b` is different from `a // b`.
* Using `print((a / b):.2f)` prints the result upto 2 decimal places.
* Learned about functions and their arguments & parameters.

### 3) In `03_Calculator2.py`
* Used user-defined function `square()` which returns `n ** 2`, there's a difference between `n * 2` and `n ** 2` the former means multiplication and the other means raised to 2.
* The other one returns the `pow()` function, it takes a number and raises it to a number as function arguments. The `pow()` function takes two parameters one as a number and another as a number which is raised to.

### 4) In `04_Compare.py`
* Learned about conditionals

### 5) In `05_Parity.py`
* Defined `is_even()` function it takes `n` as its parameter and in this function using conditional I checked if `n % 2 == 0` then it'll return boolean expression `True` if not then it'll return `False`.
* Defined `main()` function which I called `is_even()` function if this returns `True` then it'll print `"Even"` and if it returns `False` then it'll print `"Odd"`.
* Also, learned about short-hand if-else, these are used to tighten up the code.
* ```
  def is_even(n):
     return True if (n % 2 == 0) else False
  def is_even(n):
     return n % 2 == 0
  '''

### 6) In `06_House.py`
* Learned about `match case`, in this we can create many specific cases and a case that we haven't considered can be put into the "default case" and it is denoted by `case _` whatever code-block is in this keyword will only be executed if none of the above cases are valid for that expression.

### 7) In `07_Cat.py`
* Learned about `for`, and `while` loops.
