start = ['<s>']
stop = ['</s>']

def readData():
    s = ['There is a big car', 'I buy a car', 'They buy the new car']  #training data

    a = (map(lambda x: x.lower(), s))     # Convert words to lowercase letters
    data = list(a)
    dataList = []

    for i in range(len(data)):
        dataList = dataList + start
        for word in data[i].split():
            dataList.append(word)
        dataList = dataList + stop

    return dataList


def createBigram(data):
    bigramList = []                # List of bigrams
    bigramCount = {}               # count of bigrams in training data
    unigramCount = {}              # count of each unigram in trainig data

    for j in range(len(data) - 1):
        if j < len(data) - 1:

            bigramList.append((data[j], data[j + 1]))

            if (data[j], data[j + 1]) in bigramCount:
                bigramCount[(data[j], data[j + 1])] += 1
            else:
                bigramCount[(data[j], data[j + 1])] = 1

        if data[j] in unigramCount:
            unigramCount[data[j]] += 1
        else:
            unigramCount[data[j]] = 1
    return bigramList, unigramCount, bigramCount


def calcBigramProb(listOfBigrams, unigramCounts, bigramCounts):       # Calculatae bigram probability of each pair
    listOfProb = {}
    for bigram in listOfBigrams:
        word1 = bigram[0]
        listOfProb[bigram] = (bigramCounts.get(bigram)) / (unigramCounts.get(word1))
    return listOfProb



if __name__ == '__main__':
    data = readData()
    listOfBigrams, unigramCounts, bigramCounts = createBigram(data)

    inputList = input("Enter Your sentence Which you want to predict \n")

    bigramProb = calcBigramProb(listOfBigrams, unigramCounts, bigramCounts)

    print("\n Bigrams along with their probability ")
    print(bigramProb)

    inputListSplit = []
    inputListSplit += start
    splt = inputList.split()
    spltSimpleLetter = []

    for m in range(len(splt)):      # Convert words to lowercase letters
        k = splt[m].lower()
        spltSimpleLetter.append(k)
    inputListSplit = inputListSplit + spltSimpleLetter + stop
    outputProb1 = 1
    bilist = []
    bigrm = []

    for k in range(len(inputListSplit) - 1):
        if k < len(inputListSplit) - 1:
            bilist.append((inputListSplit[k], inputListSplit[k + 1]))

    print("\n The bigrams in given sentence are ")
    print(bilist)
    for k in range(len(bilist)):
        if bilist[k] in bigramProb:

            outputProb1 *= bigramProb[bilist[k]]
        else:

            outputProb1 *= 0

    print("\n All the possible Bigrams are ")
    print(listOfBigrams)

    print("\n Bigrams along with their frequency ")
    print(bigramCounts)

    print("\n Unigrams along with their frequency ")
    print(unigramCounts)

    print('\n' + f'Probablility of sentence {inputList} = ' + str(outputProb1))
