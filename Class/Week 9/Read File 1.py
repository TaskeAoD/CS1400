from pathlib import Path

path = Path("C:/Users/Taske/Documents/Github/CS1400/Class/Week 9/pi_digits.txt")
contents = path.read_text()
print(contents)