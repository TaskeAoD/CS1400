#Multiple Exceptions

import random

for i in range(10):
    
    print(f"beginning of loop {i}")
    try:
        r = random.randint(1, 4)
        if r == 1:
            print(int("fred"))
        elif r == 2:
            [][2] = 5
        elif r == 3:
            print({}[1])
        else:
            print(3/0)
    except ValueError:
        print("Cannot convert integer")
    except IndexError:
        print("List index out of range.")
    except ZeroDivisionError:
        print("Cannot divide by 0")
    except Exception: #mostly a catch all
        print("There was another type of error.")
    except: #This is the real catch all, has to be the last except block in the try group
        print("There was another unexpected error")
        
    print(f"End of loop iteration: {i}")