from pathlib import Path

path = Path("C:/Users/Taske/Documents/Github/CS1400/Class/Week 9/pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))