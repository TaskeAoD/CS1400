from math import sqrt #Contains the def of is_prime function
import math
def is_prime(n):
    trial_factor = 2
    root = sqrt(n)
    
    while trial_factor <= root:
        if n % trial_factor == 0: #Is trial factor a factor
            return False #if Yes then return right away
    trial_factor += 1 #start considering the next factor
    
    return True #tried them all, must be prime