#!/usr/bin/python

import random, difflib

def main():
    seed = input("This is the verification of Columnar Transposition Cipher.\nEnter a random seed: ")
    random.seed(int(seed))

    message = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?. "
    message *= random.randint(1, 30)
    message = list(message)
    random.shuffle(message)
    message = ''.join(message)
    key = int(random.randint(2, len(message)) / 2)

    print("The random message to be encrypted: \n" + message)
    print("The random key: \n" + str(key))
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)
    print("\nEncrypted message: \n" + encrypted)
    print("Decrypted message: \n" + decrypted)
    print("\nResult of verification: " + str(message == decrypted))


def encrypt(mes, key):
    encrypted = ""
    length = len(mes)
    # key = # of columns
    row = int(length / key)
    for i in range(key):
        for j in range(row + 1):
            position = j * key + i
            if position < length:
                encrypted += mes[position]
            else:
                continue
    return encrypted
    
def decrypt(mes, key):
    length = len(mes)
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

    return decrypted
    
if __name__ == "__main__":
    main() 
