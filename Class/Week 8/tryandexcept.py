try:
    val = int(input("Please enter a small positive integer: "))
    print(f"You entered {val}")
except ValueError:
    print("Input not accepted.")