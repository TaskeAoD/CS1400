from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n" #You need the += so it adds instead of overwrites the previous
contents += "I also love working with data.\n"

path = Path("C:/Users/Taske/Documents/Github/CS1400/Class/Week 9/Programming.txt")
path.write_text(contents)