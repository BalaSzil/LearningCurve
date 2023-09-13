# Functions
import string
import random
def randomize(ship_p):
    return ship_p[random.randrange(len(ship_p))]
def rowing(row_name):
    row_name = " ".join(row_name)
    return row_name
def exes(name_of_list):
    name_of_list.extend(list("X"*10))
    return name_of_list

# Setup
print("Welcome! Let's play a round, I'll prepare my battleships!")
Carriers = 1
Battleships = 2
Cruisers = 3
Submarines = 3
Destroyers = 5
Carrier_l = 5
Battleship_l = 4
Cruiser_l = 3
Submarine_l = 3
Destroyer_l = 2
Force = (Carriers * Carrier_l +
         Battleships * Battleship_l +
         Cruisers * Cruiser_l +
         Submarines * Submarine_l +
         Destroyers * Destroyer_l)
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []
J = []
Master_list = [exes(A), exes(B), exes(C), exes(D), exes(E), exes(F), exes(G), exes(H), exes(I), exes(J)]
helper = 0
random_helper = random.randrange((len(Master_list)) - Carrier_l)
print(len(Master_list))
while Carriers > 0:
    helper = random.randrange(0, (9 - Carrier_l))
    placement_decision = random.randrange(1)
    if placement_decision == 0:
        Master_list = Master_list[:random_helper] + ["S"] + Master_list[random_helper+Carrier_l:]
        Carriers -= 1
        # else:
        #     Carriers -= 1

print(len(Master_list))
print(Master_list)


# print(f"I have {Carriers} carriers, {Battleships} battleships, {Cruisers} cruisers, {Submarines} submarines, and {Destroyers} destroyers.")
# print(f"Carriers are {Carrier_l}, the battleships {Battleship_l}, the cruisers {Cruiser_l}, the submarines {Submarine_l}, and the destroyers {Destroyer_l} large.")
# print("None are placed diagonally.")
# print(f"You need a total of {Force} hits to win!")
# rows = (string.ascii_uppercase[0:10])
# columns = (range(1,11))

# Playing field
# You could make 10 lists (1 for each row), have the input refer to list number/list element
# Replace with "[ ]" for miss, "H" for hit.

# Placement
# Use list.remove() and list.insert() to change elements from above lists
# Can base orientation of placed ships on randomization! Range 0-9, hor if even, vert if odd.
# Carrier_plac = Carriers * Carrier_l
# Battleship_plac = Battleships * Battleship_l
# Cruiser_plac = Cruisers * Cruiser_l
# Submarine_plac = Submarines * Submarine_l
# Destroyer_plac = Destroyers * Destroyer_l
# helper = 0

# helper = 0
# for i in columns:
#     print(i, end = " ")
# print()
# for Y in rows:
#     for X in range (10):
#         print("X", end = " ")
#     print(rows[helper:helper+1])
#     helper +=1
# guess = input("Use the NumberLetter (e.g. A1) format and make a guess! ")
# for victory, hits == Force vagy while Force > 0
# Eliminate invalid guesses (l or s than 2 char, 2 letters, 2 numbers)