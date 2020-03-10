# Public Key Cryptography

## Files Descryption
- publicKeyCryptography.py:
```
# the main file containing:

- getBlockFromText():
transform message into blocks for encryption

- getTextFromBlock():
transform blocks back to message

- readKeyFile()
- encrypt()
- decrypt()
```
- Euclidean.py
```
- gcd()
- modInverse():
find the mod inverse of input
```
- primeNumber.py
```
- trialDivision():
see if a number is prime with brute force

- sieveOfEratosthenes():
get all prime numbers in the range

- rabinMiller():
a faster while not perfectly accurate method to test if a number is prime

- isPrime():
combined with rabinMiller()

- generateLargePrime():
use brute force to find large prime numbers; time-consuming
```
- generateKeyPair.py
```
- generateKeyPair():
generate the public key (n,e) and private key (n,d)
```


## How to Run
```properties
1. py generateKeyPair.py
1. py publicKeyCryptography.py
2. enter your message
3. enter "encrypt" or "decrypt"
```
