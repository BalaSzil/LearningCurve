import string
import copy
from random import randrange
from colorama import init, Fore, Style

init()

def fill_board_with_recurring_characters(board, character, length):
    for i in range(length):
        board.append(list(f"{character}"*length))
    return board


def generate_coordinate(board):
    cord_value = randrange(len(board))
    return cord_value


def generate_coordinate_ship_start(board, ship_length):
    cord_value = randrange(len(board) - ship_length)
    return cord_value


def place_ships(ship_no, ship_length):
    while ship_no > 0:
        is_vertical = randrange(2) == 0
        if is_vertical:
            x = generate_coordinate(hidden_board)
            y = generate_coordinate_ship_start(hidden_board, ship_length)
            if all(hidden_board[y + i][x] == "X" for i in range(ship_length)):
                for i in range(ship_length):
                    hidden_board[y + i][x] = "S"
                ship_no -= 1
        else:
            x = generate_coordinate_ship_start(hidden_board, ship_length)
            y = generate_coordinate(hidden_board)
            if all(hidden_board[y][x + i] == "X" for i in range(ship_length)):
                for i in range(ship_length):
                    hidden_board[y][x + i] = "S"
                ship_no -= 1

def print_board(board):
    for i in range(1, (1 + len(board))):
        print(i, end = " ")
    print()
    for j in range(len(board[0])):
        for char in board[j]:
            if char == "H":
                print(Fore.RED + char + Style.RESET_ALL, end = " ")
            elif char == "O":
                print(Fore.BLUE + char + Style.RESET_ALL, end = " ")
            else:
                print(char, end = " ")
        print(string.ascii_uppercase[j])

def intro():
    print(f"I have {Carriers} carrier(s), {Battleships} battleships, {Cruisers} cruisers, {Submarines} submarines, and {Destroyers} destroyers.")
    print(f"A carrier is {Carrier_l}, a battleship {Battleship_l}, a cruiser {Cruiser_l}, a submarine {Submarine_l}, and a destroyer {Destroyer_l} cells long.")
    print("Ships can be placed next to one another, but none are placed diagonally.")
    print(f"You need a total of {force} hits to win!")

       
print("Welcome! Let's play a round, I'll prepare my battleships!")
hidden_board = []
fill_board_with_recurring_characters(hidden_board, "X", 10)
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

place_ships(Carriers, Carrier_l)
place_ships(Battleships, Battleship_l)
place_ships(Cruisers, Cruiser_l)
place_ships(Submarines, Submarine_l)
place_ships(Destroyers, Destroyer_l)

intro()
print_board(visible_board)


while torpedos > 0 and force > 0:
    
    guess = input(f"You can only miss {torpedos} times! Use the NumberLetter (e.g. A1) format and make a guess! ")
    guess = guess.upper()
    
    is_guess_properly_formatted = guess and guess[0].isalpha() and guess[1:].isnumeric()
    if not is_guess_properly_formatted:
        print("Please use the NumberLetter format. One letter, one number. No more, no less.")
        continue
    
    hor_position = ord(guess[0]) - (ord("A"))
    ver_position = int(guess[1:]) - 1
    
    is_guess_within_bounds = hor_position < len(hidden_board) and ver_position <= len(hidden_board[0]) - 1 and ver_position != -1
    if not is_guess_within_bounds:
        print("Please use one letter, one number, within the gameboard's range.")
        continue
    
    guess_pos = hidden_board[hor_position][ver_position]
    visible_guess_pos = visible_board[hor_position][ver_position]
    
    is_it_previous_guess = visible_guess_pos == "H" or visible_guess_pos == "O"
    is_ship_hit = guess_pos == "S"
    if is_it_previous_guess:
        torpedos -= 1
        print(f"Hey, you've already tried that! You can only miss {torpedos} more times!")
        print_board(visible_board)
    elif is_ship_hit:
        force -= 1
        visible_board[hor_position][ver_position] = "H"
        print(f"That's a hit!!! The enemy is left at {force} strength!")
        print_board(visible_board)
    else:
        torpedos -= 1
        visible_board[hor_position][ver_position] = "O"
        print(f"That's a miss! You can only try {torpedos} more times!")
        print_board(visible_board)
        
if torpedos == 0:
    print("Bad luck, Captain! We've lost!!!")
if force == 0:
    print("Well done, Captain! We won!!!")