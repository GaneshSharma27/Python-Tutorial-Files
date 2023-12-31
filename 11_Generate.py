import random                   # imports all functions from random module

coin = random.choice(["Heads", "Tails"])    # if all functions are imported then write random.choice()
print("Using only \"import\" keyword:", coin)

number = random.randint(1, 10)
print("Random number from 1 to 10:", number)

cards = ["Jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
    print(card)

# from random import choice       # imports only choice function from the random module
# coin1 = choice(["Heads", "Tails"])      # only choice function
# print("Using \"from\" keyword:", coin1)