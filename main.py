#Rock, paper, scissors game
import random


def game():
    uInput = input("Enter r for rock, p for paper, or s scissor: ")
    while uInput != 'r' and uInput != 'p' and uInput != 's':
        uInput = input("Invalid ınput. Enter r, p, or s: ")
    if uInput == 'r':
        print("Your move is rock")
    elif uInput == 'p':
        print("Your move is paper")
    elif uInput == 's':
        print("Your move is scissor")
    computer = random.randint(0, 2)
    cMove = 'q'

    if computer == 0:
        cMove = 'r'
        print("Computers move is rock")
    elif computer == 1:
        cMove = 'p'
        print("Computers move is paper")
    elif computer == 2:
        cMove = 's'
        print("Computers move is scissors")

    if cMove == 'r' and uInput == 'r':
        print("Rock X Rock, Tie ")
    elif cMove == 'r' and uInput == 's':
        print("Scissor X Rock, Computer Win! ")
    elif cMove == 'r' and uInput == 'p':
        print("Paper X Rock, Player Win! ")
    elif cMove == 's' and uInput == 'p':
        print("Paper X Scissor, Computer Win! ")
    elif cMove == 's' and uInput == 's':
        print("Scissor X Scissor, Tie! ")
    elif cMove == 's' and uInput == 'r':
        print("Rock X Scissor, Player Win! ")
    elif cMove == 'p' and uInput == 'p':
        print("Paper X Paper, Tie! ")
    elif cMove == 'p' and uInput == 's':
        print("Scissor X Paper, Player Win! ")
    elif cMove == 'p' and uInput == 'r':
        print("Rock X Paper, Computer Win! ")


def play():
    while 1:
        print("Welcome to the rock, paper, scissors")
        game()
        x = int(input("If you want to quit press '1' else press another key"))
        if x == 1:
            break


play()
