def GetPigLatinWord(word):
    vowels = "aeiou"
    if word[0].lower() in vowels:
        return word + "yay"
    else:
        first_consonants = ""
        for letter in word:
            if letter.lower() not in vowels:
                first_consonants += letter
            else:
                break
        return word[len(first_consonants):] + first_consonants + "ay"

def translate_word(sentence):
    words = sentence.split()
    pig_latin_words = [GetPigLatinWord(word) for word in words]
    return " ".join(pig_latin_words)

# Example usage:
text = ''
while text != "Done":
    text = str(input("Please enter a word: "))
    if text == "Done":
        print("Quitting Translator")
        break
    else:
        pig_latin_text = translate_word(text)
        print(pig_latin_text)
