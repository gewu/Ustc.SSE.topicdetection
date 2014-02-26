# -*- coding:utf-8 -*- 
from nltk.corpus import stopwords
import nltk

porter = nltk.PorterStemmer()
pattern = r'''(?x)([A-Z]\.)+|\w+(-\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;"'?():-_`]'''

def data_read(datalist):
    eassylist = []
    for text in datalist:
        file = open (text)
        str = ""
    
        while 1:
            lines = file.readlines(10000000)
            if not lines:
                break
            for i in range (len(lines) - 1):
                if len(lines[i]) > 10:
                    str += lines[i]
                    if len(lines[i+1]) < 10:
                        eassylist.append(str.strip())
                        str = ""
    return eassylist


def tokenprocess(Strtext,flag = 1):  # flag 0 means do not use porter.stem
   
    f = open(Strtext)
    raw = f.read().strip()
    
    stop_words = stopwords.words('english')
    text1 = map(lambda strr:strr[:-1].lower() if strr[-1] == '.' else strr.lower(),nltk.regexp_tokenize(raw,pattern))
    #text1 = map(lambda strr:strr[:-1].lower() if strr[-1] == '.' else strr.lower(),nl.word_tokenize(raw))
    if (flag == 1):
        text1_filter = [porter.stem(word) for word in text1 if word not in stop_words and word.find("'") == -1 and len(word) > 1]
    else :
        text1_filter = [word for word in text1 if word not in stop_words and word.find("'") == -1 and len(word) > 1]
  
    return text1_filter




'''tokenprocess test'''

'''text = tokenprocess("text")
text_2 = tokenprocess("text_2")
them  = tokenprocess("them")
print text
print text_2
print them
'''

#f = open("tt/text_2")
#raw = f.read()
#pattern = r'''(?x)([A-Z]\.)+|\w+(-\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;"'?():-_`]'''
#print nltk.regexp_tokenize(raw, pattern)

        
#datalist = ["data/20101111_clea.txt","data/20101111_clean.txt","data/USTC2011Jan.txt"]
#print len(data_read(datalist))

            

   
        

        
    

        