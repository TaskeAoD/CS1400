#ParameterPassing.py

#Pass a parameter to the function

def increment(x):
    print(f"Beginning execution of increment, x = {x}")
    x += 1 #increment x by 1
    print(f"Ending execution of increment, x = {x}")
    return x #Gives value back to be used in other lines
def user_input():
    num = int(input("Please enter a number: "))
    return num

def main():
    x = user_input()
    print(f"Before increment, x = {x}")
    after_incrementX = increment(x)
    print(f"After increment, x = {after_incrementX}")
    
main()