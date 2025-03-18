


def get_scores():
    frames = []
    for i in range(10):
        if i < 9:  # Frames 1-9
            while True:
                first_roll = int(input(f"Enter first roll for frame {i+1} (0-10): "))
                if 0 <= first_roll <= 10:
                    break
                print("Invalid input! Must be between 0 and 10.")

            if first_roll == 10:  # Strike
                frames.append([10])
                print("Strike!")
            else:
                while True:
                    second_roll = int(input(f"Enter second roll for frame {i+1} (0-{10 - first_roll}): "))
                    if 0 <= second_roll <= (10 - first_roll):
                        break
                    print(f"Invalid input! Second roll must be between 0 and {10 - first_roll}.")
                frames.append([first_roll, second_roll])
        
        else:  # Frame 10 (extra roll allowed for strike/spare)
            while True:
                first_roll = int(input(f"Enter first roll for frame 10 (0-10): "))
                if 0 <= first_roll <= 10:
                    break
                print("Invalid input! Must be between 0 and 10.")

            while True:
                second_roll = int(input(f"Enter second roll for frame 10 (0-10): "))
                if 0 <= second_roll <= 11:
                    if first_roll != 10 and first_roll + second_roll > 10:
                        print("Invalid input! The sum of first two rolls cannot exceed 10 unless first was a strike.")
                    else:
                        break
                else:
                    print("Invalid input!")
            
            if first_roll == 10 or first_roll + second_roll == 10:  # If it's a strike or spare, allow third roll
                while True:
                    third_roll = int(input(f"Enter third roll for frame 10 (0-10): "))
                    if 0 <= third_roll <= 11:
                        break
                    print("Invalid input! Must be between 0 and 10.")
                frames.append([first_roll, second_roll, third_roll])
            else:
                frames.append([first_roll, second_roll])

    return frames

def calculate_score(frames):
    """Calculate the total score based on frames."""
    total_score = 0
    for i in range(10):
        frame = frames[i]
        if frame[0] == 10:  # Strike
            if i < 9:
                bonus = sum(frames[i+1][:2]) if len(frames[i+1]) > 1 else frames[i+1][0] + (frames[i+2][0] if i+2 < 10 else 0)
                total_score += 10 + bonus
            else:
                total_score += sum(frame)
        elif sum(frame) == 10:  # Spare
            bonus = frames[i+1][0] if i < 9 else 0
            total_score += 10 + bonus
        else:  # Open frame
            total_score += sum(frame)
    return total_score

def main():
    print("Welcome to the Bowling Score Calculator!")
    frames = get_scores()
    total_score = calculate_score(frames)
    print(f"Your total score is: {total_score}")

if __name__ == "__main__":
    main()
