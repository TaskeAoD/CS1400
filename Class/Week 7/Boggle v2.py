#Boggle v2

import random

#Dictionary list 1
numToLetter = {
    1:'A', 2:'B', 3:'C', 4:'D', 5:'E',
    6:'F', 7:'G', 8:'H', 9:'I', 10:'J',
    11:'K', 12:'L', 13:'M', 14:'N', 15:'O',
    16:'P', 17:'Q', 18:'R', 19:'S', 20:'T',
    21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'
}
# Dictionary list 2: mapping numbers to letters (1=A, 2=B, ..., 26=Z)
#numToLetter = {i: chr(64 + i) for i in range(1, 27)}
#print(numToLetter)

# Dictionary for letter scoring
letterScores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 
    'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

# Generate a 5x5 Boggle board with random letters
def generateBoggleBoard():
    return [[numToLetter[random.randint(1, 26)] for _ in range(5)] for _ in range(5)]

# Display the board
def displayBoard(board):
    for row in board:
        print(" ".join(row))

# Calculate word score
def calculateScore(word):
    return sum(letterScores.get(letter.upper(), 0) for letter in word)

# Main function
def playBoggle():
    board = generateBoggleBoard()
    print("\nGenerated Boggle Board:\n")
    displayBoard(board)

    totalScore = 0

    print()
    print("Enter words one by one. Type 'QUIT' to end game and get final score.")
    
    while True:
        word = input("Enter a word: ").strip().upper()

        if word == "QUIT":
            break

        wordScore = calculateScore(word)
        print(f"Score for '{word}': {wordScore} points\n")
        totalScore += wordScore

    print(f"\nFinal Total Score: {totalScore} points")

# Run the game
playBoggle()
