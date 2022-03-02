#!/usr/bin/env python3
from random import randint
import info()
def game()
    while True:
        
        your_choice = input("Make a choice (rock, paper, scissors): ").lower()

        choice = ["rock", "paper", "scissors"] 

        mystery_player = choice[randint (0,2)]

#AND SO THE BATTLES BEGIN!!!!!!
        print(f"\nYou chose {your_choice}, mystery_player chose {mystery_player}.\n")

        if your_choice == mystery_player:
            print("Stalemate!")
        elif your_choice == 'rock':
            if mystery_player == 'paper':
                print("Beat by a piece of paper, YOU LOSE!")
            else:
                print("Who uses scissors against a rock, YOU WIN!")
        elif your_choice == 'paper':
            if mystery_player == 'scissors':
                print("Paper was a mistake, YOU LOSE!")
            else:
                print("Imagine losing to paper, YOU WIN!")
        elif your_choice == 'scissors':
            if mystery_player == 'rock':
                print("You left a scratch, but....still LOSE!")
            else:
                print("Cut them to pieces, YOU WIN!")


        one_more_round = input("Play another round? (y/n): ").lower()
        if one_more_round.lower() != "y":
            break

