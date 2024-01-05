import re

name = input("What's your name? ").strip()
if (matches := re.search(r"^(.+), *(.+)$", name)):      # `:=` this is new in Python this assigns value from right to left and also ask boolean question
    # last, first = matches.groups()
    # last = matches.group(1)
    # first = matches.group(2)          # also can be written like this
    # name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)      # can also be written like this, by concatenating
print(f"Hello, {name}")

# `Group()` divides the expression into number of parenthesis present
# So if there are two parenthesis then it'll divide it into two groups and their indexing starts from `1`