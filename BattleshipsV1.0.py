import string
import copy
from random import randrange
from pprint import PrettyPrinter
from colorama import init, Fore, Style

# class ColorPrettyPrinter(PrettyPrinter):
#     def format(self, object, context, maxlevels, level):
#         if isinstance(object, str):
#             if object == 'S':
#                 return (Fore.GREEN + object + Style.RESET_ALL, True, False)
#             elif object == 'H':
#                 return (Fore.RED + object + Style.RESET_ALL, True, False)
#             elif object == 'O':
#                 return (Fore.BLUE + object + Style.RESET_ALL, True, False)
#         return PrettyPrinter.format(self, object, context, maxlevels, level)
    
# color_pprint = ColorPrettyPrinter()
# color_pprint.pprint(visible_board)

def Fill_With_Recurring_Characters(library_to_fill, character, length):
    for i, char in enumerate(string.ascii_uppercase[:length]):
            library_to_fill[char] = list(f"{character}" * length)
    return library_to_fill

def Generate_Coordinate(board):
    cord_value = randrange(len(board))
    return cord_value


def Generate_Coordinate_Ship_Start(board, ship_length):
    cord_value = randrange(len(board) - ship_length)
    return cord_value


def Is_Player_Input_Properly_Formatted(player_guess):
    if player_guess and player_guess[0].isalpha() and player_guess[1:].isnumeric():
        return True
    return False


def Is_Player_Input_Within_Bounds():
    if ord(hor_position) - 65 < len(hidden_board) and ver_position <= len(hidden_board["A"]) - 1 and ver_position != -1:
        return True
    return False


def Place_Ships(ship_no, ship_length):
    while ship_no > 0:
        is_vertical = randrange(2) == 0
        if is_vertical:
            x = Generate_Coordinate(hidden_board)
            y = string.ascii_uppercase[Generate_Coordinate_Ship_Start(hidden_board, ship_length)]
            if all(hidden_board[chr(ord(y) + i)][x] == "X" for i in range(ship_length)):
                for i in range(ship_length):
                    hidden_board[chr(ord(y) + i)][x] = "S"
                ship_no -= 1
        else:
            x = Generate_Coordinate_Ship_Start(hidden_board, ship_length)
            y = string.ascii_uppercase[Generate_Coordinate(hidden_board)]
            if all(hidden_board[chr(ord(y))][x + i] == "X" for i in range(ship_length)):
                for i in range(ship_length):
                    hidden_board[chr(ord(y))][x + i] = "S"
                ship_no -= 1


def Print_Board(visible_board):
    print("        ", end = "")
    for Y in range(1,(1 + len(visible_board))):
        print(Y, end = "    ")
    print()
    PrettyPrinter().pprint(visible_board)


def Intro():
    print("Welcome! Let's play a round, I'll prepare my battleships!")
    print(f"I have {ship_no_and_l['Carriers'][0]} carrier(s), {ship_no_and_l['Battleships'][0]} battleships, {ship_no_and_l['Cruisers'][0]} cruisers, {ship_no_and_l['Submarines'][0]} submarines, and {ship_no_and_l['Destroyers'][0]} destroyers.")
    print(f"A carrier is {ship_no_and_l['Carriers'][1]}, a battleship {ship_no_and_l['Battleships'][1]}, a cruiser {ship_no_and_l['Cruisers'][1]}, a submarine {ship_no_and_l['Submarines'][1]}, and a destroyer {ship_no_and_l['Destroyers'][1]} cells long.")
    print("Ships can be placed next to one another, but none are placed diagonally.")
    print(f"You need a total of {force} hits to win!")


hidden_board = {}
Fill_With_Recurring_Characters(hidden_board, "X", 10)
visible_board = copy.deepcopy(hidden_board)
player_board = copy.deepcopy(hidden_board)
ship_no_and_l = {"Carriers" : (1, 5), "Battleships" : (2, 4), "Cruisers" : (3, 3), "Submarines" : (3, 3), "Destroyers" : (5, 2)}
force = 0

for ship in ship_no_and_l:
    force += ship_no_and_l[ship][0] * ship_no_and_l[ship][1]

for placement in ship_no_and_l:
    Place_Ships(ship_no_and_l[placement][0], ship_no_and_l[placement][1])



Intro()
Print_Board(visible_board)

print(f"Time to place your ships! Ships can be placed next to one another, but not diagonally. Let's start with the Carriers. You have {ship_no_and_l['Carriers'][0]} carrier(s).")

ships_to_place = ship_no_and_l["Carriers"][0]
while ships_to_place > 0:
    start_point_input = input("Where would you like to place the ship? Give me the starting point. ")
    start_point_input = start_point_input.upper()
    if not Is_Player_Input_Properly_Formatted(start_point_input):
        print("Please use the NumberLetter format. One letter, one number. No more, no less.")
        continue
    hor_position = start_point_input[0]
    ver_position = int(start_point_input[1:]) - 1
    if not Is_Player_Input_Within_Bounds():
        print("Please use one letter, one number, within the gameboard's range.")
        continue
    placement_pos = player_board[hor_position][ver_position]
    Is_It_Occupied = placement_pos == "S"
    if Is_It_Occupied:
        print("There's already a ship there. Let's try again.")
        continue
    else:
        player_board[hor_position][ver_position] = "S"
        available_positions = []
        Print_Board(player_board)
        ok_right = ver_position + ship_no_and_l["Carriers"][1] <= len(hidden_board["A"]) and ver_position + ship_no_and_l["Carriers"][1] > 0
        ok_left = ver_position - ship_no_and_l["Carriers"][1] + 1 > -1
        ok_up = ord(hor_position) - ship_no_and_l["Carriers"][1] - 65 <= len(hidden_board) and ord(hor_position) - ship_no_and_l["Carriers"][1] - 65 >= 0
        ok_down = ord(hor_position) + ship_no_and_l["Carriers"][1] - 65 <= len(hidden_board) and ord(hor_position) + ship_no_and_l["Carriers"][1] - 65 > 0
        appropriate_placement_right = str(hor_position) + str(ver_position + ship_no_and_l["Carriers"][1])
        appropriate_placement_left = str(hor_position) + str(ver_position + 2 - ship_no_and_l["Carriers"][1])
        appropriate_placement_up = str(chr(ord(hor_position) + 1 - ship_no_and_l["Carriers"][1])) + str(ver_position + 1)
        appropriate_placement_down = str(chr(ord(hor_position) - 1 + ship_no_and_l["Carriers"][1])) + str(ver_position + 1)
        if ok_left and player_board[hor_position][ver_position - ship_no_and_l["Carriers"][1] + 1] != "S":
            available_positions.append(appropriate_placement_left)
        if ok_right and player_board[hor_position][ver_position + ship_no_and_l["Carriers"][1] - 1] != "S":
            available_positions.append(appropriate_placement_right)
        if ok_up and player_board[str(chr(ord(hor_position) + 1 - ship_no_and_l["Carriers"][1]))][ver_position] != "S":
            available_positions.append(appropriate_placement_up)
        if ok_down and player_board[str(chr(ord(hor_position) - 1 + ship_no_and_l["Carriers"][1]))][ver_position] != "S":
            available_positions.append(appropriate_placement_down)
        end_point_input = input(f"One end point of the ship will be placed at {start_point_input}. For the other end, the following positions are available: {available_positions} ")
        end_point_input = end_point_input.upper()
        if end_point_input in available_positions:
            if end_point_input == appropriate_placement_right:
                for j in range(ship_no_and_l["Carriers"][1]):                    
                    player_board[hor_position][ver_position + j] = "S"
            elif end_point_input == appropriate_placement_left:
                for j in range(ship_no_and_l["Carriers"][1]):
                    player_board[hor_position][ver_position - j] = "S"
            elif end_point_input == appropriate_placement_up:
                for j in range(ship_no_and_l["Carriers"][1]):
                    player_board[chr(ord(hor_position) - j)][ver_position] = "S"
            elif end_point_input == appropriate_placement_down:
                for j in range(ship_no_and_l["Carriers"][1]):
                    player_board[chr(ord(hor_position) + j)][ver_position] = "S"
            ships_to_place -= 1
        else:
            print("The second end point you have entered is invalid. Let's try again!")
            player_board[hor_position][ver_position] = "X"
            continue
        Print_Board(player_board)
        
        
ships_to_place = ship_no_and_l["Battleships"][0]
while ships_to_place > 0:
    start_point_input = input("Where would you like to place the ship? Give me the starting point. ")
    start_point_input = start_point_input.upper()
    if not Is_Player_Input_Properly_Formatted(start_point_input):
        print("Please use the NumberLetter format. One letter, one number. No more, no less.")
        continue
    hor_position = start_point_input[0]
    ver_position = int(start_point_input[1:]) - 1
    if not Is_Player_Input_Within_Bounds():
        print("Please use one letter, one number, within the gameboard's range.")
        continue
    placement_pos = player_board[hor_position][ver_position]
    Is_It_Occupied = placement_pos == "S"
    if Is_It_Occupied:
        print("There's already a ship there. Let's try again.")
        continue
    else:
        player_board[hor_position][ver_position] = "S"
        available_positions = []
        Print_Board(player_board)
        ok_right = ver_position + ship_no_and_l["Battleships"][1] <= len(hidden_board["A"]) and ver_position + ship_no_and_l["Battleships"][1] > 0
        ok_left = ver_position - ship_no_and_l["Battleships"][1] + 1 > -1
        ok_up = ord(hor_position) - ship_no_and_l["Battleships"][1] - 65 <= len(hidden_board) and ord(hor_position) - ship_no_and_l["Battleships"][1] - 65 >= 0
        ok_down = ord(hor_position) + ship_no_and_l["Battleships"][1] - 65 <= len(hidden_board) and ord(hor_position) + ship_no_and_l["Battleships"][1] - 65 > 0
        appropriate_placement_right = str(hor_position) + str(ver_position + ship_no_and_l["Battleships"][1])
        appropriate_placement_left = str(hor_position) + str(ver_position + 2 - ship_no_and_l["Battleships"][1])
        appropriate_placement_up = str(chr(ord(hor_position) + 1 - ship_no_and_l["Battleships"][1])) + str(ver_position + 1)
        appropriate_placement_down = str(chr(ord(hor_position) - 1 + ship_no_and_l["Battleships"][1])) + str(ver_position + 1)
        if ok_left and player_board[hor_position][ver_position - ship_no_and_l["Battleships"][1] + 1] != "S":
            available_positions.append(appropriate_placement_left)
        if ok_right and player_board[hor_position][ver_position + ship_no_and_l["Battleships"][1] - 1] != "S":
            available_positions.append(appropriate_placement_right)
        if ok_up and player_board[str(chr(ord(hor_position) + 1 - ship_no_and_l["Battleships"][1]))][ver_position] != "S":
            available_positions.append(appropriate_placement_up)
        if ok_down and player_board[str(chr(ord(hor_position) - 1 + ship_no_and_l["Battleships"][1]))][ver_position] != "S":
            available_positions.append(appropriate_placement_down)
        end_point_input = input(f"One end point of the ship will be placed at {start_point_input}. For the other end, the following positions are available: {available_positions} ")
        end_point_input = end_point_input.upper()
        if end_point_input in available_positions:
            if end_point_input == appropriate_placement_right:
                for j in range(ship_no_and_l["Battleships"][1]):                    
                    player_board[hor_position][ver_position + j] = "S"
            elif end_point_input == appropriate_placement_left:
                for j in range(ship_no_and_l["Battleships"][1]):
                    player_board[hor_position][ver_position - j] = "S"
            elif end_point_input == appropriate_placement_up:
                for j in range(ship_no_and_l["Battleships"][1]):
                    player_board[chr(ord(hor_position) - j)][ver_position] = "S"
            elif end_point_input == appropriate_placement_down:
                for j in range(ship_no_and_l["Battleships"][1]):
                    player_board[chr(ord(hor_position) + j)][ver_position] = "S"
            ships_to_place -= 1
        else:
            print("The second end point you have entered is invalid. Let's try again!")
            player_board[hor_position][ver_position] = "X"
            continue
        Print_Board(player_board)
        # MI VAN, HA AZ "S" NEM A VÉGPONT, CSAK ÁTVÁG RAJTA??? VAGY HA NINCS APPROPRIATE PLACEMENT LEHETŐSÉG??????????????
    
torpedos = 30

while torpedos > 0 and force > 0:
    guess = input(f"You can only miss {torpedos} times! Use the NumberLetter (e.g. A1) format and make a guess! ")
    guess = guess.upper()
    # Is_Guess_Properly_Formatted = guess and guess[0].isalpha() and guess[1:].isnumeric()
    if not Is_Player_Input_Properly_Formatted(guess):
        print("Please use the NumberLetter format. One letter, one number. No more, no less.")
        continue
    hor_position = guess[0]
    ver_position = int(guess[1:]) - 1
    # Is_Guess_Within_Bounds = ord(hor_position) - 65 < len(hidden_board) and ver_position <= len(hidden_board["A"]) - 1 and ver_position != -1
    if not Is_Player_Input_Within_Bounds():
        print("Please use one letter, one number, within the gameboard's range.")
        continue
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