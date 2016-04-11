"""
Your task is to write that computer simulation. Prove that switching doors is best
#by simulating 1000 games using each strategy and comparing the winning percentage.
import random
"""
# REMOVE ITEM FROM LIST THAT IS NOT RANDOM DOOR AND NOT PLAYER DOOR
import random
won_and_stuck_to_guns = 0
won_and_changed_course = 0
computer_losses = 0
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

def opens_door(host_choices_list):
    return host_choices_list[0]

def gets_CPUplayer_second_pick(CPUplayer_choices_list):
    CPUplayer_door_2 = random.choice(CPUplayer_choices_list)
    return CPUplayer_door_2

def main(won_and_stuck_to_guns, won_and_changed_course, computer_losses):
    host_choices_list = [1, 2, 3]
    CPUplayer_choices_list = [1, 2, 3]
    #list of available choices to CPU player

    random_door = gets_computer_pick()
    #determines which door has the prize behind it

    print('debug random number: ', random_door)

    CPUplayer_door = gets_CPUplayer_pick()
    #returns a random guess from the CPU player

    print('debug CPUplayer_door: ', CPUplayer_door)

    host_choices_list.remove(random_door)
    #removes the winning door from the possible doors for the host to open

    if CPUplayer_door != random_door:
        host_choices_list.remove(CPUplayer_door)
        #removes the player's door from the possible doors for the host to open

    opened_door = opens_door(host_choices_list)
    #host opens the door that is not the player's choice and not the winning door

    CPUplayer_choices_list.remove(opened_door)
    #removes the open door from the list of possible choices for CPU player to PICK

    CPUplayer_door_2 = gets_CPUplayer_second_pick(CPUplayer_choices_list)
    #determines whether CPU player sticks with original guess or chooses to open the other door.

    if CPUplayer_door == CPUplayer_door_2 and CPUplayer_door == random_door:
        won_and_stuck_to_guns += 1
    #if second choice same as first choice which is same as winning door:
    elif CPUplayer_door != CPUplayer_door_2 and CPUplayer_door_2 == random_door:
        won_and_changed_course += 1
    #if second choice different from first choice but same as winning door:
    else:
        computer_losses += 1
    #if computer lost
    return won_and_stuck_to_guns, won_and_changed_course, computer_losses

#IF STATEMENT. IF COMPUTER 2nd CHOICE = 1st CHOICE, COUNT WIN OR LOSS (dictionary with win and loss as key, and number as value?)
for _ in range(1000):
    won_and_stuck_to_guns, won_and_changed_course, computer_losses = main(won_and_stuck_to_guns, won_and_changed_course, computer_losses)
print(won_and_stuck_to_guns)
print(won_and_changed_course)
print(computer_losses)
