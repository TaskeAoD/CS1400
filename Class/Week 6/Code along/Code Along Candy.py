#Code Along
#Guess how many candy pieces are in the jar with a random number generator and a list

import random

#Function that will generate the number of pieces of candy randomly
def generateCandyInJar():
    return random.randint(50,101)

names = []
guesses = []

print("Welcome!\nThis is a game about counting candy in a jar!\nYou'll have to guess how many pieces in the jar!")

candyInJar = generateCandyInJar()

#Troubleshooting: we will print ot the number of pieces of candy in the jar
#print(candyInJar)

name = ''
guess = 0

#Loop to ask for users names and how many pieces they guess, goes until we quit
while name.lower() != 'q' or name.lower() != 'quit':
    name = input("What is your name? (Enter [q] or [quit] to exit and view winners) ")
    
    if name == 'q' or name == 'quit':
        break
    names.append(name)
    guess = int(input("Enter the pieces of candy that you think are in the jar? (50-100) "))
    guesses.append(guess)
    
winners = []
winners.append(names[0])
winningDistance = abs(guesses[0]-candyInJar)

for i in range (1, len(guesses)):
    distance = abs(guesses[i]-candyInJar)
    if distance == winningDistance:
        winners.append(name[i])
    if distance < winningDistance:
        winners.clear()
        winningDistance = distance
        winners.append(names[i])
print(f"The actual number of pieces of candy in the jar was: {candyInJar}.")
print(f"The winner(s) was/are: {winners}. The number of candy pieces was off by this number: {winningDistance}.")