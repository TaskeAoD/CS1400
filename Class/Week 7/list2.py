lst = [2*i for i in range(6)]
print(lst)
print(*lst)
print(*lst, sep=' and ', end= '--thats all folks!\n')