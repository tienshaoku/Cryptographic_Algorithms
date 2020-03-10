#!/usr/bin/python

import sys
sys.path.append("EnglishWordsDetection/")
import isEnglish as iE

def main():
    message = input("This is Columnar Transposition Cipher.\nEnter your message here: ")
    mode = input("Enter encrypt or decrypt: ")
    while mode != "encrypt" and mode != "decrypt":
        print("False input, please enter 'encrypt' or 'decrypt'")
        mode = input("Enter encrypt or decrypt: ")
    if mode == "encrypt":
        key = int(input("Enter your key here: "))
        print("\nEncrypted result: " + encrypt(message, key))
    else:
        decrypt(message)

def encrypt(mes, key):
    encrypted = ""
    length = len(mes)
    # key = # of columns
    key = key % length
    row = int(length / key)
    for i in range(key):
        for j in range(row + 1):
            position = j * key + i
            if position < length:
                encrypted += mes[position]
            else:
                continue
    return encrypted
    
def decrypt(mes):
    length = len(mes)
    array = []
    for key in range(1, length + 1):
        decrypted = ""
        remainder = length % key
        row = int(length / key) + 1
        for i in range(row - 1):
            for j in range(remainder + 1):
                position = j * row + i
                decrypted += mes[position]
            for k in range(1, key - remainder):
                position = k * (row - 1) + remainder * row + i
                decrypted += mes[position]
        for l in range(remainder):
            position = l * row + row - 1
            decrypted += mes[position]
        if iE.isEnglish(decrypted):
            message = "A possible solution is key = " + str(key) + ", and the decrypted message is as follows:\n" + decrypted + "\n"
            print(message) 
            array.append(message)
    return array
    
if __name__ == "__main__":
    main() 
