#ParameterPassing.py
#Pass a parameter to the function

def increment(x):
    print(f"Beginning execution of increment, x = {x}")
    x += 1 #increment x by 1
    print(f"Ending execution of increment, x = {x}")
    return x
    
def main():
    x = 5
    print(f"Before increment, x = {x}")
    after_incrementX= increment(x)
    print(f"After increment, x = {after_incrementX}")
    
main()