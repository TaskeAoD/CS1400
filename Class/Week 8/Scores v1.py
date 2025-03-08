def get_valid_score():
    """Prompt user for a valid test score between 0 and 100."""
    while True:
        try:
            score = float(input("Enter a test score (0-100) or type 'done' to finish: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a numeric value.")

def main():
    scores = []
    while True:
        user_input = input("Enter a test score (0-100) or type 'done' to finish: ").strip().lower()
        if user_input == 'done':
            break
        try:
            score = float(user_input)
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid numeric value.")

    if scores:
        print("\nResults:")
        print(f"Lowest Score: {min(scores)}")
        print(f"Highest Score: {max(scores)}")
        print(f"Average Score: {sum(scores) / len(scores):.2f}")
        print(f"Number of Students: {len(scores)}")
    else:
        print("No valid scores entered.")

main()
