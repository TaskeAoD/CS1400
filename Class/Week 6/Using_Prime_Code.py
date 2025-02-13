#Using Prime Code
def printPrime():
    from primecode import is_prime
    num = int(input("Enter an Integer: "))
    if is_prime(num):
        print(num, "is prime")
    else:
        print(num, "is NOT prime")