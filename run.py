import random

def play():
  user = input("Choose 'r' for Rock\nChoose 's' for Scissors\nChoose 'p' for Paper")
  computer = random.choice(['r', 'p', 's'])

  