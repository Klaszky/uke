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
  SS                  aa      s   s   h               U      U
    S    mmm mmm     a  a      ss     hhhhh           U      U   pppp
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
player_two = ''
player_three = ''
player_four = ''


def main_loop():  
    
    print smash_up
    print "\n\n"

    sets_to_be_used = which_exp_to_be_used()

    print "\n\nCool we'll be using: "
    
    for i in sets_to_be_used:
        print i + ", ",

    players = raw_input("\n\nHow many players will be participating? (Max: 4)")

    faction_picker(players)

    menu_choice = 99

    while(menu_choice != 0):

        menu_choice = menu()

        if menu_choice == 1:
            add_score()

def which_exp_to_be_used():
    decks = [org_game, over_9k_exp, cth_exp, sci_fic_exp, mons_exp]
    
    to_return = []

    already_chosen = []
    
    deck_choice = 99

    while len(to_return) > 1  or int(deck_choice) != 0:
        
        print "\n\nWhich decks would you like to use in your game?"
        print "\n1.Original Factions"
        print "2.Over 9000 Expansion"
        print "3.Obligatory Cthulhu Expansion"
        print "4.Science Fiction Expansion"
        print "5.Monster Expansion"
        print "6.All Decks"
        print "0.Exit Deck Selection"
        
        deck_choice = raw_input("\nEnter the number for the deck you would like to use: ")

        while int(deck_choice) < 0 or int(deck_choice) > 6:
            print "Sorry I didn't understand that."
            deck_choice = raw_input("\nEnter the number for the deck you would like to use: ")

        if int(deck_choice) not in already_chosen and int(deck_choice) != 0:
            already_chosen.append(int(deck_choice))
            print "\nAwesome, I'll add those decks to the list! \n"

        elif int(deck_choice) == 0:
            pass

        else:
            print "\n\nYou've already chosen those decks."

        if int(deck_choice) == 6:
            for i in decks:
                for x in i:
                    to_return.append(x)
            return to_return


        
    for i in already_chosen:
        for x in decks[i-1]:
            to_return.append(x)
    return to_return



def add_score():
    pass


def faction_picker(*num_of_players):
    for i in num_of_players:
        
        


def score_keeper():
    pass

def menu_():
    print "\n\n1.Base Broken"
    print "2.Change Score"
    print "9.Quit"
    return choice

if __name__ == "__main__":
    main_loop()