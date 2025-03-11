#Pi_million

from pathlib import Path

path = Path("C:/Users/Taske/Documents/Github/CS1400/Class/Week 9/pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:502]}...")
print(len(f"{pi_string[:502]}"))