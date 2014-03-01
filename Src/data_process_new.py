# -*- coding:utf-8 -*- 
''' the file's last line should be blank'''
import os
from nltk.corpus import stopwords
import nltk

def corpus_data():
    dir = "/home/gewu/workspace/Ustc.SE.topic_detection/cordata/"
    listfile =  os.listdir(dir)
    
    eassylist = []   #list of the document
    eassystr = ""    # eassy in the document
    for filepath in listfile:
        filepath = dir + filepath
        file = open(filepath)
        
        for line in file:
            line = line.strip()
            if (len(line) == 0 and len(eassystr) > 5):
                eassylist.append(eassystr)
                eassystr = ""
            elif (line.find('<') == -1):
                eassystr = eassystr + line
    
    return eassylist


def tokenprocess(Strtext): 
   
    f = open(Strtext)
    raw = f.read().strip()
    stop_words = stopwords.words('english')
    
    pattern = r'''(?x)([A-Z]\.)+|\w+(-\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;"'?():-_`]'''
    text1 = map(lambda word:word.lower(),nltk.regexp_tokenize(raw,pattern))
    text1_filter = [word for word in text1 if len(word) > 1 and word.find("'") == -1 and word not in stop_words]
    
  
    return text1_filter




#eassylist = corpus_data()
#print eassylist[-1]

#stop_words = stopwords.words('english')
#print stop_words


    
    
    
    