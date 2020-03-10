#!/usr/bin/python

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a     

def modInverse(x, m):
    if gcd(x, m) != 1:
        return None
    a, b, c = m, 0, 1
    d, e, f = 0, 0, 0
    while x != 0:
        d = a // x
        e = a % x
        f = b - d * c
        a = x
        b = c
        c = f
        x = e
    return b % m
