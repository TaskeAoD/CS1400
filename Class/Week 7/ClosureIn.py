#ClosureIn

def evaluate(f, x, y):
    return f(x, y)

def main():
    a = int(input("Enter an integer: ")) #a is a local or internal variable in this since it is never used outside of the function
    print(evaluate(lambda x, y: False if x == a else True, 2, 3))
    
main()