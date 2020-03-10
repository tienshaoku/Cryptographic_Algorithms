#!/usr/bin/python

upperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettersAndSpaces = upperLetters + upperLetters.lower() + " \t\n"

def loadDictionary():
    englishWords = {}
    dictionary = open("dictionary.txt")
    for word in dictionary.read().split('\n'):
        englishWords[word] = None
    dictionary.close()
    return englishWords

englishWords = loadDictionary()

def wordsCount(context):
    context = context.upper()
    context = removeNonLetter(context)
    words = context.split()
    if words == []:
        return 0
    
    matches = 0
    for word in words:
        if word in englishWords:
            matches += 1
    # float() is for the compatibility of Python 2
    return float(matches) / len(words)
    
def removeNonLetter(context):
    processed = []
    for letter in context:
        if letter in lettersAndSpaces:
            processed.append(letter)
    return ''.join(processed)

def isEnglish(context, wordPercentage = 0.3, letterPercentage = 0.75):
    wordsMatch = wordsCount(context) >= wordPercentage
    onlyWords = removeNonLetter(context)
    lettersMatch = (float(len(onlyWords) ) / len(context) ) > letterPercentage
    return wordsMatch and lettersMatch
    

