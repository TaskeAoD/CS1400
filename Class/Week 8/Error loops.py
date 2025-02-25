#Multiple Exceptions

import random

for i in range(10):
    
    print("beginning of loop")
    try:
        r = random.randint(1, 4)
        if r == 1:
            print(int("fred"))
        elif r == 2:
            [][2] = 5
        else:
            print(3/0)
    except ValueError:
        print("Cannot convert integer")
    except IndexError:
        print("List index out of range.")
    except ZeroDivisionError:
        print("Cannot divide by 0")
        
    print(f"End of loop iteration {i}")