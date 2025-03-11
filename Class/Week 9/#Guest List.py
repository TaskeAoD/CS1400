#Guest List

from pathlib import Path

contents = input("Please enter First Name: \n")
contents += ' ' #You need the += so it adds instead of overwrites the previous
contents += input("Please enter Last Name: \n") 

path = Path("C:/Users/Taske/Documents/Github/CS1400/Class/Week 9/Guest.txt")
path.write_text(contents)