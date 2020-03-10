#!/usr/bin/python

Symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !?,.'

def main():
    message = input("This is Caesar Cipher.\nEnter your message here: ")
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
    for i in range(len(mes)):
        position = Symbols.find(mes[i])
        new_position = (position + key) % len(Symbols)
        encrypted += Symbols[new_position]
    return encrypted

def decrypt(mes):
    for i in range(len(Symbols)):
        decrypted = ""
        for j in range(len(mes)):
            position = Symbols.find(mes[j])
            new_position = (position - i) % len(Symbols)
            decrypted += Symbols[new_position]
        print("Key == " + str(i) + " : " + decrypted)    
    print("\nThat's it! Hope you have find your answer ;)")


if __name__ == "__main__":
    main() 
