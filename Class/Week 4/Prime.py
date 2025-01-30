from math import sqrt
from time import perf_counter # Stop watch like timer

#max_value = int(input('Display prime values up to what number? '))
max_value = 10000
count = 0
value = 2 #because it's the smallest prime
start = perf_counter() #start/stop watch
while value <= max_value:
    #see if the value is prime
    is_prime = True
    #Try all possible factors from 2 to the value
    trial_factor = 2
    root = sqrt(value) #compute the square root of the value
    while trial_factor <= root:
        if value % trial_factor == 0:
            is_prime = False #Found a factor
            break
        trial_factor += 1
    if is_prime:
        print(value, end=' ') #display prime
    value += 1 #try next potential prime number
elapsed = perf_counter() - start
print(f'Count: {count}, Elapsed TIme: {round(elapsed, 2)} seconds')
