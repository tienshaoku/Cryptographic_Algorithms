import pprint

def getWordPattern(word):
    word = word.upper()
    count = 0
    letters = {}
    pattern = []
    
    for letter in word:
        if letter not in letters:
            letters[letter] = str(count)
            count += 1
        pattern.append(letters[letter])
    return '.'.join(pattern)

def main():
    allPatterns = {}
    dictionary = open("dictionary.txt")
    wordList = dictionary.read().split("\n")
    dictionary.close()

    for word in wordList:
        pattern = getWordPattern(word)
        if pattern in allPatterns:
            allPatterns[pattern].append(word)
        else:
            allPatterns[pattern] = [word]
    print(allPatterns)   
    output = open("wordPatterns.py", "w")
    output.write("allPatterns = ")
    output.write(pprint.pformat(allPatterns))
    output.close()

if __name__ == "__main__":
    main()
