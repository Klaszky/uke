#Smashup Randomizer with a class system
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




############## Decks of Cards #################
nums = [zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty]

org_game = ['Ninja', 'Dinosaur', 'Aliens', 'Wizards', 'Zombies', 'Robot', 'Tricksters', 'Pirates']

over_9k_exp = ['Bear Cavalry', 'Ghosts', 'Killer Plants', 'Steampunks', 'Geeks']

sci_fic_exp = ['Cyborg Apes', 'Shapeshifters', 'Super Spies', 'Time Travelers']

cth_exp = ['Minions of Cthulhu', 'Elder Things', 'Innsmouth', 'Miskatonic University']

mons_exp = ['Giant Ants', 'Mad Scientists', 'Vampires', 'Werewolves']

################ Player class ###############
class player:
    def __init__(self, num, score=0):
        self.num = num
        self.factions = []
        self.score = 0
        self.name = class_player_name(self.num)

def class_player_name(player_number):

    name_to_return = raw_input("\nPlease enter player {}'s name: ".format(player_number))
    
    while len(name_to_return) < 1 and not name_to_return.isalpha():
    
        print( "Players names' have to be at least one character long containing only letters.")
    
        name_to_return = raw_input("\nPlease enter player {}'s name: ".format(player_number))

    return name_to_return

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
    
    return to_retur

def factions_distribution(decks_being_used, players_in_game, num_of_players):

    menu = 99

    print( "\n    Faction Menu:    ")
    print( "1.We would like to pick our decks.")
    print( "2.We would like 2 random decks.")

    try:
        menu = int(raw_input("Please enter your choice: "))
    except ValueError:
        print("Please enter only 1 or 2.")
        menu = int(raw_input("Please enter your choice: "))

    while menu > 2 or menu < 1:
        try:
            print("Please enter only 1 or 2.")
            menu = int(raw_input("Please enter your choice: "))
        except ValueError:
            print("Please enter only 1 or 2.")
            menu = int(raw_input("Please enter your choice: "))

    if menu == 1:
        
        printable_decks = list(enumerate(decks_being_used, start=1))

        for n, z in printable_decks:
            print(n, z)

        print("\n\nPlease enter the number that corresponds to the deck you would like: ")

        for i in range(num_of_players):

            try:
                faction1 = int(raw_input("\n\nPlease enter player {}'s first faction.".format(i+1)))
            except ValueError:
                print("Sorry I didn't understand that. Try again.")
                faction1 = int(raw_input("\n\nPlease enter player {}'s first faction.".format(i+1)))

            while faction1 > printable_decks[-1][0] or faction1 < 0:
                try:
                    print("Sorry that wasn't in the expected range. Try again.")
                    faction1 = int(raw_input("\n\nPlease enter player {}'s first faction.".format(i+1)))
                except ValueError:
                    print("Sorry I didn't understand that. Try again.")
                    faction1 = int(raw_input("\n\nPlease enter player {}'s first faction.".format(i+1)))

            fact_player = players_in_game[i]
            fact_player.factions.append(printable_decks[faction1-1][1])
            
            decks_being_used.remove(printable_decks[faction1-1][1])
            printable_decks = list(enumerate(decks_being_used, start=1))
            for n, z in printable_decks:
                print(n, z)


        for x in range(num_of_players):

            try:
                faction2 = int(raw_input("\n\nPlease enter player {}'s second faction.".format(i+1)))
            except ValueError:
                print("Sorry I didn't understand that. Try again.")
                faction2 = int(raw_input("\n\nPlease enter player {}'s second faction.".format(i+1)))
            while faction2 > printable_decks[-1][0] or faction1 < 0:
                try:
                    faction2 = int(raw_input("\n\nPlease enter player {}'s second faction.".format(i+1)))
                except ValueError:
                    print("Sorry I didn't understand that. Try again.")
                    faction2 = int(raw_input("\n\nPlease enter player {}'s second faction.".format(i+1)))

            fact_player = players_in_game[x]
            fact_player.factions.append(printable_decks[faction2-1][1])

            decks_being_used.remove(printable_decks[faction1-1][1])
            printable_decks = list(enumerate(decks_being_used, start=1))
            for n, z in printable_decks:
                print(n, z)

    else:

        for p in players_in_game:

            for d in range(2):
            
                rand = random.choice(decks_being_used)
                p.factions.append(rand)
                decks_being_used.remove(rand)

def win_condition(number_of_players, players_in_game):
    highest = 0
    tie = 0


    for i in range(number_of_players):

        if players_in_game[i].score > highest:
            tie = 0
            highest = players_in_game[i].score
    
        elif players_in_game[i].score == highest:
            tie += 1

    if highest >= 15 and tie < 1:
        return False

    else:
        return True

def winner(number_of_players, players_in_game):
    highest = 0
    for i in range(number_of_players):
        if players_in_game[i].score > highest:
            highest = players_in_game[i].score
            won = players_in_game[i].name
    return won

def display_score(number_of_players, players_in_game):

    print( "\n################ SCORES ################\n")

    for i in range(number_of_players):
        print( "\n")
        print( players_in_game[i].name)
        print( nums[players_in_game[i].score])
        print( "\n")

def add_score(number_of_players, players_in_game):
    for i in range(number_of_players):
        try:
            players_in_game[i].score += int(raw_input("\nEnter {}'s score for this base: ".format(players_in_game[i].name)))
        except ValueError:
            print( "Please enter a valid number.")
            players_in_game[i].score += int(raw_input("\nEnter {}'s score for this base: ".format(players_in_game[i].name)))

def welcome():
    
    print(smash_up)

    decks = which_exp_to_be_used()

    number_of_players = int(raw_input("How many players will be joining the game? (Min2, Max4)"))

    if number_of_players == 2:
        player1 = player(1)
        player2 = player(2)
        players = [player1, player2]

    elif number_of_players == 3:
        player1 = player(1)
        player2 = player(2)
        player3 = player(3)
        players = [player1, player2, player3]

    else:
        player1 = player(1)
        player2 = player(2)
        player3 = player(3)
        player4 = player(4)
        players = [player1, player2, player3, player4]

    factions_distribution(decks, players, number_of_players)

    for i in range(number_of_players):
        print("{} will be playing {}".format(players[i].name, players[i].factions))


    while win_condition(number_of_players, players):
        display_score(number_of_players, players)
        add_score(number_of_players, players)

    display_score(number_of_players, players)

    victor = winner(number_of_players, players)

    print( "\n\n########################################################################################")
    print( "****************************************************************************************")
    print( "########################################################################################")
    print( "             ~~~~~~~~~~~~~~~~~~~~~~~{} WINS!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     ".format(victor))
    print( "########################################################################################")
    print( "****************************************************************************************")
    print( "########################################################################################\n\n")

if __name__ == '__main__':
    welcome()