#Pig Latin Converter

Vowel = ('a', 'e', 'i', 'o', 'u')

#Should return with Pig Latin
def isVowel(phrase):
    if (phrase[0] in Vowel):
        return (phrase + "yay")
    else:
        for letter in phrase:
            return (phrase[phrase.index(letter):] + phrase[phrase.index(letter)] + 'ay')
        
def FirstVowelPos():
    return
    
def GetPigLatinWord(phrase):
    if isVowel(phrase):
        return phrase
    
    
phrase = ""
while phrase != 'Done':
    phrase = input('Please Enter Word: ');
    if phrase == 'Done':
        print("Quitting translator")
        break
    if GetPigLatinWord(phrase):
        print(phrase)