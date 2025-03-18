import random
import string

# Dictionary mapping numbers to letters (1=A, 2=B, ..., 26=Z)
num_to_letter = {i: chr(64 + i) for i in range(1, 27)}

# Dictionary for letter scoring
letter_scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 
    'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

# Generate a 5x5 Boggle board with random letters
def generate_boggle_board():
    return [[num_to_letter[random.randint(1, 26)] for _ in range(5)] for _ in range(5)]

# Display the board
def display_board(board):
    for row in board:
        print(" ".join(row))

# Calculate word score
def calculate_score(word):
    return sum(letter_scores.get(letter.upper(), 0) for letter in word)

# Main function
def play_boggle():
    board = generate_boggle_board()
    print("\nGenerated Boggle Board:")
    display_board(board)

    words = input("\nEnter words you found (separated by space): ").split()
    total_score = sum(calculate_score(word) for word in words)

    print("\nScores for each word:")
    for word in words:
        print(f"{word.upper()}: {calculate_score(word)} points")

    print(f"\nTotal Score: {total_score} points")

# Run the game
play_boggle()
