#local_counter

def create_counter(n):
    count = 0
    
    def counter():
        nonlocal count
        if count < n:
            count += 1
        return count
    return counter


ctr = create_counter(5)
print(ctr())
print(ctr())
print(ctr())
print(ctr())
print(ctr())
print(ctr())
