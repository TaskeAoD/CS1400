# get multiplication table size from user
size = int(input('Please enter the table size: '))
# Print a size by size multiplication table

for column in range(1, size+1):
    print('{0:4}'.format(column), end='')
print()

for column in range(1, size+1):
    print('-----', end='')
print()
for row in range(1, size+1):
    #print(row#, row)
    for column in range(1, size+1):
        product = row*column #computes the product
        print('{0:4}'.format(product), end='') #Displays product
    print() #move to the next row