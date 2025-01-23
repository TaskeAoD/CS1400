# get multiplication table size from user
size = int(input('Please enter the table size: '))
# Print a size by size multiplication table
for row in range(1, size+1):
    for column in range(1, size+1):
        product = row*column #computes the product
        print('{0:4}'.format(product), end='') #Displays product
    print() #move to the next row