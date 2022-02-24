#!/usr/bin/env python3
#BEAR, COWBOY, NINJA
#We all know the good old game Rock, Paper, Scissors. But now there's a WAY more fun version - Ninja, Cowboy, Bear*!!


from random import randint


#RULEZ:Ninja beats Cowboy using lighting speed ninja kicks, Cowboy beats Bear with his quick draw and perfect accuracy, Bear beats Ninja with a strong swipe of his clawed paw 

while True:                          
                                    
                                #Similar "(Rock,  Paper, Scissors)
    your_avatar = input("Choose an avatar (bear, cowboy, ninja): ").lower()

#Possible choices for your Avatar
    avatar = ["bear", "cowboy", "ninja"]

#Random avatar for opponent
    mystery_player = avatar[randint (0,2)]

#AND SO THE BATTLES BEGIN!!!!!!
    print(f"\nYou chose {your_avatar}, mystery_player chose {mystery_player}.\n")

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
