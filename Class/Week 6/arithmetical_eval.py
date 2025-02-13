#arithmetical eval

def add(x, y):
    '''
    adds x,y
    '''
    return(x + y)

def multiply(x, y):
    '''
    multiply x,y
    '''
    return(x * y)
def evaluate(f, x, y):
    '''
    calls the function f with parameters x, y
    f(x, y)'''
    return f(x, y)
def main():
    '''tests the add, multiply, and evaluate functions'''
    print(add(2, 3))
    print(multiply(2, 3))
    print(evaluate(add, 2, 3))
    print(evaluate(multiply, 2, 3))
    
main()
