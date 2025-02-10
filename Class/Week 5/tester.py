def isvowel(test):
    vowels = 'aeiou'
    for i in test:
        if i in vowels:
            print("There are vowels")
            return
    else:
        print("vowels not in here")
        return

test = ''  
while test != "bad":          
    test = str(input("Type a word: "))
    if test == "bad":
        break
    else:
        isvowel(test)
        print("test complete")