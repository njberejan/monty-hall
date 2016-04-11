"""
Your task is to write that computer simulation. Prove that switching doors is best
#by simulating 1000 games using each strategy and comparing the winning percentage.
import random
"""

import random

#need to create three random doors with variables
#need to write function to have computer select random door as winner and assign to variables
#prompt user to input choice of door (this can later be fed into function as "player selection" for purposes of running simulations)
#computer must determine if user input == winning door
#if not, must remove the door that is not the winning door and not the user door
#player must be prompted again to pick between two doors
#must determine if user's second choice is winner or not

door_a = 1

door_b = 2

door_c = 3

random_door = random.randint(1, 3)
print('debug random number: ', random_door)
while True:
    player_door = input("Please choose a door, 1, 2, or 3: ")
    if not player_door.isnumeric():
        print("That's not a number, dummy!")
        continue
    elif int(player_door) > 3:
        print("Please pick between 1 and 3.")
        continue
    else:
        break
