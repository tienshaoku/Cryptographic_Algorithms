#!/usr/bin/python

import pyperclip, sys, random, copy
import makeWordPattern as MWP
import wordPatterns

Symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    message = input("This is Substitution Cipher.\nEnter your message here: ")
    mode = input("Enter encrypt or decrypt: ")
    processed = ""
    while mode != "encrypt" and mode != "decrypt":
        print("False input, please enter 'encrypt' or 'decrypt'")
        mode = input("Enter encrypt or decrypt: ")
    if mode == "encrypt":
        key = int(input("Enter a random seed here: "))
        random.seed(key)
        processed = encrypt(message)
    else:
        mode = int(input("Decrypt with key (1) or without key (2)? Please Enter 1 or 2: "))
        while mode != 1 and mode != 2:
            print("False input, please enter 1 or 2")
            mode = int(input("Decrypt with key (1) or without key (2)? Please Enter 1 or 2: "))
        if mode == 1:
            key = input("Please enter your key: ")
            processed = decryptWithKey(message, key)
        else:
            mappedList = decryptWithoutKey(message)
            sheet = ""
            print("Undecrypted words are: ")
            for key in mappedList:
                if len(mappedList[key]) != 1:
                    print(key + " can be: ")
                    print(mappedList[key])
                    sheet += "_"
                else:
                    sheet += mappedList[key][0]
            print("\nThe decrypted message is: ")
            for letter in message:
                if letter.upper() in Symbols:
                    index = Symbols.find(letter.upper())
                    processed += sheet[index]
                else: 
                    processed += letter
    pyperclip.copy(processed)
    print(processed)


def encrypt(mes):
    encrypted = ""
    arr = list(Symbols)
    sheet = []
    for i in range(26):
        ran = random.randint(0, 25 - i)
        sheet.append(arr.pop(ran))
    print("The encryptoin key is: %s" %"".join(sheet) )

#   Another shuffle approach:
#   sheet = list(Symbols)
#   random.shuffle(sheet)
#   sheet = ''.join(sheet)

    for symbol in mes:
        if symbol.upper() in Symbols:
            index = Symbols.find(symbol.upper())
            encrypted += sheet[index]
        else:
            encrypted += symbol
    return encrypted

def decryptWithKey(mes, key):
    decrypted = ""
    for symbol in mes:
        if symbol in Symbols:
            index = key.find(symbol)
            decrypted += Symbols[index]
        else:
            decrypted += symbol
    return decrypted

def makeLetterList():
    letterList = {}
    for i in range(65, 91):
        letterList[str(chr(i))] = []
#    print(letterList)
    return letterList

def intersectList(l1, l2):
    intersectedList = makeLetterList()
    for letter in Symbols:
        if l1[letter] == []:
            intersectedList[letter] = copy.deepcopy(l2[letter])
        elif l2[letter] == []:
            intersectedList[letter] = copy.deepcopy(l1[letter])
        else:
            for mappedLetter in l1[letter]:
                if mappedLetter in l2[letter]:
                    intersectedList[letter].append(mappedLetter)
    return intersectedList

def cleanseList(l):
    again = True
    while again:
        again = False
        solved = []
        for letter in Symbols:
            if len(l[letter]) == 1:
                solved.append(l[letter][0])
        for letter in Symbols:
            for s in solved:
                if len(l[letter]) != 1 and s in l[letter]:
                    l[letter].remove(s)
                    if len(l[letter]) == 1:
                        again = True
    return l

def decryptWithoutKey(mes):
    letterList = makeLetterList()
    letterAndSpace = Symbols + " "
    processed = ""
    for letter in mes:
        if letter.upper() in letterAndSpace:
            processed += letter.upper()
    processedList = processed.split()
    for word in processedList:
        candidateList = makeLetterList()
        wordPattern = MWP.getWordPattern(word)
        patterns = wordPatterns.allPatterns
        if wordPattern not in patterns:
             continue    # The word is not in dictionary
        for candidate in patterns[wordPattern]:
            for i in range(len(word)):  
                if candidate[i] not in candidateList[word[i]]:          
                    candidateList[word[i]].append(candidate[i])
        letterList = intersectList(letterList, candidateList)
    return cleanseList(letterList)

if __name__ == "__main__":
    main() 


