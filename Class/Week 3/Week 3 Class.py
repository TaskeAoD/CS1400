#Learning Loops
#current_number = 0
#while current_number <= 10:
#    print(current_number)
#    current_number += 1

#While Loops
#x = 1
#while x <= 5:
#    print(x)

#Prompt command    
#prompt = "\nTell me something and I will repeat it back to you: "
#prompt += "\nEnter 'quit' to end. "
#message = ""
#active = True
#while active == True:
#    message = input(prompt)
#    if message == 'quit' or  'Quit' or 'QUIT' or 'q' or 'Q':
#        active = False
#    else:
#        print(message)

print("Help, my computer doesn't work.")
done = False #Not done initially
while not done:
    print("Does the computer make any sounds? (Fans, etc)")
    choice = input("or show any lights? (y/n): ")
    #Troubleshooter control logic path
    if choice == 'n': #Computer has no power
        choice = input("Is the computer plugged into the wall? (y/n) ")
        if choice == 'n': #They need to plug it in to the wall
            print("Please plug it in to the wall.")
            done = True
        else: #They have power, just other things wrong
            choice = input("Is the computer in the on position? (y/n) ")
            if choice == 'n': #needs to be powered on
                print("Please turn the computer to the on setting.")
                done = True
            else:
                choice = input("Does the computer have a fuse? (y/n)")
                if choice == 'n': #got no fuse
                    choice = input("Is the power outlet functioning? (y/n)")
                    if choice == 'n':
                        print("Please fix outlet at the breaker ")
                        print("or find another location to plug in.")
                        done = True
                    else: #beyond level 1 support
                        print("Please consult tech for level 2 support.")
                        done = True
                else: #Check fuse
                    print("Please check and replace fuse if necessary.")
                    done = True
    else:
        choice == 'y'
        print("Please consult level 2 support.")
        done = True
        
