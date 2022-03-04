#!/usr/bin/env python3
# Importing randint function
# From random module
from random import randint

# Menu courtesy of "Andy Dolinski's youtube video "https://www.youtube.com/watch?v=63nw00JqHo0&t=207s"
# Initial Menu
# Define the menu() function
def menu():
    print("[1] Rock, Paper, Scissors") # Press 1 to play RPS
    print("[2] Bear, Ninja, Cowboy")   # Press 2 to play BNC
    print("[0] Exit")                  # Press 0 to exit

# Define what happens when option 1 is chosen
def game1():
    your_wins = 0
    mystery_player_wins = 0
    tie = 0

    while True:
        your_choice = input("Make a choice (Rock, Paper, Scissors): ").lower()
# Mystery_players random choices
        choice = ["rock", "paper", "scissors"]
        mystery_player = choice[randint (0,2)]

# AND SO THE BATTLES BEGIN!!!!!!
# Ask user to choose from options defined in your_choice, mystery_player plays random choice
        print(f"\nYou chose {your_choice}, mystery_player chose {mystery_player}.\n")
    
        if your_choice == mystery_player:
            print("\tStalemate!")
            tie+=1 # Add 1 to Tie counter
        elif your_choice == 'rock':
            if mystery_player == 'paper':
                print("\tBeat by a piece of paper, YOU LOSE!")
                mystery_player_wins+=1 # Add 1 to mystery_player_wins counter
            else:
                print("\tWho uses scissors against a rock, YOU WIN!")
                your_wins+=1 # Add 1 to your_wins
        elif your_choice == 'paper':
            if mystery_player == 'scissors':
                print("\tPaper was a mistake, YOU LOSE!")
                mystery_player_wins+=1 # Add 1 to mystery_player_wins counter
            else:
                print("\tImagine losing to paper, YOU WIN!")
                your_wins+=1 # Add 1 to your_wins
        elif your_choice == 'scissors':
            if mystery_player == 'rock':
                print("\tYou left a scratch, but....still LOSE!")
                mystery_player_wins+=1 # Add 1 to mystery_player_wins counter
            else:
                print("\tCut them to pieces, YOU WIN!")
                your_wins+=1 # Add 1 to your_wins

        print("You have "+str(your_wins)+" wins")
        print("The computer has "+str(mystery_player_wins)+" wins")
        print("Tied "+str(tie))
        
        play_again = input("Play again? (Y/N): ").lower()
        while play_again not in ['y', 'n']:
            play_again = input("That is not a valid choice. Please try again: ").lower()

        if play_again == 'n':
            break
        menu()

        print("\n----------------------------")
        print("----------------------------\n")

def game2():      
    your_wins = 0
    mystery_player_wins = 0
    tie = 0

    while True:
        your_avatar = input("Choose an avatar (Bear, Cowboy, Ninja): ").lower() # Similar "(Rock,  Paper, Scissors)
        avatar = ["bear", "cowboy", "ninja"] # Possible choices for your Avatar
        mystery_player = avatar[randint (0,2)] # Random avatar for opponent

# AND SO THE BATTLES BEGIN!!!!!!
        print(f"\nYou chose {your_avatar}, mystery_player chose {mystery_player}.\n")

        if your_avatar == mystery_player:
            print("\n----------------------------")
            print("----------------------------\n")
            print("Stalemate. You both live another day!\n")
            print("\n----------------------------")
            print("----------------------------\n")
            tie+=1 # Add 1 to Tie counter
        elif your_avatar == 'bear':
            if mystery_player == 'cowboy':
                print("\n----------------------------")
                print("----------------------------\n")
                print("Bullet through the head, YOU LOSE!\n")
                print("\n----------------------------")
                print("----------------------------\n")
                mystery_player_wins+=1 # Add 1 to mystery_player_wins counter
            else:
                print("\n----------------------------")
                print("----------------------------\n")
                print("You demolished them, YOU WIN!\n")
                print("\n----------------------------")
                print("----------------------------\n")
                your_wins+=1 # Add 1 to your_wins
        elif your_avatar == 'cowboy':
            if mystery_player == 'ninja':
                print("\n----------------------------")
                print("----------------------------\n")
                print("Without a sound..., YOU LOSE!\n")
                print("\n----------------------------")
                print("----------------------------\n")
                mystery_player_wins+=1 # Add 1 to mystery_player_wins counter
            else:
                print("\n----------------------------")
                print("----------------------------\n")
                print("Bullet through the head, YOU WIN!\n")
                print("\n----------------------------")
                print("----------------------------\n")
                your_wins+=1 # Add 1 to your_wins
        elif your_avatar == 'ninja':
            if mystery_player == 'bear':
                print("\n----------------------------")
                print("----------------------------\n")
                print("You have been demolished, YOU LOSE!\n")
                print("\n----------------------------")
                print("----------------------------\n")
                mystery_player_wins+=1 # Add 1 to mystery_player_wins counter
            else:
                print("\n----------------------------")
                print("----------------------------\n")
                print("Without a sound..., YOU WIN!\n")
                print("\n----------------------------")
                print("----------------------------\n")
                your_wins+=1 # Add 1 to your_wins
        
        # Print the score counter after every round
        print("\nYou have "+str(your_wins)+" wins")
        print("The computer has "+str(mystery_player_wins)+" wins")
        print("Tied "+str(tie))
        
        play_again = input("Play again? (Y/N): ").lower()
        while play_again not in ['y', 'n']:
            play_again = input("That is not a valid choice. Please try again: ").lower()

        if play_again == 'n':
          break

        print("\n----------------------------")
        print("----------------------------\n")


menu()
game = int(input("Choose a game to play: "))
while game != 0:
    if game == 1:
        game1()
        break
    elif game == 2:
        game2()
        break
    else:
        print("invalid option.")

print("\nThanks For playing Goodbye.\n")
