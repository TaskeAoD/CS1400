#Pig Latin

#Variable List
#letter = Helps check for vowels letter by letter
#word = The word itself
#PigLatinWord = The translated word
#index = to log where the vowel is in the word
#FirstVowelIndex

#Functions
#First is isVowel to check to see if there are vowels in the word
def isVowel(letter):
    return letter in 'aeiou' 

#This checks for the vowel location and indexes it's position as 0, 1, 2 etc unless there are no vowels where it indexes as -1    
def FirstVowelPos(word):
    for index, letter in enumerate(word):
        if isVowel(letter):
            return index
    return -1   #Only here to make sure it doesn't freak out when a word with no vowels is used

#The main part of the program, calls to other functions to do smaller work
def GetPigLatinWord(word):
    word = ''.join(char for char in word if char.isalpha()).lower() #Had to add lower to the end because was giving me issues when earlier in line
    if not word:
        return "Please enter an actual word" #If you enter a string of nonsense it will output this because it's detecting there's nothing left to work with
    FirstVowelIndex = FirstVowelPos(word)
    if FirstVowelIndex == 0:
        return word + " in Pig Latin is " + word +'yay'
    elif FirstVowelIndex > 0:
        return word + " in Pig Latin is " + word[FirstVowelIndex:] + word[:FirstVowelIndex] + "ay"
    elif FirstVowelIndex < 0:
        return word + " isn't something that needs to be translated" #Realized after writing this that the single quote messed up the print

while True:
    word = input("Please enter a word to translate to Pig Latin, to quit enter (Over123): ")
    if word == 'Over123':
        print("Quitting the Translator Now.")
        break
    else:
        PigLatinWord = GetPigLatinWord(word)
        print(f"{PigLatinWord}")