#!/usr/bin/python

Frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getLetterCount(mes):
    dic = {}
    for i in range(65, 91):
        dic[chr(i)] = 0
    for letter in mes.upper():
        if letter in Letters:
            dic[letter] += 1
    return dic

def getFrequencyOrder(mes):
    letterCount = getLetterCount(mes)
    countToLetter = {}
    for letter in Letters:
        if letterCount[letter] not in countToLetter:
            countToLetter[letterCount[letter]] = [letter]
        else:
            countToLetter[letterCount[letter]].append(letter)
    # Use reverse sequence to avoid miscalculation of scores
    # For example: I, N, V, K have the same frequency.
    # While I and N are generally more frequently used, 
    # placing them in reverse order can avoid miscalculation(since I and N are also more frontly place in "Frequency"), 
    # as these four have the same frequency.
    for count in countToLetter:
        countToLetter[count].sort(key = Frequency.find, reverse = True)
        countToLetter[count] = ''.join(countToLetter[count])
    pairs = list(countToLetter.items())
    pairs.sort(key = lambda x: x[0], reverse = True)
    order = []
    for pair in pairs:
        order.append(pair[1])
    return "".join(order)

def matchScore(mes):
    order = getFrequencyOrder(mes)
    score = 0
    for letter in order[:6]:
        if letter in Frequency[:6]:
            score += 1
    for letter in order[20:]:
        if letter in Frequency[20:]:
            score += 1
    return score
    
