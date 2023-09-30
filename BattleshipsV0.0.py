# Functions
import string
import copy
from random import randrange


def Fill_Board_Recurring_Characters(board, character, length):
    for i in range(length):
        board.append(list(f"{character}"*length))
    return board


def Generate_Coordinate(board):
    cord_value = randrange((len(board)))
    return cord_value


def Generate_Coordinate_Ship_Start(board, ship_length):
    cord_value = randrange((len(board)) - ship_length)
    return cord_value


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


def Print_Board(visible_board):
    helper = 0
    for Y in range(1,(1 + len(visible_board))):
        print(" ", Y, end = "  ")
    print()
    for X in range(len(visible_board[0])):
        print(visible_board[helper], end = " ")
        print(string.ascii_uppercase[helper])
        helper += 1
        
        
# Setup
print("Welcome! Let's play a round, I'll prepare my battleships!")
hidden_board = []
Fill_Board_Recurring_Characters(hidden_board, "X", 10)
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
print(f"I have {Carriers} carrier(s), {Battleships} battleships, {Cruisers} cruisers, {Submarines} submarines, and {Destroyers} destroyers.")
print(f"A carrier is {Carrier_l}, a battleship {Battleship_l}, a cruiser {Cruiser_l}, a submarine {Submarine_l}, and a destroyer {Destroyer_l} cells long.")
print("Ships can be placed next to one another, but none are placed diagonally.")
print(f"You need a total of {force} hits to win!")


Print_Board(visible_board)


# Gameplay
while torpedos > 0 and force > 0:
    guess = input(f"You can only miss {torpedos} times! Use the NumberLetter (e.g. A1) format and make a guess! ")
    guess = guess.upper()
    Is_Guess_Not_Properly_Formatted = guess == "" or not guess[0].isalpha() or not guess[1:].isnumeric()
    if Is_Guess_Not_Properly_Formatted:
        print("Please use the NumberLetter format. One letter, one number. No more, no less.")
    else:
        hor_position = ord(guess[0]) - (ord("A"))
        ver_position = int(guess[1:]) - 1
        Is_Guess_Within_Bounds = hor_position >= len(hidden_board) or ver_position > len(hidden_board[0]) - 1
        if Is_Guess_Within_Bounds:
            print("Please use one letter, one number, within the gameboard's range.")
        else:
            guess_pos = hidden_board[hor_position][ver_position]
            visible_guess_pos = visible_board[hor_position][ver_position]
            Is_It_Previous_Guess = visible_guess_pos == "H" or visible_guess_pos == "O"
            Is_Ship_Hit = guess_pos == "S"
            if Is_It_Previous_Guess:
                torpedos -= 1
                print(f"Hey, you've already tried that! You can only miss {torpedos} more times!")
                Print_Board(visible_board)
            elif Is_Ship_Hit:
                force -= 1
                visible_board[hor_position][ver_position] = "H"
                print(f"That's a hit!!! The enemy is left at {force} strength!")
                Print_Board(visible_board)
            else:
                torpedos -= 1
                visible_board[hor_position][ver_position] = "O"
                print(f"That's a miss! You can only try {torpedos} more times!")
                Print_Board(visible_board)
if torpedos == 0:
    print("Bad luck, Captain! We've lost!!!")
if force == 0:
    print("Well done, Captain! We won!!!")