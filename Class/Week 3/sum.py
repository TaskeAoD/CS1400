sum = 0
for i in range(5, 101, 5):
    previousSum = sum
    sum += i
    print(f"{previousSum} + {i} = {sum}")
print(f"done {sum}")