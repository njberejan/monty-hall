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

def gets_computer_pick():
    random_door = random.randint(1, 3)
    return random_door

def gets_player_pick():
    while True:
        player_door = input("Please choose a door, 1, 2, or 3: ")
        if not player_door.isnumeric():
            print("That's not a number, dummy!")
            continue
        elif int(player_door) > 3:
            print("Please pick between 1 and 3.")
            continue
        else:
            return player_door

def gets_player_second_pick(player_door, random_door):
    while True:
        if not int(player_door) == random_door:
            print('Goat!')
            player_door_2 = str(input("Please choose another door, {} or {}: ".format(doors[0], random_door)))
            return player_door_2

def gets_outcome_of_game(player_door_2):
    while True:
        if int(player_door_2) == random_door:
            print('You picked the winning door!')
            break
        else:
            print('A second goat! Have fun with that, loser!')
            break

def removes_picked_doors_from_list(player_door, random_door, doors):
    if int(player_door) == random_door:
        print('should quit now')
    else:
        doors.remove(int(player_door))
        doors.remove(int(random_door))
    return doors

doors = [1, 2, 3]
random_door = gets_computer_pick()
print('debug random number: ', random_door)
player_door = gets_player_pick()
doors = removes_picked_doors_from_list(player_door, random_door, doors)
player_door_2 = gets_player_second_pick(player_door, random_door)
gets_outcome_of_game(player_door_2)
