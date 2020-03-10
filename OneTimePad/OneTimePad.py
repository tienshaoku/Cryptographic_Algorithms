#!/usr/bin/python

import secrets

Symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    message = input("This is One Time Pad.\nEnter your message here: ")
    pad, processed = encrypt(message)
    print("The pad for encryption: " + pad)
    print("The encrypted message: " + processed)

def encrypt(mes):
    processed = ""
    for i in mes:
        if i.upper() in Symbols:
            processed += i.upper() 
    length = len(processed)
    pad = ""
    for i in range(length):
        pad += Symbols[secrets.randbelow(26)]
    encrypted = ""
    for i in range(length):
        index_mes = Symbols.find(processed[i].upper())
        index_pad = Symbols.find(pad[i])
        encrypted += Symbols[(index_mes + index_pad) % 26]    
    return pad, encrypted

if __name__ == "__main__":
    main() 


