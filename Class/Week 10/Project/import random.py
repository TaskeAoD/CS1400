import random

def randCity():
    firsts = ['North', 'East', 'South', 'West', 'New', 'Old']
    middles = ['Wood', 'River', 'Field', 'Lake']
    ends = [' Village', 'burg', ' City', 'Town']
    
    first = random.choice(firsts)
    middle = random.choice(middles)
    end = random.choice(ends)
    
    return f"{first}{middle}{end}"

if __name__ == "__main__":
    for _ in range(5):
        print(randCity())
