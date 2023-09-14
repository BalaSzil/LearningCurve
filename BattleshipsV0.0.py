# Functions
import string
import random
def rowing(row_name):
    row_name = " ".join(row_name)
    return row_name
def exes(name_of_list):
    name_of_list.extend(list("X"*10))
    return name_of_list
def vector(name_of_master_list):
    pos_value = random.randrange((len(name_of_master_list)))
    return pos_value
def vector_sans_l(name_of_master_list, ship_length):
    pos_value = random.randrange((len(name_of_master_list)) - ship_length)
    return pos_value
def placement(ship, ship_length):
    while ship > 0:
        placement_decision = random.randrange(2)
        if placement_decision == 0:
            x = vector(Master_list)
            y = vector_sans_l(Master_list[x], ship_length)
            for i in range(ship_length):
                if all(Master_list[y + i][x] == "X" for i in range(ship_length)):
                    for i in range(ship_length):
                        Master_list[y + i][x] = "S"
                    ship -= 1
        elif placement_decision == 1:
            x = vector_sans_l(Master_list, ship_length)
            y = vector(Master_list)
            for i in range(ship_length):
                if all(Master_list[y][x + i] == "X" for i in range(ship_length)):
                    for i in range(ship_length):
                        Master_list[y][x + i] = "S"
                    ship -= 1
    
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
# letter = C
# position = ord(letter) - ord(A)
# print(position)
# print(ord("A"))

placement(Carriers, Carrier_l)
placement(Battleships, Battleship_l)
placement(Cruisers, Cruiser_l)
placement(Submarines, Submarine_l)
placement(Destroyers, Destroyer_l)

count = 0
for sublist in Master_list:
    for element in sublist:
        if element == "S":
            count += 1
print(count)
print(Master_list)


print(f"I have {Carriers} carriers, {Battleships} battleships, {Cruisers} cruisers, {Submarines} submarines, and {Destroyers} destroyers.")
print(f"Carriers are {Carrier_l}, the battleships {Battleship_l}, the cruisers {Cruiser_l}, the submarines {Submarine_l}, and the destroyers {Destroyer_l} large.")
print("None are placed diagonally.")
print(f"You need a total of {Force} hits to win!")
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