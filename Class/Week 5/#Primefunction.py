#Primefunction.py

from math import sqrt

def is_prime(n):
    """
    determine the prime of a given value
    n is an integer to test for prime
    returns true if n is prime otherwise, returns false
    """
    root = round(sqrt(n)) + 1
    #Try all potential factors from 2 to the sqrt of n
    for trial_factor in range(2, root):
        if n % trial_factor == 0: #is it a factor?
            return False #Found Factor
        return True #No factor found
    
def main():
    """
    Test for prime values for each integer from 2 up to provided value
    by user. if prime, it prints, else no print
    """
    max_value = int(input("Display prime values up to what number: "))
    for value in range(2, max_value +1):
        if is_prime(value):
            print(value)##, end= " ")
    print()

main()