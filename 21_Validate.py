import re       # `re` means regular expression

email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if ((username) and ("." in domain)):    # it can also be `domain.endswith(".edu")`
#     print("Valid!")
# else:
#     print("Invalid!")

# for reference what this ".", "+", "*" mean read `docs.python.org/3/library/re.html`
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):   # `\` after using `r` means raw string it takes the input as it is!
    print("Valid!")                                      # `re.IGNORECASE` for ignoring things in uppercase
else:
    print("Invalid!")


# --------This is the regular expression that browsers use for validating the email address that we fill in the forms/websites--------
# ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](/:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
