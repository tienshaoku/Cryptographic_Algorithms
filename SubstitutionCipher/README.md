# Substitution Cipher
_The longer the message is, the better the program can decrypt._

## Files Descryption
- SubstitutionCipher.py:
```
# the main file containing:

- encrypt()
- decryptWithKey()
- makeLetterList():
make an empty dictionary

- intersectList():
compare two lists and keep the intersected possibilities

- cleanseList():
if a ciphertext is decrypted, its corresponding plaintext should be removed from others' lists of possibilities

- decryptWithoutKey()
```

- makeWordPattern.py:
```
- getWordPattern()
```
- wordPatterns.py
```
Patterns of each English word, produced by makeWordPattern.py.
For example, pattern of "dog" is: 0.1.2, as all three letters are different.
```
- dictionary.txt ([Source](https://nostarch.com/crackingcodes))


## How to Run
```properties
1. py SubstitutionCipher.py
2. enter your message
3. enter "encrypt" or "decrypt"

4.
if "encrypt": enter a random seed
    
if "decrypt": choose decryption with key (1) or without key (2)
    if (1): enter the key
```
