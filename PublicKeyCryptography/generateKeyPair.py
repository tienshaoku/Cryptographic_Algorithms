#!/usr/bin/python

import random, sys, os
import Euclidean as Eu
import primeNumber as pN

def main():
    publicKey, privateKey = generateKeyPair(512)
    output = open("publicKey.txt", "w")
    output.write(publicKey[0], "\n", publicKey[1])
    output.close()
    output = open("privateKey.txt", "w")
    output.write(privateKey[0], "\n", privateKey[1])
    output.close()

def generateKeyPair(keySize):
    p, q = 0, 0
    while p == q:
        p = pN.generateLargePrime(keySize)
        q = pN.generateLargePrime(keySize)
    n = p * q
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize)
        if Eu.gcd(e, (p - 1) * (q - 1)) == 1:
            break
    d = Eu.modInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    print("Public Key = ", publicKey)
    print("Private Key = ", privateKey)
    return publicKey, privateKey

if __name__ == "__main__":
    main()
