name = str(input("Please ender your full name here: "))
age = int(input("How old are you in years? "))
school = int(input("How many years have you been in school? "))
percentagelife = (school/age)
percentage = round(percentagelife * 100, 2)

print("Your name is ", name, "and you have been in school for ", percentage,"% of your life.")