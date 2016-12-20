'''
Created on Dec 19, 2016

@author: Trayvon
'''

#This file will contain the main menu

def MainMenu():
    # Create a basic text based menu    
    play = 'Play Game'
    ops = 'Options'
    valid = False
    
    print('\tMain Menu\n' +
          'Please choose from the options below\n\n' +
          'Press 1:\t play the game\n' +
          'Press 2:\t Options\n')
    
    
    #validate input
    while(valid == False):
        choice = input('Type your selection here: ')
        
        #player chose to play the game
        if (choice == '1'):
            print('You chose: ', ops)
            valid = True
        
        #player chose the options
        elif (choice == '2'):
            print('You chose: ', play)
            valid = True

    #If the player chose to Play game, execute loop
    
    #If the player chose the options, execute the options
    
MainMenu()