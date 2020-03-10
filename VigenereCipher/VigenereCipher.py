#!/usr/bin/python

import pyperclip, sys, random, itertools
import isEnglish as iE
import frequencyAnalysis as fA

Symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MaxKeyLength = 16

def main():
    message = input("This is Vigenere Cipher.\nEnter your message here: ")
    mode = input("Enter encrypt or decrypt: ")
    processed = ""
    while mode != "encrypt" and mode != "decrypt":
        print("False input, please enter 'encrypt' or 'decrypt'")
        mode = input("Enter encrypt or decrypt: ")
    if mode == "encrypt":
        submode = int(input("Enter your own key (1) or make it random (2) ? "))
        if submode == 1:
            key = input("Enter your key (<= 8, as this is time-consuming): ").upper()
            processed = encryptWithKey(message, key)
        else:
            seed = int(input("Enter a random seed here: "))
            length = int(input("Enter the length of key: "))
            random.seed(seed)
            processed, key = encryptWithoutKey(message, length)
            print("The encryption key is: ", key)
    else:
        mode = int(input("Decrypt with key (1) or without key (2)? Please Enter 1 or 2: "))
        while mode != 1 and mode != 2:
            print("False input, please enter 1 or 2")
            mode = int(input("Decrypt with key (1) or without key (2)? Please Enter 1 or 2: "))
        if mode == 1:
            key = input("Enter the encryption key: ")
            processed = decryptWithKey(message, key)    
        else:
            key, processed = decryptWhenKeyIsAWord(message)    
            print("The encryption key is: ", key)
            again = input("Is this the right answer? If no, enter N: ")
            if again == "N":
                processed, key = decryptWhenKeyIsRandom(message)
                print("The encryption key is: ", key)
    pyperclip.copy(processed)
    print(processed)

def encryptWithoutKey(mes, length):
    encrypted = ""
    key = ""
    for i in range(length):
        key += Symbols[random.randint(0,26)]
    count = 0
    for letter in mes:
        if letter.upper() in Symbols:
            index = Symbols.index(letter.upper())
            encrypted += Symbols[(index + Symbols.index(key[count]) ) % 26]   
            count = (count + 1) % length
        else:
            encrypted += letter 
    return encrypted, key

def encryptWithKey(mes, key):
    encrypted = ""
    count = 0
    for letter in mes:
        if letter.upper() in Symbols:
            index = Symbols.index(letter.upper())
            encrypted += Symbols[(index + Symbols.index(key[count]) ) % 26]   
            count = (count + 1) % len(key)
        else:
            encrypted += letter 
    return encrypted

def decryptWithKey(mes, key):
    decrypted = ""
    count = 0
    for letter in mes:
        if letter.upper() in Symbols:
            index = Symbols.index(letter.upper())
            decrypted += Symbols[(index - Symbols.index(key[count]) ) % 26]   
            count = (count + 1) % len(key)
        else:
            decrypted += letter 
    return decrypted

def decryptWhenKeyIsAWord(mes):
    possibleAnswers = {}
    for key in iE.englishWords:
        decrypted= decryptWithKey(mes, key)
        result, percentage = iE.isEnglish(decrypted)
        if result:
            possibleAnswers[key] = [decrypted, percentage]
    answers = list(possibleAnswers.items())
#    print(answers)
    answers.sort(key = lambda x: x[1][1], reverse = True)
    return answers[0][0], answers[0][1][0]

def findSequence(mes):
    possibleSeq = {}
    for seqLength in range(3, 6):
        for seqStart in range(len(mes) - seqLength):
            sequence = mes[seqStart : seqStart + seqLength]
            for i in range(seqStart + seqLength, len(mes) - seqLength):
                if mes[i : i + seqLength] == sequence:
                    if mes[i : i + seqLength] not in possibleSeq:
                        possibleSeq[sequence] = []
                    possibleSeq[sequence].append(i - seqStart)
    return possibleSeq

def findFactors(num):
    if num < 2:
        return []
    factors = []
    for i in range(2, MaxKeyLength + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def kasiskiExamination(mes):
    sequences = findSequence(mes)
    seqFactors = {}
    for seq in sequences:
        seqFactors[seq] = []
        for spacing in sequences[seq]:
            seqFactors[seq].extend(findFactors(spacing))
    factorCount = {}
    for seq in seqFactors:
        for count in seqFactors[seq]:
            if count not in factorCount:
                factorCount[count] = 0
            factorCount[count] += 1
    countList = list(factorCount.items())
    countList.sort(key = lambda x: x[1], reverse = True)
    possibleKeyLength = []
    for length in countList:
        if length[0] < 9:
            possibleKeyLength.append(length[0])
    print(possibleKeyLength)
    return possibleKeyLength

def getSubkeyLetter(nth, keyLength, mes):
    letters = ""
    while nth < len(mes):
        letters += mes[nth]
        nth += keyLength
    return letters

def attemptWithKeyLength(mes, keyLength):
    freqScores = []
    for nth in range(keyLength):
        nthLetters = getSubkeyLetter(nth, keyLength, mes)
        scores = []
        for subkey in Symbols:
            decrypted = decryptWithKey(nthLetters, subkey) 
            matchTuple = (subkey, fA.matchScore(decrypted) )
            scores.append(matchTuple)
        scores.sort(key = lambda x: x[1], reverse = True)
        freqScores.append(scores[:4])    # four of the highest scores
 
    rightDecrypted, rightKey, accuracy = "", "", 0
    for indexes in itertools.product(range(4), repeat = keyLength):
        possibleKey =""
        for i in range(keyLength):
            possibleKey += freqScores[i][indexes[i]][0]
        decrypted = decryptWithKey(mes, possibleKey)
        result, percentage = iE.isEnglish(decrypted)
        if result and percentage > accuracy:
            rightKey = possibleKey
            accuracy = percentage
            rightDecrypted = decrypted
    if accuracy != 0:
        return rightDecrypted, rightKey, accuracy
    else:
        return None, None, None

def decryptWhenKeyIsRandom(mes):
    possibleKeyLength = kasiskiExamination(mes)
    rightDecrypted, rightKey, accuracy = "", "", 0
    for keyLength in possibleKeyLength:
        print("Attempting with key length = ", keyLength)
        decrypted, possibleKey, percentage = attemptWithKeyLength(mes, keyLength)
        print(percentage)
        if decrypted != None and percentage > accuracy:
            rightKey = possibleKey
            accuracy = percentage
            rightDecrypted = decrypted
    if rightDecrypted == None:
        rightDecrypted, rightKey, accuracy = "", "", 0
        for keyLength in range(1, MaxKeyLength):
            if KeyLength not in possibleKeyLength:
                rightDecrypted, rightKey, accuracy = "", "", 0
                decrypted, possibleKey, percentage = attemptWithKeyLength(mes, keyLength)
                if decrypted != None and percentage > accuracy:
                    rightKey = possibleKey
                    accuracy = percentage
                    rightDecrypted = decrypted
    return rightDecrypted, rightKey




if __name__ == "__main__":
    main() 


