def readData():
    data = ['There is a big car','I buy a car','They buy the new car']
    dat=[]
    print(data[0])
    
    for i in range(len(data)):
        start = ['<s>']
        dat=dat+ start
        for word in data[i].split():
            dat.append(word)
        stop = ['</s>']
        dat = dat + stop
    print(dat)
    return dat

def createBigram(data):
   listOfBigrams = []
   bigramCounts = {}
   unigramCounts = {}

   for i in range(len(data)-1):
      if i < len(data) - 1:

         listOfBigrams.append((data[i], data[i + 1]))

         if (data[i], data[i+1]) in bigramCounts:
            bigramCounts[(data[i], data[i + 1])] += 1
         else:
            bigramCounts[(data[i], data[i + 1])] = 1

      if data[i] in unigramCounts:
         unigramCounts[data[i]] += 1
      else:
         unigramCounts[data[i]] = 1
   return listOfBigrams, unigramCounts, bigramCounts

def calcBigramProb(listOfBigrams, unigramCounts, bigramCounts):
    listOfProb = {}
    for bigram in listOfBigrams:
        word1 = bigram[0]
        listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word1))
    return listOfProb
    
if __name__ == '__main__':
    data = readData()
    listOfBigrams, unigramCounts, bigramCounts = createBigram(data)

    print("\n All the possible Bigrams are ")
    print(listOfBigrams)

    print("\n Bigrams along with their frequency ")
    print(bigramCounts)

    print("\n Unigrams along with their frequency ")
    print(unigramCounts)

    bigramProb = calcBigramProb(listOfBigrams, unigramCounts, bigramCounts)

    print("\n Bigrams along with their probability ")
    print(bigramProb)
    inputList="I buy a car"
    splt1 = []
    start = ['<s>']
    splt1 = splt1 +start
    splt2 = []
    splt2=inputList.split()
    splt = splt1 +splt2
    stop = ['</s>']
    splt = splt + stop
    outputProb1 = 1
    bilist=[]
    bigrm=[]

    for i in range(len(splt) - 1):
        if i < len(splt) - 1:

            bilist.append((splt[i], splt[i + 1]))

    print("\n The bigrams in given sentence are ")
    print(bilist)
    for i in range(len(bilist)):
        if bilist[i] in bigramProb:

            outputProb1 *= bigramProb[bilist[i]]
        else:

            outputProb1 *= 0
    print('\n' + 'Probablility of sentence \"This is my cat\" = ' + str(outputProb1))