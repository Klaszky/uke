#Smash up score keeper / faction picker
from __future__ import print_function
import random

zero = """
   #  
 #  #  
#    #
#    #
 #  # 
  #   
"""
one = """
   #
  ##
 # #
   #
   #
 #####  
"""
two = """
  ###
#    #
    #  
  #
#
#####
"""
three = """
  ###
#    #
   ##
#    #
 ###
"""
four = """
    ##
  #  #
#    #
######     
     #
     #
"""
five = """
 #####
#     
##
 ####
    ##
#    #
 ####
"""
six = """
  ###
#     #
#
#####
#    #
#    #
 ####
"""
seven = """
 #####
#    #
    #
 #####
  #
 #
"""
eight = """
 ###
#   #
 ###
#   #
 ###
"""
nine = """
 ####
#   # 
#####
   #
  #
 #
"""
ten = """
   #       # 
  ##     #  #
 # #    #    #
   #    #    #
   #     #  #
 #####    #
"""

eleven = """
   #     #
  ##    ##
 # #   # #
   #     #
   #     #
 ##### #####
"""

twelve = """
   #      ###
  ##    #    #
 # #        #
   #      #
   #    #
 #####  #####
"""

thirteen = """
   #       ###
  ##     #    #
 # #        ##
   #          #
   #     #    #
 #####    ###
"""

fourteen = """
   #         ##
  ##       #  #
 # #     #    #
   #     ######
   #          #
 #####        #
"""

fifteen = """
   #      #####
  ##     # 
 # #      ##
   #        ##
   #     #    #
 #####    ####     
"""
sixteen = """
   #      ####
  ##     #    #
 # #     #
   #     ######
   #     #    #
 #####    #### 
 """
seventeen = """
   #      ####
  ##     #    #
 # #         #  
   #     ######
   #       #
 #####    # 
"""
eighteen = """
   #      ####
  ##     #    #
 # #     #    #  
   #      ####
   #     #    #
 #####    ####
"""
nineteen = """
   #      ####
  ##     #    #
 # #     #    #  
   #      ####
   #        #
 #####    ##
"""
twenty = """
  ###        #
#    #     #  #
    #     #    #
  #       #    #
#          #  #
#####       #
"""
smash_up = """
 SSSS                                                 U      U 
S    S                                                U      U
 S                             ssss   h               U      U
  SS                 aa       s    s  h               U      U
    S    mmm mmm    a  a       ss     hhhhh           U      U   pppp
S    S  m   m   m   aaaaa    s    s   h    h           U    U   p    p
 SSSS   m   m   m   a   a     ssss    h    h            UUUU    ppppp
                                                                p
                                                                p
"""


sets_to_be_used = []

org_game = ['Ninja', 'Dinosaur', 'Aliens', 'Wizards', 'Zombies', 'Robot', 'Tricksters', 'Pirates']

over_9k_exp = ['Bear Cavalry', 'Ghosts', 'Killer Plants', 'Steampunks', 'Geeks']

sci_fic_exp = ['Cyborg Apes', 'Shapeshifters', 'Super Spies', 'Time Travelers']

cth_exp = ['Minions of Cthulhu', 'Elder Things', 'Innsmouth', 'Miskatonic University']

mons_exp = ['Giant Ants', 'Mad Scientists', 'Vampires', 'Werewolves']

nums = [zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty]

players = 0

player1 = 0

player2 = 0

player3 = 0

player4 = 0

player_names_list = [player1, player2, player3, player4]



########################################################################################
########################################################################################




class player_class:
    #sets_to_be_used
    def __init__(self, num, factions = [], score=0, name=0):
        self.num = num
        self.score = score
        self.name = class_player_name(self.num)



def class_faction_picker(decks_being_used, player_num):
    menu = 0
    player_to_be_assigned_a_deck = player_names_list[player_num]
    factions_to_be_assigned = player_names_list
    
    while len(factions) < 2:
    
        print( "\n    Faction Menu:    ")
        print( "1.I would like to pick my decks.")
        print( "2.I would like 2 random decks.")
        print( "3.I would like to see a list of available decks.")
    
        try:
            menu = int(raw_input("Please make a choice: "))
    
        except ValueError:
            print( "\nSorry I didn't understand that. Try again.")
            menu = int(raw_input("Please make a choice: "))

        while menu < 1 or menu > 3:
            print( "\nPlease enter a valid menu number.")
            print( "\n    Faction Menu:    ")
            print( "1.I would like to pick my decks.")
            print( "2.I would like 2 random decks.")
            print( "3.I would like to see a list of available decks.")

        if menu == 1:
            pass
        elif menu == 2:
            for i in range(2): 
                rand = random.choice(decks_being_used)
                player.faction.append(rand)
                decks_being_used.remove(rand)



def class_player_name(player_number):

    name_to_return = raw_input("\nPlease enter player {}'s name: ".format(player_number))
    
    while len(name_to_return) < 1 and not name_to_return.isalpha():
    
        print( "Players names' have to be at least one character long containing only letters.")
    
        name_to_return = raw_input("\nPlease enter player {}'s name: ".format(player_number))

    return name_to_return


player1 = player_class(1)
player1.factions = class_faction_picker(org_game, player1.num)

print( player1.factions)

########################################################################################
########################################################################################





def main_loop():  
    
    print( smash_up)
    print( "\n\n")

    sets_to_be_used = which_exp_to_be_used()

    print( "\n\nCool we'll be using: ",)
    
    
    for i in sets_to_be_used:
    
        if i == sets_to_be_used[-1]:
            print( " and " + i)
    
        else:
            print( i + ", ",)

    try:

        players = int(raw_input("\n\nHow many players will be participating? (Min: 2, Max: 4)  "))    
    
    except ValueError:
    
        print( "Please enter a number between two and four.")
        players = int(raw_input("\n\nHow many players will be participating? (Min: 2, Max: 4)  "))
    

    
    while players < 2 or players > 4:
    
        print( "\nSorry there can only be between two and four players.")

        players = int(raw_input("\n\nHow many players will be participating? (Min: 2, Max: 4)  ")) 

    
    for i in range(players):

        player_names_list[i] = player(i) 


    
    for z in range(players):
    
        print( "\n{} will be playing {}.\n".format(player_names_list[z.name], player_factions[z.factions]))


    
    # while win_condition(players):
    
    #     display_score(players)
    #     add_score(players)

    # display_score(players)

    # victor = winner(players)

    # print( "\n\n########################################################################################")
    # print( "****************************************************************************************")
    # print( "########################################################################################")
    # print( "             ~~~~~~~~~~~~~~~~~~~~~~~{} WINS!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     ".format(victor))
    # print( "########################################################################################")
    # print( "****************************************************************************************")
    # print( "########################################################################################\n\n")

def which_exp_to_be_used():

    decks = [org_game, over_9k_exp, cth_exp, sci_fic_exp, mons_exp]
    
    to_return = []

    already_chosen = []
    
    deck_choice = 99

    while (len(to_return) > 1  or deck_choice != 0) and len(already_chosen) < 5:
        
        print( "\n\nWhich decks would you like to use in your game?")
        print( "\n1.Original Factions")
        print( "2.Over 9000 Expansion & Geeks")
        print( "3.Obligatory Cthulhu Expansion")
        print( "4.Science Fiction Expansion")
        print( "5.Monster Expansion")
        print( "6.All Decks")
        print( "0.Exit Deck Selection")
        
        
        try:
            deck_choice = int(raw_input("\nEnter the number for the deck you would like to use: "))

        
        except ValueError:
        
            print( "Please enter a non-negative number between 0-6.")
            deck_choice = int(raw_input("\nEnter the number for the deck you would like to use: "))

        
        while deck_choice > 6 or deck_choice < 0 :

            print( "Sorry I didn't understand that.")
            
            try:
            
                deck_choice = int(raw_input("\nEnter the number for the deck you would like to use: "))
            
            except ValueError:
            
                print( "Please enter a non-negative number between 0-6.")
                deck_choice = int(raw_input("\nEnter the number for the deck you would like to use: "))

        
        if deck_choice not in already_chosen and deck_choice != 0:
            already_chosen.append(deck_choice)
            print( "\nAwesome, I'll add those decks to the list! \n")

        
        elif deck_choice == 0:
            pass

        
        else:
            print( "\n\nYou've already chosen those decks.")

        
        if deck_choice == 6:
            for i in decks:
                for x in i:
                    to_return.append(x)
            return to_return
    
    
    for i in already_chosen:
        for x in decks[i-1]:
            to_return.append(x)
    
    return to_return

def player_names(number_of_players):

    for i in range(number_of_players):
            player_names_list[i] = raw_input("\nPlease enter player {}'s name: ".format(i+1))
            while len(player_names_list[i]) < 1 and not player_names_list[i].isalpha():
                print( "Players names' have to be at least one character long containing only letters.")
                player_names_list[i] = raw_input("\nPlease enter player {}'s name: ".format(i+1))




def faction_picker(decks_being_used, player):

    for i in range(2):
        rand = random.choice(decks_being_used)
        player.append(rand)
        decks_being_used.remove(rand)



def display_score(number_of_players):

    print( "\n################ SCORES ################\n")

    for i in range(number_of_players):
        print( "\n")
        print( player_names_list[i])
        print( nums[player_scores[i]])
        print( "\n")

def add_score(number_of_players):

    for i in range(number_of_players):
        try:
            player_scores[i] += int(raw_input("\nEnter {}'s score for this base: ".format(player_names_list[i])))
        except ValueError:
            print( "Please enter a valid number.")
            player_scores[i] += int(raw_input("\nEnter {}'s score for this base: ".format(player_names_list[i])))


def win_condition(number_of_players):
    highest = 0
    count = 0

    for i in player_scores:
    
        if i > highest:
            count = 0
            highest = i
    
        elif i == highest:
            count += 1

    if highest >= 15 and count < 1:
        return False

    else:
        return True

def winner(number_of_players):
    highest = 0
    for i in range(number_of_players):
        if player_scores[i] > highest:
            highest = player_scores[i]
            won = player_names_list[i]
    return won

if __name__ == "__main__":
    pass
    #main_loop()