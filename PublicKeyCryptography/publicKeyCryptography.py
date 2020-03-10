#!/usr/bin/python

import sys, math, pyperclip

Symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

def main():
    message = input("This is Public Key Encryption.\nEnter your message here: ")
    mode = input("Enter encrypt or decrypt: ")
    processed = ""
    while mode != "encrypt" and mode != "decrypt":
        print("False input, please enter 'encrypt' or 'decrypt'")
        mode = input("Enter encrypt or decrypt: ")
    if mode == "encrypt":
        processed = encrypt(message, "publicKey.txt")
    else:
        print("Decryption supports only predetermined file currently.")
        processed = decrypt("encrypted.txt", "privateKey.txt")
    pyperclip.copy(processed)
    print(processed)

def getBlockFromText(mes, size):
    for letter in mes:
        if letter not in Symbols:
            print("Message contains unsupported letters.")
            sys.exit()
    blockInts = []
    for i in range(0, len(mes), size):
        blockInt = 0
        for j in range(i, min(i + size, len(mes))):
            blockInt += Symbols.index(mes[j]) * (len(Symbols) ** (j % size))
        blockInts.append(blockInt)
    return blockInts

def getTextFromBlock(blockInts, messageLength, size):
    message = []
    for blockInt in blockInts:
        letters = [] 
        for i in range(size - 1, -1, -1):
            if len(message) + i < messageLength:
                index = blockInt // len(Symbols) ** i 
                blockInt = blockInt % (len(Symbols) ** i) 
            letters.insert(0, Symbols[index])
        message.extend(letters)
    return "".join(message)      

def readKeyFile(fileName):
    objec = open(fileName)
    content = objec.read()
    objec.close()
    n, EorD = content.split("\n")
    return n, EorD

def encrypt(message, publicKeyFile):
    n, e = readKeyFile(publicKeyFile)
    blockSize = int(math.log(2 ** 512, len(Symbols) ) )
    print("blockSize is: ", blockSize)
    encrypted = []
    blockInts = getBlockFromText(message, blockSize)    
    for blockInt in blockInts:
        encrypted.append(pow(blockInt, e, n))
    encryptedContent = ",".join(encrypted)
 
    objec = open("encrypted.txt", "w")
    objec.write("%s_%s_%s" %(len(message), blockSize, encryptedContent))
    objec.close()
    return encryptedContent

def decrypt(messageFile, privateKeyFile):
    n, d = readKeyFile(privateKeyFile)
    objec = open("encrypted.txt")
    content = objec.read()
    messageLength, blocksize, encryptedContent = content.split("_")
    encryptedMessage = []
    for encrypted in encryptedContent.split(","):
        encryptedMessage.append(int(encrypted))
    blockInts = []
    for encrypted in encryptedMessage:
        blockInts.append(pow(encrypted, d, n))
    return getTextFromBlock(blockInts, int(messageLength), int(blockSize))

if __name__ == "__main__":
    main()


