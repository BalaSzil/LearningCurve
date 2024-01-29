import random
import copy


def get_inputs():
    
    number_of_tables = get_number_of_tables()
            
    players_per_table, minimum_number_of_players = get_players_per_table(number_of_tables)
    
    total_number_of_players = get_total_number_of_players(minimum_number_of_players)
    
    player_names = get_player_names(total_number_of_players)
    
    return (number_of_tables, players_per_table, total_number_of_players, player_names)
        

def get_number_of_tables():
    
    is_input_correct = False
    
    while is_input_correct == False:
        
        number_of_tables = input("Hány asztalon játszatok? ")
        
        is_appropriate_number = number_of_tables.isnumeric() and int(number_of_tables) <= 10
        
        if is_appropriate_number:
            number_of_tables = int(number_of_tables)
            is_input_correct = True
            
        elif not is_appropriate_number:
            print("Nem megfelelő értéket adtál meg. Kérlek, adj meg egy 10 alatti egész számot!")
            
    return number_of_tables


def get_players_per_table(number_of_tables):
    players_per_table = []
    
    for i in range(number_of_tables):
        
        is_input_correct = False
        
        while is_input_correct == False:
            
            value = input(f"Hány játékos van a(z) {i + 1}. asztalnál? 2 vagy 4? ")
            
            is_appropriate_number = value == "2" or value == "4"
            
            if is_appropriate_number:
                players_per_table.append(int(value))
                is_input_correct = True
            
            elif not is_appropriate_number:
                print("Nem megfelelő számot adtál. Az asztaloknál 2 vagy 4 játékos játszhat.")
    
    minimum_number_of_players = 0
    
    for i in range(number_of_tables):
        minimum_number_of_players += players_per_table[i]        
        
    return (players_per_table, minimum_number_of_players)


def get_total_number_of_players(minimum_number_of_players):
    
    is_input_correct = False
        
    while is_input_correct == False:
        
        total_number_of_players = input("Hány játékos van összesen? ")
        
        is_appropriate_number = total_number_of_players.isnumeric() and int(total_number_of_players) <= 100 and int(total_number_of_players) >= minimum_number_of_players
        
        if is_appropriate_number:
            total_number_of_players = int(total_number_of_players)
            is_input_correct = True
            
        elif not is_appropriate_number:
            print(f"Nem megfelelő értéket adtál meg. Kérlek, adj meg egy egész számot, ami legalább {minimum_number_of_players}, legfeljebb 100!")
    
    return total_number_of_players


def get_player_names(number_of_players):
    player_names = []
    
    for i in range(number_of_players):
        name_of_player = input(f"Mi a neve a(z) {i + 1}. játékosnak? ")
        
        if name_of_player == "":
            name_of_player = input(f"Semmit nem adtál meg. Mi a neve a(z) {i + 1}. játékosnak? ")
        
        player_names.append(name_of_player)

    return player_names


def get_players_playing_at_the_same_time(players_per_table):
    players_playing_at_the_same_time = 0
    
    for key in range(len(players_per_table)):
        players_playing_at_the_same_time += players_per_table[key]
    
    return players_playing_at_the_same_time

        
def get_number_of_possible_match_ups(number_of_tables, total_number_of_players, players_per_table):  
    all_2_player_tables = 2 in players_per_table and 4 not in players_per_table
    all_4_player_tables = 2 not in players_per_table and 4 in players_per_table
    
    total_number_of_players = total_number_of_players - (total_number_of_players % 2)
    
    if all_2_player_tables:
        number_of_possible_match_ups = (total_number_of_players * (total_number_of_players - 1)) / (2 * number_of_tables)
        
    elif all_4_player_tables:
        number_of_possible_match_ups = (total_number_of_players * (total_number_of_players - 1) * (total_number_of_players - 2) * (total_number_of_players - 3)) / (24 * number_of_tables)
    
    elif not all_2_player_tables and not all_4_player_tables:
        number_of_possible_match_ups = total_number_of_players * (total_number_of_players - 1) / all_4_player_tables
        
    if number_of_possible_match_ups > 12:
        number_of_possible_match_ups = 12
    
    print(f"\nLétrehozott játékok száma: {int(number_of_possible_match_ups)}")
    
    return int(number_of_possible_match_ups)


def generate_game_setups(number_of_possible_match_ups, number_of_tables, player_names, players_per_table):
    games_played = []
    games_played_with_players_opposite = []
    
    while len(games_played) != number_of_possible_match_ups:
        
        table_setup = []
        table_setup_with_players_opposite = []
        valid_player_names = copy.deepcopy(player_names)
        
        for table in range(number_of_tables):
            
            players_at_selected_table = set_players_for_one_table(valid_player_names, players_per_table[table])
            table_setup.append(players_at_selected_table)
            
            selected_table_with_opposite_players = reverse_configuration(players_at_selected_table)
            table_setup_with_players_opposite.append(selected_table_with_opposite_players)
        
        added_already = check_if_added_already(games_played, table_setup, players_per_table)
        players_opposite_added_already = check_if_added_already(games_played_with_players_opposite, table_setup, players_per_table)
        
        if not added_already and not players_opposite_added_already:
                games_played.append(table_setup)
                games_played_with_players_opposite.append(table_setup_with_players_opposite)
    
    return games_played


def set_players_for_one_table(valid_player_names, selected_table):
    players_at_selected_table = []
    
    for k in range(selected_table):
        player = random.choice(valid_player_names)
        valid_player_names.remove(player)
        players_at_selected_table.append(player)
            
    return players_at_selected_table


def check_if_added_already(games_played, table_setup, players_per_table):
    
    for table in table_setup:
        players_at_table = len(table)
        
        if players_at_table == 2:
            
            for past_game in games_played:
                
                if table in past_game:
                    return True
                    
        elif players_at_table == 4:
            
            same_players_with_different_invalid_setups = get_invalid_setups(table)
            
            for past_game in games_played:
                
                if table in past_game:
                    return True
                
                elif same_players_with_different_invalid_setups in games_played:
                    return True
                
    return False


def reverse_configuration(table):
   same_table_with_opposite_sides = table[::-1]
   return same_table_with_opposite_sides


def get_invalid_setups(table):
    invalid_setups = []
    
    invalid_setup_1 = table[1] + table[0] + table[2] + table[3]
    invalid_setup_2 = table[0] + table[1] + table[3] + table[2]
    invalid_setup_3 = table[2] + table[3] + table[0] + table[1]
    invalid_setup_4 = table[2] + table[3] + table[1] + table[0]
    invalid_setup_5 = table[3] + table[2] + table[0] + table[1]
    invalid_setup_6 = table[3] + table[2] + table[1] + table[0]
    
    invalid_setups.append(invalid_setup_1)
    invalid_setups.append(invalid_setup_2)
    invalid_setups.append(invalid_setup_3)
    invalid_setups.append(invalid_setup_4)
    invalid_setups.append(invalid_setup_5)
    invalid_setups.append(invalid_setup_6)
    
    return invalid_setups


def print_answers(games_played, number_of_tables, players_per_table, number_of_possible_match_ups):
    
    for i in range(number_of_possible_match_ups):
        print(f"A(z) {i + 1}. játék legyen:\n")
        
        for j in range(number_of_tables):
            
            print(f"{j + 1}. asztal játékosai: {games_played[i][j]}\n")
            
        if (number_of_possible_match_ups - i - 1) != 0:
            print(f"Még {number_of_possible_match_ups - i - 1} konfiguráció van.")        
        
        if (len(games_played) - i - 1) != 0:
            input("Ha jöhet a következő kör, nyomd meg az ENTER billentyűt.\n")
            
    input("\nKifogytunk!!!\nHa szeretnél még egy kört ugyanezekkel a játékosokkal, nyomd meg az ENTER billentyűt.\nHa új játékosokat szeretnél megadni, zárd be és indítsd újra a programot!")
    
number_of_tables, players_per_table, total_number_of_players, player_names = get_inputs()
players_playing_at_the_same_time = get_players_playing_at_the_same_time(players_per_table)
number_of_possible_match_ups = get_number_of_possible_match_ups(number_of_tables, total_number_of_players, players_per_table)

game_is_running = True

while game_is_running:
    games_played = generate_game_setups(number_of_possible_match_ups, number_of_tables, player_names, players_per_table)
    print_answers(games_played, number_of_tables, players_per_table, number_of_possible_match_ups)