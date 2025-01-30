from random import randrange, seed

seed(12)

for i in range(0, 100): #print 100 random numbers
    print(randrange(1, 1001), end = ' ') # range 1...1000 inclusive
print()