#!/usr/bin/env python3
#BEAR, COWBOY, NINJA

# Description/Rules: The bear mauls the ninja to death, the ninja kicks the cowboy's ass, and the cowboy shoots the bear.-----bear beats ninja, ninja beats cowboy, and cowboy shoots bear.-----


import random

#Possible choices for your Avatar
#Similar "Rock,  Paper, Scissors

while True:
    your_avatar = input("Choose an avatar (bear, cowboy, ninja): ")

    avatars = ["bear", "cowboy", "ninja"]
    mystery_player = random.choice(avatars)
    print(f"\nYou chose {your_avatar}, computer chose {mystery_player}.\n")


    if your_avatar == mystery_player:
        print("Stalemate. You both live another day!")
    elif your_avatar == 'bear':
        if mystery_player == 'cowboy':
            print("Bullet through the head, YOU LOSE!")
        else:
            print("You demolished them, YOU WIN!")
    elif your_avatar == 'cowboy':
        if mystery_player == 'ninja':
            print("Without a sound..., YOU LOSE!")
        else:
            print("Bullet through the head, YOU WIN!")
    elif your_avatar == 'ninja':
        if mystery_player == 'bear':
            print("You have been demolished, YOU LOSE!")
        else:
            print("Without a sound..., YOU WIN!")


    one_more_round = input("Challenge another opponent? (y/n): ")
    if one_more_round.lower() != "y":
        break
