import random

def play():
    user = input("Choose 'r' for Rock\nChoose 's' for Scissors\nChoose 'p' for Paper").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'you won'
    return 'you lost'

