# Functions
import string
import copy
from random import randrange


def Fill_Sublist_With_X(name_of_list):
    name_of_list.extend(list("X"*10))
    return name_of_list


def Coordinate(name_of_board):
    cord_value = randrange((len(name_of_board)))
    return cord_value


def Coordinate_Sans_Length(name_of_board, ship_length):
    cord_value = randrange((len(name_of_board)) - ship_length)
    return cord_value


def Guess_Not_Correct_Length(player_guess):
    if len(player_guess) not in (2,3):
        return True
    else:
        return False

    
def Guess_Not_Correct_Format(player_guess):
    if not guess[0].isalpha() or not guess[1].isnumeric():
        return True
    else:
        return False


def Guess_Out_Of_Bounds(player_guess):
    if len(player_guess) == 3:
        if ord(player_guess[0].upper()) < 65:
            return True
        elif ord(player_guess[0].upper()) >= (65 + len(hidden_board)):
            return True
        elif int(player_guess[1:]) > len(hidden_board[0]):
            return True
    elif len(player_guess) == 2:
        if ord(player_guess[0].upper()) < 65 or ord(player_guess[0].upper()) >= (65 + len(hidden_board)):
            return True
    elif len(player_guess) == 3 and int(player_guess[1:]) > len(hidden_board[0]):
        return True
    else:
        return False


def Placement(ship_no, ship_length):
    while ship_no > 0:
        is_vertical = randrange(2) == 0
        if is_vertical:
            x = Coordinate(hidden_board)
            y = Coordinate_Sans_Length(hidden_board, ship_length)
            if all(hidden_board[y + i][x] == "X" for i in range(ship_length)):
                for i in range(ship_length):
                    hidden_board[y + i][x] = "S"
                ship_no -= 1
        else:
            x = Coordinate_Sans_Length(hidden_board, ship_length)
            y = Coordinate(hidden_board)
            if all(hidden_board[y][x + i] == "X" for i in range(ship_length)):
                for i in range(ship_length):
                    hidden_board[y][x + i] = "S"
                ship_no -= 1


def Already_Tried_That(guess_pos):
    if guess_pos == "H" or guess_pos == "O":
        return True
    else:
        return False
    
    
def Ship_Is_Hit(guess_pos):
    if guess_pos == "S":
        return True
    else:
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
# for i in columns:
#     print(i, end = " ")
# print()
# for Y in rows:
#     for X in range (10):
#         print("X", end = " ")
#     print(rows[helper : helper + 1])
#     helper += 1
    
# def Print_Table(masterList):
#     for i in range(len(masterList)):
#         print(masterList[i])
#         print()
    
    
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
hidden_board = [Fill_Sublist_With_X(A), Fill_Sublist_With_X(B), Fill_Sublist_With_X(C), Fill_Sublist_With_X(D), Fill_Sublist_With_X(E), Fill_Sublist_With_X(F), Fill_Sublist_With_X(G), Fill_Sublist_With_X(H), Fill_Sublist_With_X(I), Fill_Sublist_With_X(J)]
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
torpedos = 10

Placement(Carriers, Carrier_l)
Placement(Battleships, Battleship_l)
Placement(Cruisers, Cruiser_l)
Placement(Submarines, Submarine_l)
Placement(Destroyers, Destroyer_l)

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
    if Guess_Not_Correct_Length(guess):
        print("Guess_Not_Correct_Length")
        # print("Please use the NumberLetter format. One letter, one number. No more, no less.")
    elif Guess_Not_Correct_Format(guess):
        print("Guess_Not_Correct_Format")
        # print("Please use letters and numbers in the correct format.")
    elif Guess_Out_Of_Bounds(guess):
        print("Guess_Out_Of_Bounds")
        # print("Please use one letter, one number, within the gameboard's range.")
    else:
        letter = guess[0]
        number = int(guess[1:])
        hor_position = ord(letter) - (ord("A"))
        ver_position = (number - 1)
        guess_pos = hidden_board[hor_position][ver_position]
        if Ship_Is_Hit(guess_pos):
            force -= 1
            hidden_board[hor_position][ver_position] = "H"
            visible_board[hor_position][ver_position] = "H"
            print(f"That's a hit!!! The enemy is left at {force} strength!")
            Print_Visible_Board(visible_board)
        elif Already_Tried_That(guess_pos):
            torpedos -= 1
            print(f"Hey, you've already tried that! You can only try {torpedos} more times!")
            Print_Visible_Board(visible_board)
        else:
            hidden_board[hor_position][ver_position] = "O"
            visible_board[hor_position][ver_position] = "O"
            torpedos -= 1
            print(f"That's a miss! You can only try {torpedos} more times!")
            Print_Visible_Board(visible_board)
            
            
# for playerboard print hidden board as above, but print x for x and s, print o and h as they are