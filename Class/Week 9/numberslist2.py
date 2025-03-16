try:
    sum = 0

    numbers = open('numbers.txt', 'r') #Opens numbers.txt in read

    for n in numbers: #This will read each line in numbers.txt and attach it to the variable 'n'
        num = int(n.strip())  # strip() removes any excess whitespace
        print(num) #Prints numbers in file
        sum += num #This will add them all together

    print(f"Sum: {sum}") #Prints the sum
    numbers.close() #Closes file

except FileNotFoundError as err:
    print(err)