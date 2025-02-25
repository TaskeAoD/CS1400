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
    except ValueError as e:
        print("Cannot convert integer", type(e), e)
    except IndexError as e:
        print("List index out of range.", type(e), e)
    except ZeroDivisionError as e:
        print("Cannot divide by 0", type(e), e)
    except Exception as e: #mostly a catch all
        print("There was another type of error.", type(e), e)
    except: #This is the real catch all, has to be the last except block in the try group
        print("There was another unexpected error", type(e), e)
        
    print(f"End of loop iteration: {i}")