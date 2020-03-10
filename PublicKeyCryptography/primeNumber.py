#!/usr/bin/python

import math, random

def trialDivision(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num) ) + 1):
        if num % i == 0:
            return False
    return True    

def sieveOfEratosthenes(num):
    sieve = [True] * (num + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.sqrt(num) ) + 1):
        for j in range(2, int(num/2) + 1):
            if i * j <= num:
                sieve[i * j] = False
    sieveList = []
    for i in range(num):
        if sieve[i]:
            sieveList.append(i)
    return sieveList

def rabinMiller(num):
    if num % 2 == 0 or num < 2:
        return False    # Doesn't work on even numbers
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        s /= 2
        t += 1
    for trial in range(5):    # Test primality for 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, int(s), num)
        if v != 1:
            i = 0
            while v != num - 1:
                if i == t - 1:
                    return False
                else:
                    i += 1
                    v = (v ** 2) % num
    return True

def isPrime(num):
    smallPrime = sieveOfEratosthenes(100)
    if num < 2:
        return False
    for prime in smallPrime:
        if num % prime == 0:
            return False
    return rabinMiller(num)

def generateLargePrime(keysize = 1024):
    while True:
        num = random.randrange(2 ** (keysize-1), 2 ** keysize)
        if isPrime(num):
            print(num)
            return num

