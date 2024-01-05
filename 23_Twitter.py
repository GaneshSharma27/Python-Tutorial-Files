import re

url = input("URL: ").strip()
# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")
# # `removeprefix()` removes the prefix of whatever is typed into its function arguments

# `sub()` stands for substitute
# re.sub(pattern, repl, string, count=0, flags=0)
username = re.sub(r"^((http|https)://)?(www\.)?twitter\.com/", "", url)
#                       https? ---> also can be written like this
print(f"Username: {username}")