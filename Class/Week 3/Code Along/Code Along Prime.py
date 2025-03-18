print("This is a Prime Number calculator")

num = 0
while num != -1:
    num = int(input("Enter a positive integer to check if it is Prime or not: (Enter -1 to quit) "))
    if num == -1:
        break
    if num<-1:
        print("Number must be a positive number.")
        continue
    isPrime = True
    for i in range(2, (num//2)+1): #Could not give accurate responses without the 'num//2' included in range statement
        if num % i == 0:
            isPrime = False
            break
    if isPrime == True:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is not a Prime Number")