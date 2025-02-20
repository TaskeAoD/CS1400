lst = [1, 2, 3, 4, 5, 6, 7]
print(f"list = {lst}")
obj1 = reversed(lst)
print(lst)
print(f"reversed = {obj1}")
obj2 = lst[::-1]
print(lst)
print(f"obj2 = {obj2}")
obj3 = lst.reverse()
print(lst)
print(f"obj3 = {obj3}")