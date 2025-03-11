#Scoring program for teachers

def getScores(): #Function to get scores
    while True:
        try:
            score = int(input("Enter the score (0-100): ")) #Could use float, but scores entered are whole numbers
            if 0 <= score <= 100:
                return score
            if 0 >= score >= 100:
                print("Score cannot be below 0 or above 100.")
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError: #Main error type
            print("Error: Please enter a whole number to be counted in the scores.")
            
def main():
    scores = [] #Variable array for score collection
    
    while True:
        scoreInput = input("Enter 'a' to (a)dd a score or 'c' to (c)omplete list: ").strip().lower()
        if scoreInput == 'a':
            score = getScores()
            scores.append(score)
        elif scoreInput == 'c':
            break
        else:
            print("Invalid input: Please enter 'a' to (a)dd score or 'c' to (c)omplete list: ").strip().lower()
        
    if score:
        print("\nResults:")
        print(f"Highest Score: {max(scores)}")
        print(f"Lowest Score: {min(scores)}")
        print(f"Average Score(Rounded): {sum(scores)/len(scores):.2f}")
        print(f"Number of Scores input: {len(scores)}")
    else:
        print("No valid scores have been entered.")
        
main()