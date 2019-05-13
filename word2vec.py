
import numpy as np
import pickle
from collections import Counter


def processDataset(filename):
    openedFile = open(filename,'rb')
    allLines = openedFile.readlines()
    myStr = ""
    for line in allLines:
        myStr+=str(line)
    finalDict=Counter(myStr.split())
    return myStr,finalDict



fullCorpus,datasetDictionary = processDataset('conversationData.txt')
wordList=list(datasetDictionary.keys())

#print(wordList)
with open("wordList.txt","wb") as fp:
    pickle.dump(wordList,fp)


