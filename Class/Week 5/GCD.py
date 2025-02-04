def gcd(n1, n2):
    min = n1 if n1 < n2 else n2
    largest_factor = 1
    for i in range(1, min + 1):
        if n1 % i == 0 and n2 % i == 0:
            largest_factor = i
    return largest_factor
def get_int():
    return int(input("Please enter Integer: "))
def main():
    n1 = get_int()
    n2 = get_int()
    print(f"gcd of {n1} and {n2} is {gcd(n1, n2)}")
    
main()