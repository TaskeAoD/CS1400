size = 0
def multiplication():
# get multiplication table size from user
    size = int(input('Please enter the table size: '))
# Print a size by size multiplication table
# FIrst print a heading: 1,2,3,4,5,etc
    print("     ", end='')
# Print column heading
    for column in range(1, size + 1):
        print('{0:4}'.format(column), end='')
    print() #prints blank line
# Print line separator
    print(" +", end='')
    for column in range(1, size+1):
        print('-----', end='') #Line separator
    print()
    for row in range(1, size+1):
        print('{0:3} |'.format(row), end='')
        for column in range(1, size+1):
            product = row*column #computes the product
            print('{0:4}'.format(product), end='') #Displays product
        print() #move to the next row