# -*- coding:utf-8 -*- 
from __future__ import  division
import nltk as nl
import math
import data_process 

porter = nl.PorterStemmer()
pattern = r'''(?x)([A-Z]\.)+|\w+(-\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;"'?():-_`]'''

def freqDist (list_word,rawtext):
    
    result = {}
    for word in list_word:
        countword = rawtext.count(word)
        length = len(rawtext)
        freq = countword / length
        
        result[word] = freq
    return result
    


def If_idf(freqd,word2,corpus):
    
    docnum = len(corpus)
    dict = nl.defaultdict(int)
    for word in word2:
        count = 0                  #count will not be zhe zero
        for doc in corpus:
            if word in doc:
                count = count + 1
        
        dict[word] =  freqd[word] * math.log10(docnum/count)
    
    return dict


     
def final_process(text,eassy):

    
    wordt = data_process.tokenprocess(text)
    listword = set(wordt)

    resultword = freqDist(listword,wordt)
    res = If_idf(resultword,listword,eassy)
    
    return res,wordt


def valueall(test1raw,test1,test2raw,test2):
    testall = set(test1raw + test2raw)
    test_1 = []
    test_2 = []
    for word in testall:
        test_1.append(test1[word])
        test_2.append(test2[word])
        
    value = value2 = value3 = 0
    for i in range(len(test_2)):
        value = value + test_1[i]*test_2[i]
        value2 = value2 + math.pow(test_1[i],2)
        value3 = value3 + math.pow(test_2[i],2)
  
    valu = value / (math.sqrt(value2) * math.sqrt(value3))
    return valu



datalist1 = []                          #read all the data
path = "/home/gewu/workspace/Ustc.SE.topic_detection"
testdata = ["/data/20101111_clea.txt","/data/20101111_clean.txt","/data/USTC2011Jan.txt"]
for wordtemp in testdata:
    datalist1.append(path + wordtemp)

doclist = data_process.data_read(datalist1)

#doclist = []
#for doc in eassy:
#    doclist.append(data_process.tokenprocess(doc,0))


test1,rawtest1 = final_process("text",doclist)
test2,rawtest2 = final_process("text_2",doclist)
test3,rawtest3 = final_process("them",doclist)

print valueall(rawtest1,test1,rawtest2,test2)
print valueall(rawtest2,test2,rawtest3,test3)
print valueall(rawtest3,test3,rawtest1,test1)

#print test1
#print test2
#print valueall(test1,test3)
#print valueall(test2,test3)









