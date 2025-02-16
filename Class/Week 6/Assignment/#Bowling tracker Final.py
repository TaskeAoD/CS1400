#Bowling tracker

#Function to get scores
def scores():
    frames = [] #Array for frame scores
    for i in range(10): #Can't go over 10 per frame
        if i < 9: #Frames 1-9 rules
            while True:
                rollOne = int(input(f"Please enter your first roll for Frame {i+1} (1-10): "))
                if 0 <= rollOne <= 10: #In case someone tries to cheat their score.
                    break
                print("It's impossible to roll under 0 or over 10, please enter a valid roll.")
            if rollOne == 10: #Strike rules
                frames.append([10])
                print("STRIKE!!")
            else:
                while True:
                    rollTwo = int(input(f"Please enter your second roll for Frame {i+1} (1-{10-rollOne}): "))
                    if 0 <= rollTwo <= (10 - rollOne):
                        break
                    print("It's impossible to roll under 0 or over 10, please enter a valid roll.")
                frames.append([rollOne, rollTwo])
        
        else: #Frame 10 special rule
            while True:
                rollOne = int(input(f"Please enter your first roll for Frame {i+1} (1-10): "))
                if 0 <= rollOne <= 10:
                    break
                print("It's impossible to roll under 0 or over 10, please enter a valid roll.")
            while True:
                rollTwo = int(input(f"Please enter your second roll for Frame {i+1} (1-{10-rollOne}): "))
                if 0 <= rollTwo <= 10:
                    if rollOne != 10 and rollOne + rollTwo > 10:
                        print("10th frame rules: Your score can't be over 10 unless your first roll was a strike or a spare on the second roll.")
                    else:
                        break
                else: 
                    print("It's impossible to roll under 0 or over 10, please enter a valid roll.")
            #Special rule start        
            if rollOne == 10 or rollOne + rollTwo == 10:
                while True:
                    rollThree = int(input(f"Please enter you third roll for Frame {i+1} (0-10): "))
                    if 0 <= rollThree <= 10:
                        break
                    print("It's impossible to roll under 0 or over 10, please enter a valid roll.")
                frames.append([rollOne, rollTwo, rollThree])
            else:
                frames.append([rollOne, rollTwo])
    return frames

#Function to calculate scores
def scoreCalculator(frames):
    scoreTotal = 0
    for i in range(10):
        frame = frames[i]
        if frame[0] == 10:
            if i < 9:
                extra = sum(frames[i+1][:2]) if len(frames[i+1]) > 1 else frames[i+1][0] + (frames[i+2][0] if i+2 < 10 else 0)
                scoreTotal += 10 + extra
            else:
                scoreTotal += sum(frame)
        elif sum(frame) == 10: #Spare rules
            extra = frames[i+1][0] if i < 9 else 0
            scoreTotal += 10 + extra
        else: #Missed the spare
            scoreTotal += sum(frame)    
    return scoreTotal

#Main call function
def main():
    print("Welcome to the individual score tracker for bowling!")
    print("Each frame you'll need to enter your first and second roll.\nIf it's the 10th frame and you got a strike then you'll enter your third roll too.")
    name = input("Please enter your name: ")
    frames = scores()
    scoreTotal = scoreCalculator(frames)
    print(f"{name}, your total score for this game is {scoreTotal}.")
    if scoreTotal == 300:
        print("Congratulations! You played a perfect game!")
    else:
        print("Nice game!")
    
main()