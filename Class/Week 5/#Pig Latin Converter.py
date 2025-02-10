#Pig Latin Converter

word = ''
words = ''
#Should return with Pig Latin

#def isvowel(test):   #For some reason I couldn't get this to easily
#    vowels = 'aeiou' #work with the rest, but it did let me test
#    for i in test:   #early on for vowels
#        if i in vowels:
#            print("There are vowels")
#            return
#    else:
#        print("vowels not in here")
#        return

#Now the actual part of the program that converts to Pig Latin
def GetPigLatinWord(words):
    vowels = "aeiou"                  #Was able to get it to check again for
    if words[0].lower() in vowels:  #for vowels, and combined to output earlier
        return word + "yay"           #variable with the correct modifications
    else:
        first_consonants = ""
        for letter in word:
            if letter.lower() not in vowels:
                first_consonants += letter
            else:
                break
        return words[len(first_consonants):] + first_consonants + "ay"

def translate_word(word):
    words = word.split()
    words = [GetPigLatinWord(word) for word in words]
    return " ".join(words)


while word != 'Done':
    word = input("Please Enter Word: (If done with translating enter 'Done') ");
    if word == 'Done':
        print("Quitting translator")
        break
    else:
        translate = translate_word(word)
        print(translate)
        print("Let's try another! ")