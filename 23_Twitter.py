import re

url = input("URL: ").strip()
# username = url.removeprefix("https://twitter.com/")   # `removeprefix()` removes the prefix of whatever is typed into its function arguments
# print(f"Username: {username}")

# `sub()` stands for substitute
# re.sub(pattern, repl, string, count=0, flags=0)
# re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, string, flags=0)

# username = re.sub(r"^((http|https)://)?(www\.)?twitter\.com/", "", url)
#                       https? ---> also can be written like this

if (matches := re.search(r"^https://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)):     # (?:www\.) ----> `?:` means don't consider it in a group
    print(f"Username:", matches.group(1))
