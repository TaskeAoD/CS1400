from math import sqrt, pow

sideA = float(input("Enter the value for Side A: "))
sideB = float(input("Enter the value for Side B: "))

print(f"The value entered for Side A is {sideA}")
print(f"The value entered for Side B is {sideB}")

sideA_Squared = pow(sideA, 2)
sideB_Squared = pow(sideB, 2)

sideC_Squared = sideA_Squared + sideB_Squared

sideC = sqrt(sideC_Squared)
print(f"The value of Side C is {sideC}")