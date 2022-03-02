#!/usr/bin/env python3
from random import randint

print()
your_wins = 0
mystery_player_wins = 0
tie = 0

while True:
    your_choice = input("Make a choice (Rock, Paper, Scissors): ").lower()
    choice = ["rock", "paper", "scissors"]
    mystery_player = choice[randint (0,2)]


#AND SO THE BATTLES BEGIN!!!!!!
    print(f"\nYou chose {your_choice}, mystery_player chose {mystery_player}.\n")
  
    if your_choice == mystery_player:
        print("\tStalemate!")
        tie+=1
    elif your_choice == 'rock':
        if mystery_player == 'paper':
            print("\tBeat by a piece of paper, YOU LOSE!")
            mystery_player_wins+=1
        else:
            print("\tWho uses scissors against a rock, YOU WIN!")
            your_wins+=1
    elif your_choice == 'paper':
        if mystery_player == 'scissors':
            print("\tPaper was a mistake, YOU LOSE!")
            mystery_player_wins+=1
        else:
            print("\tImagine losing to paper, YOU WIN!")
            your_wins+=1
    elif your_choice == 'scissors':
        if mystery_player == 'rock':
            print("\tYou left a scratch, but....still LOSE!")
            mystery_player_wins+=1
        else:
            print("\tCut them to pieces, YOU WIN!")
            your_wins+=1

    print()
    print("You have "+str(your_wins)+" wins")
    print("The computer has "+str(mystery_player_wins)+" wins")
    print("Tied "+str(tie))
    print()

    play_again = input("Play again? (Y/N) ").lower()
    while play_again not in ['y', 'n']:
        play_again = input("That is not a valid choice. Please try again: ").lower()

    if play_again == 'n':
        break

    print("\n----------------------------")
    print("----------------------------\n")


