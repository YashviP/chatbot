import pandas as pd
import numpy as np
import yaml
import re

f=open('greetings.yml','r')
d=yaml.load(f)


def clean_msg(message):
    #Remove Newlines
    cleanedMsg=message.replace('\n', ' ').lower()

    #Deal with some weird tokens
    cleanedMsg=cleanedMsg.replace("\xc2\xa0",'')

    #Remove punctuations
    cleanedMsg = re.sub('([.,!?])', '', cleanedMsg)

    #remove multiple spaces
    cleanedMsg = re.sub(' +', ' ', cleanedMsg)

    return cleanedMsg

mydict={}

for i in range(0,len(d)):

    msg=clean_msg(str(d[i][0]))
    resp=clean_msg(str(d[i][1]))
    print(d[i][1])
    mydict[msg.rstrip()]=resp.rstrip()




conversationFile = open('conversationData.txt', 'w')
np.save('conversationDictionary.npy',mydict)
for key,value in mydict.items():
    if(not key or not value):
        continue
    #conversationFile.write('msg : '+ key+'\n'+ 'reply : ' + value + '\n')
    conversationFile.write(key + " " + value + " ")


