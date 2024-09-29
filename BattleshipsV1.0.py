import string
import copy
from random import randrange
from colorama import Fore, Style


def fill_with_recurring_characters(library_to_fill, character, length):
    for i, char in enumerate(string.ascii_uppercase[:length]):
            library_to_fill[char] = list(f"{character}" * length)
    return library_to_fill


def generate_coordinate(board):
    cord_value = randrange(len(board))
    return cord_value


def generate_coordinate_ship_start(board, ship_length):
    cord_value = randrange(len(board) - ship_length)
    return cord_value


def is_player_input_properly_formatted(player_guess):
    return player_guess and player_guess[0].isalpha() and player_guess[1:].isnumeric()
       

def is_player_input_within_bounds(hor_position, ver_position):
    if ord(hor_position) - 65 < len(hidden_board) and ver_position <= len(hidden_board["A"]) - 1 and ver_position != -1:
        return True
    return False


def place_ships(ship_no, ship_length, board):
    while ship_no > 0:
        is_vertical = randrange(2) == 0
        if is_vertical:
            x = generate_coordinate(board)
            y = string.ascii_uppercase[generate_coordinate_ship_start(board, ship_length)]
            if all(board[chr(ord(y) + i)][x] == "X" for i in range(ship_length)):
                for i in range(ship_length):
                    board[chr(ord(y) + i)][x] = "S"
                ship_no -= 1
        else:
            x = generate_coordinate_ship_start(board, ship_length)
            y = string.ascii_uppercase[generate_coordinate(board)]
            if all(board[chr(ord(y))][x + i] == "X" for i in range(ship_length)):
                for i in range(ship_length):
                    board[chr(ord(y))][x + i] = "S"
                ship_no -= 1


def player_place_ship(ship_no, ship_length):
    ships_to_place = ship_no
    print(f"You have {ship_no} ships of {ship_length} length to place.")
    print_board(player_board)
    
    while ships_to_place > 0:
        start_point_input = input("Where would you like to place the ship? Give me the starting point. ")
        start_point_input = start_point_input.upper()
    
        if not is_player_input_properly_formatted(start_point_input):
            print("Please use the NumberLetter format. One letter, one number. No more, no less.")
            continue
        
        hor_position = start_point_input[0]
        ver_position = int(start_point_input[1:]) - 1
        
        if not is_player_input_within_bounds(hor_position, ver_position):
            print("Please use one letter, one number, within the gameboard's range.")
            continue
        
        placement_pos = player_board[hor_position][ver_position]
        is_it_occupied = placement_pos == "S"
        
        if is_it_occupied:
            print("There's already a ship there. Let's try again.")
            continue
        
        else:
            player_board[hor_position][ver_position] = "S"
            available_positions = []
            print_board(player_board)
            #szomszed poziciok tesztelesere lehet directions lista v dictionary (1,0),(-1,0),(0,1),(0,-1)
            ok_right = ver_position + ship_length <= len(hidden_board["A"]) 
            ok_left = ver_position - ship_length + 1 > -1
            ok_up = ord(hor_position) - ship_length - 65 + 1 >= 0
            ok_down = ord(hor_position) + ship_length - 65 <= len(hidden_board)
            ok_right_placement = str(hor_position) + str(ver_position + ship_length)
            ok_left_placement = str(hor_position) + str(ver_position + 2 - ship_length)
            ok_up_placement = str(chr(ord(hor_position) + 1 - ship_length)) + str(ver_position + 1)
            ok_down_placement = str(chr(ord(hor_position) - 1 + ship_length)) + str(ver_position + 1)
        
            if ok_left and player_board[hor_position][ver_position - ship_length + 1] != "S":
                available_positions.append(ok_left_placement)
                if ok_left_placement in available_positions:
                    for i in range(ship_length - 1):
                        if ok_left_placement in available_positions and player_board[hor_position][ver_position - ship_length + 1 + i] == "S":
                            available_positions.remove(ok_left_placement)
            if ok_right and player_board[hor_position][ver_position + ship_length - 1] != "S":
                available_positions.append(ok_right_placement)
                if ok_right_placement in available_positions:
                    for i in range(ship_length - 1):
                        if ok_right_placement in available_positions and player_board[hor_position][ver_position + ship_length - 1 - i] == "S":
                            available_positions.remove(ok_right_placement)
            if ok_up and player_board[str(chr(ord(hor_position) + 1 - ship_length))][ver_position] != "S":
                available_positions.append(ok_up_placement)
                if ok_up_placement in available_positions:
                    for i in range(ship_length - 1):
                        if ok_up_placement in available_positions and player_board[str(chr(ord(hor_position) + 1 + i - ship_length))][ver_position] == "S":
                            available_positions.remove(ok_up_placement)
            if ok_down and player_board[str(chr(ord(hor_position) - 1 + ship_length))][ver_position] != "S":
                available_positions.append(ok_down_placement)
                if ok_down_placement in available_positions:
                    for i in range(ship_length - 1):
                        if ok_down_placement in available_positions and player_board[str(chr(ord(hor_position) - 1 - i + ship_length))][ver_position] == "S":
                            available_positions.remove(ok_down_placement)
            
            if bool(available_positions) == False:
                print("There are no available positions from this starting point. Please select a new one!")
                player_board[hor_position][ver_position] = "X"
                continue
            
            end_point_input = input(f"One end point of the ship will be placed at {start_point_input}. For the other end, the following positions are available: {available_positions} ")
            end_point_input = end_point_input.upper()
            
            if end_point_input in available_positions:
                if end_point_input == ok_right_placement:
                    for j in range(ship_length):                    
                        player_board[hor_position][ver_position + j] = "S"
                elif end_point_input == ok_left_placement:
                    for j in range(ship_length):
                        player_board[hor_position][ver_position - j] = "S"
                elif end_point_input == ok_up_placement:
                    for j in range(ship_length):
                        player_board[chr(ord(hor_position) - j)][ver_position] = "S"
                elif end_point_input == ok_down_placement:
                    for j in range(ship_length):
                        player_board[chr(ord(hor_position) + j)][ver_position] = "S"
                ships_to_place -= 1
                print_board(player_board)
                
            else:
                print("The second end point you have entered is invalid. Let's try again!")
                player_board[hor_position][ver_position] = "X"
                continue
    
    
def print_board(board):
    for i in range(1, (1 + len(board))):
        print(i, end = " ")
    print()
    for j, row in enumerate(board):
        for character in board[row]:
            if character == "H":
                print(Fore.RED + character + Style.RESET_ALL, end = " ")
            elif character == "O":
                print(Fore.BLUE + character + Style.RESET_ALL, end = " ")
            elif character == "S":
                print(Fore.GREEN + character + Style.RESET_ALL, end = " ")
            else:
                print(character, end = " ")
        print(string.ascii_uppercase[j])


def intro():
    print("Welcome! Let's play a round, I'll prepare my battleships!")
    print(f"I have {ship_no_and_length['Carriers'][0]} carrier(s), {ship_no_and_length['Battleships'][0]} battleships, {ship_no_and_length['Cruisers'][0]} cruisers, {ship_no_and_length['Submarines'][0]} submarines, and {ship_no_and_length['Destroyers'][0]} destroyers.")
    print(f"A carrier is {ship_no_and_length['Carriers'][1]}, a battleship {ship_no_and_length['Battleships'][1]}, a cruiser {ship_no_and_length['Cruisers'][1]}, a submarine {ship_no_and_length['Submarines'][1]}, and a destroyer {ship_no_and_length['Destroyers'][1]} cells long.")
    print("Ships can be placed next to one another, but none are placed diagonally.")
    print(f"You need a total of {enemy_force} hits to win!")
    

def run_easy_mode(enemy_force, player_force):
    shots_taken_by_player = 0
    
    while player_force > 0 and enemy_force > 0:
        print_board(visible_board)
        guess = input(f"The enemy has a force of {enemy_force}! Use the NumberLetter (e.g. A1) format and make a guess! ")
        guess = guess.upper()
        
        if not is_player_input_properly_formatted(guess):
            print("Please use the NumberLetter format. One letter, one number. No more, no less.")
            continue
        
        hor_position = guess[0]
        ver_position = int(guess[1:]) - 1
        
        if not is_player_input_within_bounds(hor_position, ver_position):
            print("Please use one letter, one number, within the gameboard's range.")
            continue
        
        guess_pos = hidden_board[hor_position][ver_position]
        visible_guess_pos = visible_board[hor_position][ver_position]
        is_it_previous_guess = visible_guess_pos == "H" or visible_guess_pos == "O"
        is_ship_hit = guess_pos == "S"
        
        if is_it_previous_guess:
            print("Hey, you've already tried that! You just missed a turn!")
        
        elif is_ship_hit:
            enemy_force -= 1
            visible_board[hor_position][ver_position] = "H"
            print(f"That's a hit!!! You murderer! Those sailors had families... The enemy is left at {enemy_force} strength!")
            shots_taken_by_player += 1
            print_board(visible_board)
        
        else:
            visible_board[hor_position][ver_position] = "O"
            print(f"That's a miss! The enemy is still at {enemy_force} strength!")
            shots_taken_by_player += 1
            print_board(visible_board)
        
        print("The enemy is shooting...")
        hor_position = str(chr(randrange(len(player_board)) + 65))
        ver_position = randrange(len(player_board))
        enemy_shot = player_board[hor_position][ver_position]
        is_it_previous_guess = enemy_shot == "H" or enemy_shot == "O"
        is_player_ship_hit = enemy_shot == "S"
        
        while is_it_previous_guess:
            hor_position = str(chr(randrange(len(player_board)) + 65))
            ver_position = randrange(len(player_board))
            enemy_shot = player_board[hor_position][ver_position]
            is_it_previous_guess = enemy_shot == "H" or enemy_shot == "O"
            
        if is_player_ship_hit:
            player_force -= 1
            player_board[hor_position][ver_position] = "H"
            print_board(player_board)
            print(f"The enemy shot at {hor_position}{ver_position + 1}! We're hit!!! We're down to {player_force} strength!")
        
        else:
            player_board[hor_position][ver_position] = "O"
            print_board(player_board)
            print(f"The enemy shot at {hor_position}{ver_position + 1}! That's a miss! Thank the gods! We're still at {player_force} strength!")
            
    if player_force == 0:
        print(f"Noob play, Captain! We've lost!!! You've made {shots_taken_by_player} shots in the course of the game.")
    if enemy_force == 0:
        print(f"GG, Captain! We won!!! You've made {shots_taken_by_player} shots in the course of the game.")
        

def run_moderate_mode(enemy_force, player_force):
    shots_taken_by_player = 0
    
    while player_force > 0 and enemy_force > 0:
        print_board(visible_board)
        guess = input(f"The enemy has a force of {enemy_force}! Use the NumberLetter (e.g. A1) format and make a guess! ")
        guess = guess.upper()
        
        if not is_player_input_properly_formatted(guess):
            print("Please use the NumberLetter format. One letter, one number. No more, no less.")
            continue
        
        hor_position = guess[0]
        ver_position = int(guess[1:]) - 1
        
        if not is_player_input_within_bounds(hor_position, ver_position):
            print("Please use one letter, one number, within the gameboard's range.")
            continue
        
        guess_pos = hidden_board[hor_position][ver_position]
        visible_guess_pos = visible_board[hor_position][ver_position]
        is_it_previous_guess = visible_guess_pos == "H" or visible_guess_pos == "O"
        is_ship_hit = guess_pos == "S"
        
        if is_it_previous_guess:
            print("Hey, you've already tried that! You just missed a turn!")
        
        elif is_ship_hit:
            enemy_force -= 1
            visible_board[hor_position][ver_position] = "H"
            print(f"That's a hit!!! You murderer! Those sailors had families... The enemy is left at {enemy_force} strength!")
            shots_taken_by_player += 1
            print_board(visible_board)
        
        else:
            visible_board[hor_position][ver_position] = "O"
            print(f"That's a miss! The enemy is still at {enemy_force} strength!")
            shots_taken_by_player += 1
            print_board(visible_board)
        
        print("The enemy is shooting...")
        enemy_shot = moderate_level_enemy_shoots()
        is_it_previous_guess = enemy_shot == "H" or enemy_shot == "O"
        is_player_ship_hit = enemy_shot == "S"
        
        while is_it_previous_guess:
            enemy_shot = moderate_level_enemy_shoots()
            enemy_shot = player_board[hor_position][ver_position]
            is_it_previous_guess = enemy_shot == "H" or enemy_shot == "O"
            
        if is_player_ship_hit:
            player_force -= 1
            player_board[hor_position][ver_position] = "H"
            print_board(player_board)
            print(f"The enemy shot at {hor_position}{ver_position + 1}! We're hit!!! We're down to {player_force} strength!")
        
        else:
            player_board[hor_position][ver_position] = "O"
            print_board(player_board)
            print(f"The enemy shot at {hor_position}{ver_position + 1}! That's a miss! Thank the gods! We're still at {player_force} strength!")
    
    if player_force == 0:
        print(f"Noob play, Captain! We've lost!!! You've made {shots_taken_by_player} shots in the course of the game.")
    if enemy_force == 0:
        print(f"GG, Captain! We won!!! You've made {shots_taken_by_player} shots in the course of the game.")
        

def moderate_level_enemy_shoots():
    pass


def check_board():
    pass


hidden_board = {}
fill_with_recurring_characters(hidden_board, "X", 10)
visible_board = copy.deepcopy(hidden_board)
player_board = copy.deepcopy(hidden_board)
ship_no_and_length = {"Carriers" : (1, 5), "Battleships" : (2, 4), "Cruisers" : (3, 3), "Submarines" : (3, 3), "Destroyers" : (5, 2)} 
#lehetne ship v vmi class numberrel meg lengthel
enemy_force = 0
player_force = 0

for ship in ship_no_and_length:
    enemy_force += ship_no_and_length[ship][0] * ship_no_and_length[ship][1]
    player_force += ship_no_and_length[ship][0] * ship_no_and_length[ship][1]
    

for placement in ship_no_and_length:
    place_ships(ship_no_and_length[placement][0], ship_no_and_length[placement][1], hidden_board)


intro()
auto_placement_prompt = ""

while auto_placement_prompt.upper() != "MANUAL" or auto_placement_prompt != "AUTO":
    auto_placement_prompt = input("Would you like to place your ships (enter 'Manual') or would you like me to place them automatically (enter 'Auto')? ")
    if auto_placement_prompt.upper() == "MANUAL":
        print("Time to place your ships! Ships can be placed next to one another, but not diagonally.")
        player_place_ship(ship_no_and_length["Carriers"][0], ship_no_and_length["Carriers"][1])
        player_place_ship(ship_no_and_length["Battleships"][0], ship_no_and_length["Battleships"][1])
        player_place_ship(ship_no_and_length["Cruisers"][0], ship_no_and_length["Cruisers"][1])
        player_place_ship(ship_no_and_length["Submarines"][0], ship_no_and_length["Submarines"][1])
        player_place_ship(ship_no_and_length["Destroyers"][0], ship_no_and_length["Destroyers"][1])
        break
    elif auto_placement_prompt.upper() == "AUTO":
        for placement in ship_no_and_length:
            place_ships(ship_no_and_length[placement][0], ship_no_and_length[placement][1], player_board)
        print("Here are your ships!")
        print_board(player_board)
        print()
        break
    else:
        print("I'm sorry, I didn't get that. Please enter 'Manual' or 'Auto'.")


difficulty_prompt = ""

while difficulty_prompt.upper() != "EASY" or difficulty_prompt.upper() != "MODERATE" or difficulty_prompt.upper() != "HARD":
    difficulty_prompt = input("What difficulty would you like to play on? Please enter 'Easy' or 'Moderate'. ")
    
    if difficulty_prompt.upper() == "EASY":       
        run_easy_mode(enemy_force, player_force)
            
    elif difficulty_prompt.upper() == "Moderate":
        run_moderate_mode(enemy_force, player_force)
        
    else:
        print("I'm sorry, I didn't get that. Please enter 'Easy' or 'Moderate'.")