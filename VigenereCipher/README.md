# Vigenere Cipher
_The longer the message is, the better the program can decrypt._

## Files Descryption
- VigenereCipher.py:
```
# the main file containing:

- encryptWithoutKey()
- encryptWithKey()
- decryptWithKey()
- decryptWhenKeyIsAWord()
When the key is a word, we can use brute force to loop over all the possible words in "dictionary.txt"

- decryptWhenKeyIsRandom():
When the key is random letters, we have to analyze the pattern of ciphertext with:
(1) Kasiski examination: find the possible key length
(2) Find possible letters in the key
(3) Iterate over all possible keys and compare the result to words in "dictionary.txt"

- findFactors()
- findSequence():
identify patterns of the ciphertext

- kasiskiExamination()
- getSubkeyLetter()
- attemptWithKeyLength()
```

- frequencyAnalysis.py:
```
- getLetterCount()
count how many times a letter appears in the message

- getFrequencyOrder():
sort the appearance frequency of each letter, and concatenate letters into a string

- matchScore():
compare the similarity between appearance frequency string to "ETAOINSHRDLCUMWFGYPBVKJXQZ"
```
- isEnglish.py
```
- loadDictionary():
input dictionary.txt
- wordsCount()
- removeNonLetter()
- isEnglish()
```
- dictionary.txt ([Source](https://nostarch.com/crackingcodes))


## How to Run
```properties
1. py VigenereCipher.py
2. enter your message
3. enter "encrypt" or "decrypt"

4.
if "encrypt": enter your own key (1) or make it random (2)
    if (1): enter the key (length <= 8, as this is time-consuming)
    if (2): enter the random seed
    
if "decrypt": choose decryption with key (1) or without key (2)
    if (1): enter the key
```
