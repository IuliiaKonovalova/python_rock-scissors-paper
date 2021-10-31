import random
import os
from simple_term_menu import TerminalMenu

def play():
    user = ''
    while user not in ['r', 'p', 's']:
      user = input("Choose 'r' for Rock\nChoose 's' for Scissors\nChoose 'p' for Paper\n").lower()
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print('tie')
    elif is_win(user, computer):
        print('you won')
    else:
        print('you lost')

def is_win(player, comp):
    #returns true if the player is a winner
    if (player == 'r' and comp == 's') or (player == 's' and comp == 'p') or (player == 'p' and comp == 'r'):
        return True


def main():
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # Shows welcoming message
    print('Welcome to Rock-Scissors-Paper')
    # Presents options for the user
    options = ['1. Yes', '2. Quit']
    main_menu = TerminalMenu(options)
    quitting = False
    while quitting is not True:
        options_index = main_menu.show()
        options_choice = options[options_index]
        if options_choice == '2. Quit':
            quitting = True
        else:
            play()

main()