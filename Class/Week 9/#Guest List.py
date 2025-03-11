#Guest List

from pathlib import Path

firstname = input("Please enter First Name: \n")
space = ' ' #You need the += so it adds instead of overwrites the previous
lastname = input("Please enter Last Name: \n")
#fullName = (firstname + space + lastname)
fullName = f'{firstname} {lastname}\n'

path = Path("C:/Users/Taske/Documents/Github/CS1400/Class/Week 9/Guest.txt")
path.write_text(fullName)

with open(path) as file_object:
    for line in file_object:
        print(line)