word = input("Enter a word: ")
vowel_count = 0
for letter in word:
    if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or letter == 'i' or letter == 'I' or letter == 'o' or letter == 'O' or letter == 'u' or letter == 'U':
        print(letter, ',\n', sep='', end='')
        vowel_count += 1
print(f'\nVowel Count was {vowel_count}')
for char in 'abcdefg':
    print(f'[{char}]')
    
