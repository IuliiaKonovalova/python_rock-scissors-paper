import random

def play():
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

play()