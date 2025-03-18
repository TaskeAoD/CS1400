#code along TranslatePirate

english_pirate_dict = {
"hello":"ahoy", 
"to":"ta", 
"was":"be", 
"cheat":"hornswaggle", 
"cheating":"hornswaggle'n",
"toilet":"head", 
"hi":"yo-ho-ho", 
"man":"matey",
"pardon":"avast", 
"excuse":"arrrgh", 
"yes":"aye", 
"my":"me", 
"friend":"matey", 
"sir":"matey", 
"miss":"comely wench", 
"stranger":"scurvy dog", 
"officer":"foul blaggart", 
"where":"whar", 
"is":"be", 
"for":"fer", 
"are":"be", 
"am":"be", 
"the":"th", 
"going":"goin", 
"you":"ye", 
"your":"yer", 
"tell":"be tellin", 
"know":"be knowin", 
"far":"many leagues", 
"old":"barnacle-covered", 
"attractive":"comely", 
"happy":"grog-filled", 
"quickly":"smartly", 
"nearby":"broadside", 
"restroom":"head", 
"restaurant":"galley", 
"hotel":"fleabag inn", 
"bar":"Skull & Scuppers", 
"mall":"market", 
"bank":"buried treasure", 
"die":"visit Davey Jones Locker", 
"died":"visited Davey Jones Locker", 
"kill":"keel-haul", 
"killed":"keel-hauled", 
"sleep":"take a caulk", 
"stupid":"addled", 
"after":"aft", 
"stop":"belay", 
"nonsense":"bilge", 
"ocean":"briny deep", 
"go":"get ye", 
"song":"shanty", 
"money":"doubloons", 
"drunk":"three sheets to the wind", 
"food":"grub", 
"nose":"prow", 
"leave":"weigh anchor", 
"cheat":"hornswaggle", 
"forward":"fore", 
"child":"sprog", 
"children":"sprogs", 
"sailor":"swab", 
"lean":"careen", 
"find":"come across", 
"mother":"dear ol mum, bless her black soul", 
"mom":"dear ol mum, bless her black soul", 
"drink":"barrel o rum", 
"of":"o", "there":"thar", 
"my":"me", "mine":"me", 
"gun":"cannon", 
"monkey":"tailed imp", 
"expert":"old smartly", 
"flag":"Jolly Roger", 
"dad":"capn", 
"teacher":"wise sage", 
"phone":"cursed device", 
"computer":"magic box", 
"speak":"parley", 
"person":"landlubber", 
"people":"landlubbers", 
"sir":"matey", 
"hotel":"fleabag", 
"student":"swabbie", 
"boy":"matey", 
"professor":"foul blaggart", 
"restaurant":"galley", 
"students":"swabbies", 
"bathroom":"head"}

#TranslateWords translate single word from english to pirate
#parameters: word
#return pirate version or original if translation isn't in dictionary

def translateWord(word):
    word = word.lower()
    if word in english_pirate_dict:
        return english_pirate_dict[word]
    else:
        return word 

#print(translateWord('weber'))

#Translate Sentence, will translate sentence and return pirate sentence
#parameter: Sentence
#return: Sentence in pirate

def translateSentence(sentence):
    pirateSentence = ''
    words = sentence.split()
    for i in words:
        i = translateWord(i)
        pirateSentence += i + ' '
    return pirateSentence[0].upper() + pirateSentence[1:] +'.'

sentence = ''
while sentence.lower != 'q' and sentence.lower != 'quit':
    sentence = input("Please enter a phrase or sentence you wish to translate in Pirate.\nEnter (q)uit: ")
    print(translateSentence(sentence))
