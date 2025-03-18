#Battleship One Sided
import math
from random import randint
from time import sleep
shipA = 0 #Ship Location A
shipB = 0 #Ship Location B
coordA = 0 #Player choice A
coordB = 0 #Player choice B
turn = 0
def distance(shipA, shipB, coordA, coordB):
    return math.sqrt((coordA - shipA)**2 + (coordB - shipB)**2) #Your Choices subtract Ship Location squared to remain positive
dist = distance(shipA, shipB, coordA, coordB)
print("Welcome to Battleship! Would you like to play?")
play = int(input("Please select from the following options:\n1. Yes; 2. No; 3. Teach me. "))
while play != 0:
    if play == 2:
        print("Have a great day!")
        break
    if play == 1:
        print("Setting up game, please wait.")
        shipA = randint(1, 10)
        shipB = randint(1, 10)
        for count in range(10, -1, -1):
            print(f"{count} turns left.")
            sleep(1)
            if turn == 10:
                play = int(input("You didn't sink it this time, would you like to try again? "))
                turn = 0
            coordA = int(input("Please enter your 'X' Coordinate: "))
            coordB = int(input("Please enter your 'Y' Coordinate: "))
            if coordA == shipA and coordB == shipB:
                print("Thats a hit! You sank my Submarine!")
                turn += 1
                print(f"You sank it in {turn} guesses!")
                turn = 0
                play = int(input("Would you like to play again? "))
                break
            else:
                print("Try again!")
                def distance(shipA, shipB, coordA, coordB):
                    return math.sqrt((coordA - shipA)**2 + (coordB - shipB)**2)
                dist = distance(shipA, shipB, coordA, coordB)
                print(f"You were {round(dist, 2)}km off from hitting it!")
                turn += 1

    if play == 3:
        print("This version of Battleship is played with just you and the computer.")
        print("When the game starts the computer will place a submarine and your task")
        print("is to sink it in as few turns as possible.\nYou have 10 attempts in a 10x10 kilometer field.")
        play = int(input("Would you like to play? "))