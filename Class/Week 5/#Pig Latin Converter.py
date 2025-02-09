#Pig Latin Converter

word = ''
words = ''
#Should return with Pig Latin



def GetPigLatinWord(words):
    vowels = "aeiou"
    if words[0].lower() in vowels:
        return word + "yay"
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
    word = input('Please Enter Word: ');
    if word == 'Done':
        print("Quitting translator")
        break
    else:
        translate = translate_word(word)
        print(translate)