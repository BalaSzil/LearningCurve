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
print (f"I have {Carriers} carriers, {Battleships} battleships, {Cruisers} cruisers, {Submarines} submarines, and {Destroyers} destroyers.")
print (f"Carriers are {Carrier_l}, the battleships {Battleship_l}, the cruisers {Cruiser_l}, the submarines {Submarine_l}, and the destroyers {Destroyer_l} large.")
print ("None are placed diagonally.")
# 'Invisible' table with ships here
# Make it visible while testing
import string
import random
rows = (string.ascii_uppercase[0:11])
columns = (range(1,11))
helper = 0
for i in columns:
    print(i, end = " ")
print()
for Y in rows:
    for X in range (10):
        print("X", end = " ")
    print(rows[helper:helper+1])
    helper +=1
guess = input("Use the NumberLetter (e.g. A1) format and make a guess! ")
# Eliminate invalid guesses (l or s than 2 char, 2 letters, 2 numbers)