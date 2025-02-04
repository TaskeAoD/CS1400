#Count To N
#Count to N and print
n = int(input("Please enter a number to count up from 1: "))

def count_to_n(n):
    for i in range(1, n+1):
        print(i, end=" ")
    print()
print("Going to count to 10:")
count_to_n(10)
print("Going to count to 5:")
count_to_n(5)
print(f"Going to count to {n}:")
count_to_n(n)