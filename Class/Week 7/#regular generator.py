#regular generator

def generate_multiple(m, n):
    count = 0
    while count < n:
        yield m * count
        count += 1
        
def main():
    for mult in generate_multiple(3, 6):
        print(mult, end= ' ')
    print()
    
if __name__ == '__main__':
    main()