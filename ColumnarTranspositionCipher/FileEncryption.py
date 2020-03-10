#!/usr/bin/python

import time, os, random
import ColumnarTranspositionCipher as CTV

def main():
    inputFile = input("Please enter the input file name: ")
    while not os.path.exists(inputFile):
        inputFile = input("The file does not exist. Please enter again: ")
    inputFileList = inputFile.split('.')
    outputFileList = ["Processed"]
    for string in inputFileList:
        outputFileList.append(string)
    outputFile = '.'.join(outputFileList)
    if os.path.exists(outputFile):
        print("The processed file %s already exists. (C)Continue or (Q)quit?" %(outputFile))
        response = input(' > ')
        if not response.lower() == 'c':
            sys.exit()

    mode = input("Please enter encrypt or decrypt: ")
    while mode != "encrypt" and mode != "decrypt":
        mode = input("Please enter encrypt or decrypt: ")
    if mode == "encrypt":
        seed = input("Please enter a random seed: ")
        while True:
            try:
                seed = int(seed)
                break
            except:
                seed = input("Please enter a random seed: ")
        random.seed(seed)

    fileObj = open(inputFile)
    content = fileObj.read()
    fileObj.close()
    print("%sing..." %(mode.title())) 

    startTime = time.time()
    if mode == "encrypt":
        key = int(random.randint(2, int(len(content) / 2) ) )
        print("The key for encryption: " + str(key) + "; \nRemember not to let others know ;)")
        processed = CTV.encrypt(content, key)
    else:
        processed = CTV.decrypt(content)

    totalTime = round(time.time() - startTime, 2)
    print("%stion time: %s seconds" %(mode, totalTime) )

    outputFileObj = open(outputFile, 'w')
    if mode == "decrypt":
        for item in processed:
            outputFileObj.write(item + '\n')
    else:
        outputFileObj.write(processed)
    outputFileObj.close()
    print("Done %stion." %(mode) )

if __name__ == "__main__":
    main()
