#!/usr/bin/python

import pyperclip, sys, random
import Euclidean as Eu
import isEnglish as iE

# len(Symbols) == 67
Symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789 !?.;:"
Symbols_len = len(Symbols)

def main():
    message = input("This is Affine Cipher.\nEnter your message here: ")
    mode = input("Enter encrypt or decrypt: ")
    processed = ""
    while mode != "encrypt" and mode != "decrypt":
        print("False input, please enter 'encrypt' or 'decrypt'")
        mode = input("Enter encrypt or decrypt: ")
    if mode == "encrypt":
        key = int(input("Enter a random seed here: "))
        random.seed(key)
        k1, k2 = generateKeyPair()
        print("The two encryption keys are: %s and %s" %(k1, k2) )
        processed = encrypt(message, k1, k2)
    else:
        mode = int(input("Decrypt with key (1) or without key (2)? Please Enter 1 or 2: "))
        while mode != 1 and mode != 2:
            print("False input, please enter 1 or 2")
            mode = int(input("Decrypt with key (1) or without key (2)? Please Enter 1 or 2: "))
        if mode == 1:
            k1 = int(input("Enter the first key: "))
            k2 = int(input("Enter the second key: "))
            processed = decryptWithKey(message, k1, k2)    
        else:
            processed, k1, k2 = decryptWithoutKey(message)
            print("Keys for encryption: %s and %s" %(k1, k2) )
    pyperclip.copy(processed)
    print(processed)


def generateKeyPair():
    k1, k2 = 1, 0
    while k1 == 1 or k2 == 0: 
        rand = random.randint(1,10000)
        k1 = int(rand / Symbols_len ) % Symbols_len
        k2 = int(rand % Symbols_len )
    return k1, k2

def encrypt(mes, k1, k2):
    encrypted = ""
    for symbol in mes:
        if symbol in Symbols:
            index = Symbols.find(symbol)
            encrypted += Symbols[(index * k1 + k2 ) % Symbols_len]
        else:
            encrypted += symbol
    return encrypted

def decryptWithKey(mes, k1, k2):
    decrypted = ""
    for symbol in mes:
        if symbol in Symbols:
            index = Symbols.find(symbol)
            if k1 == 0:
                decrypted += Symbols[(index - k2) % Symbols_len]
            else: 
                decrypted += Symbols[ ( (index - k2) % Symbols_len * Eu.modInverse(k1, Symbols_len) ) % Symbols_len]
        else:
            decrypted += symbol
    return decrypted

def decryptWithoutKey(mes):
    decrypted = ""
    result = []
    highest = [0, 0, 0]
    for i in range(Symbols_len):        
        for j in range(Symbols_len):        
            if i == 1 or j == 0:
                continue
            decrypted = decryptWithKey(mes, i, j)
            isEnglish, percentage = iE.isEnglish(decrypted)
            if isEnglish:
                result.append([i, j, percentage])
            decrypted = ""
    for k in range(len(result)):
        if result[k][2] > highest[2]:
            highest = result[k]
    return decryptWithKey(mes, highest[0], highest[1]), highest[0], highest[1]

if __name__ == "__main__":
    main() 


