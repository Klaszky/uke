#Smash up score keeper / faction picker
from random import choice

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
   #     #    #
   #      ###
 #####
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
 S                             sss    h               U      U
  SS                 aa       s   s   h               U      U
    S    mmm mmm    a  a       ss     hhhhh           U      U   pppp
S    S  m   m   m   aaaaa    s   s    h    h           U    U   p    p
 SSSS   m   m   m   a   a     sss     h    h            UUUU    ppppp
                                                                p
                                                                p
"""

org_game = ['Ninja', 'Dinosaur', 'Aliens', 'Wizards', 'Zombies', 
    'Robot', 'Tricksters', 'Pirates']

over_9k_exp = ['Bear Cavalry', 'Ghosts', 'Killer Plants', 'Steampunks']

sci_fic_exp = ['Cyborg Apes', 'Shapeshifters', 'Super Spies', 'Time Travelers']

cth_exp = ['Minions of Cthulhu', 'Elder Things', 'Innsmouth', 'Miskatonic University']

mons_exp = ['Giant Ants', 'Mad Scientists', 'Vampires', 'Werewolves']

nums = [one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty]

sets_to_be_used = []

player_one = ''
player_one_score = 0

player_two = ''
player_two_score = 0

player_three = ''
player_three_score = 0

player_four = ''
player_four_score = 0

def main_loop():  
    
    print smash_up
    print "\n\n"

    sets_to_be_used = which_exp_to_be_used()

    print "\n\nCool we'll be using: ",
    
    for i in sets_to_be_used:
        if i == sets_to_be_used[-1]:
            print " and " + i
        else:
            print i + ", ",

    players = int(raw_input("\n\nHow many players will be participating? (Min:2, Max: 4)  "))

    while players < 2 or players > 4:
        print "\nSorry there can only be between 2 and four players."
        players = int(raw_input("\n\nHow many players will be participating? (Min:2, Max: 4)  "))      

    faction_picker(players)

    # menu_choice = 99

    # while(menu_choice != 0):

    #     menu_choice = menu()

    #     if menu_choice == 1:
    #         add_score()

def which_exp_to_be_used():
    decks = [org_game, over_9k_exp, cth_exp, sci_fic_exp, mons_exp]
    
    to_return = []

    already_chosen = []
    
    deck_choice = 99

    while len(to_return) > 1  or deck_choice != 0:
        
        print "\n\nWhich decks would you like to use in your game?"
        print "\n1.Original Factions"
        print "2.Over 9000 Expansion"
        print "3.Obligatory Cthulhu Expansion"
        print "4.Science Fiction Expansion"
        print "5.Monster Expansion"
        print "6.All Decks"
        print "0.Exit Deck Selection"
        
        deck_choice = int(raw_input("\nEnter the number for the deck you would like to use: "))

        while deck_choice > 6 or deck_choice < 0 :
            print "Sorry I didn't understand that."
            deck_choice = int(raw_input("\nEnter the number for the deck you would like to use: "))

        if deck_choice not in already_chosen and deck_choice != 0:
            already_chosen.append(deck_choice)
            print "\nAwesome, I'll add those decks to the list! \n"

        elif deck_choice == 0:
            pass

        else:
            print "\n\nYou've already chosen those decks."

        if deck_choice == 6:
            for i in decks:
                for x in i:
                    to_return.append(x)
            return to_return
    
    for i in already_chosen:
        for x in decks[i-1]:
            to_return.append(x)
    return to_return


def faction_picker(num_of_players):

    if num_of_players == 2:
        player_one = raw_input("\nPlease enter player one's name: ")
        player_two = raw_input("\nPlease enter player two's name: ")
    
    elif num_of_players == 3:
        player_one = raw_input("\nPlease enter player one's name: ")
        player_two = raw_input("\nPlease enter player two's name: ")
        player_three = raw_input("\nPlease enter player three's name: ")
    
    else:
        player_one = raw_input("\nPlease enter player one's name: ")
        player_two = raw_input("\nPlease enter player two's name: ")
        player_three = raw_input("\nPlease enter player three's name: ")
        player_four = raw_input("\nPlease enter player four's name: ")

def add_score():
    pass

def score_keeper():
    pass

def menu_():
    print "\n\n1.Base Broken"
    print "2.Change Score"
    print "9.Quit"
    return choice

if __name__ == "__main__":
    main_loop()