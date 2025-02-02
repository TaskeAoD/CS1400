#Kangaroo Zoo Prices:
#3 and under = 6; adult = 12;
#Passes 3 and under = 50; adult = 85

underprice = 6 #Price for 3 and under
under = 0 #Amount of 3 and under; formula is under*price
overprice = 12 #Price for adults
over = 0 #Amount of Adults; formula is over*price
flopper3price = 50 #Price for 3 and under pass
flopper3pass = 0 #Amount of 3 and under passes; formula is pass*price
flopper18price = 85 #Price for Adult Pass
flopper18pass = 0 #Amount of Adult Passes; formula is pass*price
total = 0

print("Welcome to Kangaroo Zoo!\n Please choose an option:")
print("1. Cost Estimate\n2. Quit")
choiceA = int(input("Enter Choice: "))
while choiceA != 0:
    if choiceA == 2:
        print("Have a bouncy day!")
        break
    if choiceA == 1:
        print("Let's figure out your cost!")
        under = int(input("How many young jumpers will there be? "))
        over = int(input("How many adults will be accompanying them? "))
        choiceB = int(input("Will you be buying any Flopper Passes? 1(Yes), 2(No) "))
        totalA = (underprice*under)+(overprice*over)
        if choiceB == 2:
            print(f"Your total will be ${totalA}.")
            choiceA = int(input("Would you like to start over? 1(Yes), 2(No) "))
            
        if choiceB == 1:
            flopper3pass = int(input("How many Passes for Young Floppers would you like? "))
            flopper18pass = int(input("How many Adult Passes do you need? "))
            totalB = (flopper3pass*flopper3price)+(flopper18pass*flopper18price)
            print(f"Your total is {totalA + totalB}")
            choiceA = int(input("Would you like to start over? 1(Yes), 2(No) "))
            