import sys
VOWELS = ('a', 'e', 'i', 'o', 'u')

def pig_latin(word):
    if (word[0] in VOWELS):
       return (word +"yay")
    else:
       for letter in word:
          if letter in VOWELS:
             return (word[word.index(letter):] + word[:word.index(letter)] + "ay")
    return word

word = ""   
while True:
    word = input("Type in the word or Exit to exit:")
    if (word == "exit" or word == "Exit" or word == "EXIT"):
        print("Goodbye")
        sys.exit()
    else:
        print(pig_latin(word))