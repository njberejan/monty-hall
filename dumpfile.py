"""
Your task is to write that computer simulation. Prove that switching doors is best
#by simulating 1000 games using each strategy and comparing the winning percentage.
import random
"""

import random

#need to create three random doors with variables
#need to write function to have computer select random door as winner and assign to variables
#prompt user to input choice of door (this can later be fed into function as "CPUplayer selection" for purposes of running simulations)
#computer must determine if user input == winning door
#if not, must remove the door that is not the winning door and not the user door
#CPUplayer must be prompted again to pick between two doors
#must determine if user's second choice is winner or not

def gets_computer_pick():
    random_door = random.randint(1 , 3)
    return random_door

def gets_CPUplayer_pick():
    CPUplayer_door = random.randint(1 , 3)
    return CPUplayer_door

def gets_CPUplayer_second_pick(CPUplayer_choices_list):
    CPUplayer_door_2 = random.choice(CPUplayer_choices_list)
    return CPUplayer_door_2

def gets_outcome_of_game(CPUplayer_door_2, random_door):
    if CPUplayer_door_2 == random_door:
        print("CPU player wins")
    else:
        print("CPU player loses")

def main():

    CPUplayer_choices_list = [1, 2, 3]
    #list of available choices to CPU player
    random_door = gets_computer_pick()
    #determines which door has the prize behind it
    print('debug random number: ', random_door)
    CPUplayer_door = gets_CPUplayer_pick()
    #returns a random guess from the CPU player
    print('debug CPUplayer_door: ', CPUplayer_door)
    CPUplayer_choices_list.remove(CPUplayer_door)
    if CPUplayer_door == random_door:
        print("The CPU player wins!")
        exit()
    #removes CPU player's first guess from list of available guesses.
    print('debug CPUplayer_choices_list: ', CPUplayer_choices_list)
    CPUplayer_door_2 = gets_CPUplayer_second_pick(CPUplayer_choices_list)
    #returns a second guess from remaining guesses in list.
    print('debug CPUplayer_door_2: ', CPUplayer_door_2)
    gets_outcome_of_game(CPUplayer_door_2, random_door)

#IF STATEMENT. IF COMPUTER 2nd CHOICE = 1st CHOICE, COUNT WIN OR LOSS (dictionary with win and loss as key, and number as value?)
main()
