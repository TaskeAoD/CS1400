#Program is here to determine how many odds or evens or zeros you enter

num = 0
evencount = 0
oddcount = 0
nullcount = 0 #Using null instead of zero or '0' for better clarity
totalcount = 0 #Debug gave me the ideo for a total count when it showed the individual counts for each variable
while num != 111:
    num = int(input("Please enter a number between 0 and 10. Enter '111' to quit. "))
    if num == 111: #A very deliberate thing to put in to prevent accidental exits
        print(f"You entered a total of {totalcount} numbers, with {oddcount} being odd,\n and {evencount} being even, to include {nullcount} zero(s).")
        break
    if num in [2, 4, 6, 8, 10]: #By using 'in' for both even and odd this will let me avoid extra numbers that I don't want counted.
        evencount += 1
        totalcount += 1
    if num in [1, 3, 5, 7, 9]:
        oddcount += 1
        totalcount += 1
    elif num in [0]: #This will let me still count 0
        nullcount += 1
        totalcount += 1