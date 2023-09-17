# Functions
import string
import random
def exes(name_of_list):
    """Gives you ten X-es for the row"""
    name_of_list.extend(list("X"*10))
    return name_of_list
def vector(name_of_master_list):
    """"Returns random number within the ML lenght"""
    pos_value = random.randrange((len(name_of_master_list)))
    return pos_value
def vector_sans_l(name_of_master_list, ship_length):
    """Returns random number within ML minus ship lenght"""
    pos_value = random.randrange((len(name_of_master_list)) - ship_length)
    return pos_value
def placement(ship_no, ship_length):
    """Places given type of ship, returns nothing"""
    while ship_no > 0:
        is_vertical = random.randrange(2) == 0
        if is_vertical:
            x = vector(Master_list)
            y = vector_sans_l(Master_list, ship_length)
            if all(Master_list[y + i][x] == "X" for i in range(ship_length)):
                for i in range(ship_length):
                    Master_list[y + i][x] = "S"
                ship_no -= 1
        else:
            x = vector_sans_l(Master_list, ship_length)
            y = vector(Master_list)
            if all(Master_list[y][x + i] == "X" for i in range(ship_length)):
                for i in range(ship_length):
                    Master_list[y][x + i] = "S"
                ship_no -= 1
    
    
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
force = (Carriers * Carrier_l
         + Battleships * Battleship_l
         + Cruisers * Cruiser_l
         + Submarines * Submarine_l
         + Destroyers * Destroyer_l)
torpedos = 10
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

placement(Carriers, Carrier_l)
placement(Battleships, Battleship_l)
placement(Cruisers, Cruiser_l)
placement(Submarines, Submarine_l)
placement(Destroyers, Destroyer_l)

# count = 0
# for sublist in Master_list:
#     for element in sublist:
#         if element == "S":
#             count += 1
# print(count)
# print(Master_list)


# Playerboard
print(f"I have {Carriers} carriers, {Battleships} battleships, {Cruisers} cruisers, {Submarines} submarines, and {Destroyers} destroyers.")
print(f"Carriers are {Carrier_l}, the battleships {Battleship_l}, the cruisers {Cruiser_l}, the submarines {Submarine_l}, and the destroyers {Destroyer_l} large.")
print("Ships can be placed next to one another, but none are placed diagonally.")
print(f"You need a total of {force} hits to win!")
rows = (string.ascii_uppercase[0:10])
columns = (range(1,11))

helper = 0
for i in columns:
    print(i, end = " ")
print()
for Y in rows:
    for X in range (10):
        print("X", end = " ")
    print(rows[helper : helper + 1])
    helper += 1
    
    
# Gameplay
while torpedos > 0 and force > 0:
    guess = input(f"You can only miss {torpedos} times! Use the NumberLetter (e.g. A1) format and make a guess! ")
    guess = guess.upper()
    if len(guess) != 2:
        print("Please use the NumberLetter format. One letter, one number. No more, no less.")
    elif ord(guess[0]) < 65 or ord(guess[0]) > 90:
        print("Please use the NumberLetter format. One letter, one number. No more, no less.")
    elif ord(guess[1]) < 48 or ord(guess[1]) > 57:
        print("Please use the NumberLetter format. One letter, one number. No more, no less.")
    else:
        letter = guess[0]
        number = int(guess[1])
        hor_position = ord(letter) - (ord("A"))
        ver_position = (number - 1)
        guess_pos = Master_list[hor_position][ver_position]
        if guess_pos == "S":
            guess_pos = "H"
            force -= 1
            print(f"That's a hit!!! The enemy is left at {force} strength!")
            print(Master_list)
        else:
            guess_pos = "O"
            torpedos -= 1
            print(f"That's a miss! You only try {torpedos} more times!")
            print(Master_list)


# Eliminate invalid guesses (l or s then 2 char, 2 letters, 2 numbers). Based on ordenance number ranges maybe?