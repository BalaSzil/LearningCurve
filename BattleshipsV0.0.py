# Functions
import string
import copy
from random import randrange


def Fill_With_Recurring_Characters(row, character, length):
    row.extend(list(f"{character}"*length))
    return row


def Generate_Coordinate(board):
    cord_value = randrange((len(board)))
    return cord_value


def Generate_Coordinate_Ship_Start(board, ship_length):
    cord_value = randrange((len(board)) - ship_length)
    return cord_value


def Is_Player_Input_Properly_Formatted(player_guess):
    if not player_guess[0].isalpha() or not player_guess[1:].isnumeric():
        return False
    return True

def Is_Player_Input_Within_Bounds(player_guess):
    if hor_position >= len(hidden_board):
        return False
    elif ver_position > len(hidden_board[0]) - 1:
        return False
    return True


def Place_Ships(ship_no, ship_length):
    while ship_no > 0:
        is_vertical = randrange(2) == 0
        if is_vertical:
            x = Generate_Coordinate(hidden_board)
            y = Generate_Coordinate_Ship_Start(hidden_board, ship_length)
            if all(hidden_board[y + i][x] == "X" for i in range(ship_length)):
                for i in range(ship_length):
                    hidden_board[y + i][x] = "S"
                ship_no -= 1
        else:
            x = Generate_Coordinate_Ship_Start(hidden_board, ship_length)
            y = Generate_Coordinate(hidden_board)
            if all(hidden_board[y][x + i] == "X" for i in range(ship_length)):
                for i in range(ship_length):
                    hidden_board[y][x + i] = "S"
                ship_no -= 1


def Already_Tried_That(Is_Guess_pos):
    if Is_Guess_pos == "H" or Is_Guess_pos == "O":
        return True
    return False
    
    
def Ship_Is_Hit(Is_Guess_pos):
    if Is_Guess_pos == "S":
        return True
    return False
        
    
def Print_Visible_Board(visible_board):
    helper = 0
    for Y in range(1,(1 + len(visible_board))):
        print(Y, end = " ")
    print()
    for X in range(len(visible_board[0])):
        print(visible_board[helper : helper + 1], end = " ")
        print(string.ascii_uppercase[helper])
        helper += 1
    
    
# Setup
print("Welcome! Let's play a round, I'll prepare my battleships!")
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
hidden_board = [Fill_With_Recurring_Characters(A, "X", 10), Fill_With_Recurring_Characters(B, "X", 10), Fill_With_Recurring_Characters(C, "X", 10), Fill_With_Recurring_Characters(D, "X", 10), Fill_With_Recurring_Characters(E, "X", 10), Fill_With_Recurring_Characters(F, "X", 10), Fill_With_Recurring_Characters(G, "X", 10), Fill_With_Recurring_Characters(H, "X", 10), Fill_With_Recurring_Characters(I, "X", 10), Fill_With_Recurring_Characters(J, "X", 10)]
visible_board = copy.deepcopy(hidden_board)
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
torpedos = 30

Place_Ships(Carriers, Carrier_l)
Place_Ships(Battleships, Battleship_l)
Place_Ships(Cruisers, Cruiser_l)
Place_Ships(Submarines, Submarine_l)
Place_Ships(Destroyers, Destroyer_l)

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
    if Is_Player_Input_Properly_Formatted(guess) is False:
        print("Please use the NumberLetter format. One letter, one number. No more, no less.")
    else:
        hor_position = ord(guess[0]) - (ord("A"))
        ver_position = int(guess[1:]) - 1
        if Is_Player_Input_Within_Bounds(guess) is False:
            print("Please use one letter, one number, within the gameboard's range.")
        else:
            guess_pos = hidden_board[hor_position][ver_position]
            visible_guess_pos = visible_board[hor_position][ver_position]
            if Already_Tried_That(visible_guess_pos):
                torpedos -= 1
                print(f"Hey, you've already tried that! You can only miss {torpedos} more times!")
                Print_Visible_Board(visible_board)
            elif Ship_Is_Hit(guess_pos):
                force -= 1
                visible_board[hor_position][ver_position] = "H"
                print(f"That's a hit!!! The enemy is left at {force} strength!")
                Print_Visible_Board(visible_board)
            else:
                torpedos -= 1
                visible_board[hor_position][ver_position] = "O"
                print(f"That's a miss! You can only try {torpedos} more times!")
                Print_Visible_Board(visible_board)
if torpedos == 0:
    print("Bad luck, Captain! We've lost!!!")
if force == 0:
    print("Well done, Captain! We won!!!")