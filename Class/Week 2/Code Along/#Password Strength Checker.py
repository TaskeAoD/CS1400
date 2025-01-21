#This program uses if and elif conditions to determine if your password is safe
score = 0

print("This test will determine if your password is considered strong.")
print("Please follow instructions carefully and only enter 'Yes', 'Y', 'yes' or 'y' if your password meets the criteria.")
print("If your password does not meet the criteria please answer with 'No', 'N', 'no' or 'n'.")

character = input("Do you have more than 9 characters in your password? ")
if character in "Yesy": #Using the 'if' variable 'in' combination lets you check to see if any of the letters or combinations
    score += 1          # are in the stated variable
elif character in "Non":  #This can be risky because it just looks for characters instead of specific words, but could be useful
    score += 0            # to filter out specific characters if you wanted them to input a password to check for security
    
mix1 = input("Do you have a mix of letters and numbers? ")
if mix1 == 'yes' or mix1 == 'Yes' or mix1 == 'y' or mix1 == "Y": #Using 'or' lets you have different acceptable answers that it
    score += 1                                                   # can recognize as approved
elif mix1 == 'no' or mix1 == 'No' or mix1 == 'n' or mix1 == "N":
    score += 0
    
mix2 = input("Do you use Upper and Lower case letters? ")
if mix2 in "Yesy":
    score += 1
elif mix2 in "Non":
    score += 0

symbol = input("Do you use symbols in your password? ") #This would be a great area for 'in' if you wanted to check for specific symbols
if symbol in "Yesy":                                    # in a password compared to just checking for any letters from yes
    score += 1
elif symbol in "Non":
    score += 0

print(f"You scored {score} on this. Your result is:")
if score == 0:
    print("You need a much stronger password")
elif score == 1:
    print("It's weak, but you can do better.")
elif score == 2:
    print("It's getting there. Definitely better than others.")
elif score == 3:
    print("Your password is pretty strong, just a bit more and you're good!")
elif score == 4:
    print("Your password is strong! Just make sure you change it regularly!")