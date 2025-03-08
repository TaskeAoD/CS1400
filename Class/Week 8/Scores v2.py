#Program to get scores from the user, giving an output of high, low, average, and number of scores

def getScore(): #Ask user for score
    while True:
        try:
            score = int(input("Enter a test score (0-100): ")) #Using int since float isn't needed
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError: #Main type of error we'll run into since it's just numbers
            print("Error: Please enter a numeric value.")

def main():
    scores = []
    
    while True:
        action = input("\nEnter 'a' to (a)dd a score or 'c' to (c)omplete: ").strip().lower()
        
        if action == 'a':
            score = getScore()
            scores.append(score)
        elif action == 'c':
            break
        else:
            print("Invalid input. Please enter 'a' to (a)dd a score or 'c' to (c)omplete.").strip().lower()

    if scores:
        print("\nResults:")
        print(f"Lowest Score: {min(scores)}")
        print(f"Highest Score: {max(scores)}")
        print(f"Average Score: {sum(scores) / len(scores):.2f}")
        print(f"Number of Students: {len(scores)}")
    else:
        print("No valid scores entered.")

#Main part of program
main()
