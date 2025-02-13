#Using primecode2

import primecode

num = int(input("Enter an Integer: "))
if primecode.is_prime(num):
    print(num, "is prime")
else:
    print(num, "is NOT prime")