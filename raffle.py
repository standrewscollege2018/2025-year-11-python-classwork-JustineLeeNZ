''' Runs a raffle draw - Justine Lee '''

# need random library so can choose a winner
import random

# list to store names of raffle entrants
entrants = []

# ask for prize name and price
prize_name = input("Name of prize: ")
prize_price = int(input("Price of prize: "))

# ask for names of entrants
keep_asking = True

while keep_asking == True:
    name = input("Name (type end to finish): ")
    if name == "end":
       keep_asking = False
    else:
        entrants.append(name)

# print details of raffle, prize and entrant names
print("\nThe raffle is now live...")
print(f"There are {len(entrants)} people in the draw for the {prize_name}")

for i in range(0, len(entrants)):
    print(entrants[i])

# choose winner and display raffle result
winner_index = random.randint(0, len(entrants)-1)
winner_name = entrants[winner_index]

print(f"\nThe winner of the {prize_name} worth {prize_price} is... {winner_name}")




