#Palindrome Tester, is a phrase a palindrome
#Palindrome is a phrase that is the same forwards and backwards

#Create a function to create a header
def printHeader(text):
    line = ("************************")
    print(line)
    print(f"* {text}")
    print(line)
    

#Clean a string, remove spaces, punctuation, lowercase all letters,
#leaves us with a clean version of the string
#nothing is returned
def clean(phrase):
    letters = "abcdefghijklmnopqrstuvwxyz"
    cleanString = ""
    for i in phrase.lower():
        if i in letters:
            cleanString += i
    return cleanString
    

#Determine if a string is a palindrome
#Will return a clean version of the string = no punctuation, no caps, no spaces
def isPalindrome(phrase):
    cleanString = clean(phrase)
    backwards = cleanString[::-1]
    if cleanString == backwards:
        return True
    return False


#Main Program
printHeader("Palindrome Tester")

phrase = clean("Hello, World!")
printHeader(phrase)
result = isPalindrome(phrase)
print(result)