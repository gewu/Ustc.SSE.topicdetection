# -*- coding:utf-8 -*- 
from __future__ import  division
from data_process_new import *
from nltk.corpus import wordnet as wn
import re
import math

def val_tf (rawtext):
    corpus = corpus_data()   # our test corpus 
    result = nltk.defaultdict(int)
    list_word = set(rawtext)
    
    for word in list_word:
        result[word] = rawtext.count(word)  
    
    doc_num = len(corpus)
    
    for word in rawtext:
        count = 1                    #count should not be the zero
        for cor in corpus:
            if cor.find(word) != -1:
                count = count + 1
            
    tmp = result[word]
    result[word] = (1+math.log10(tmp)) * math.log10(doc_num/count) 
    
    return result

def val_cos(rawtext1,dict_text1,rawtext2,dict_text2):
    allwords = set(rawtext1+rawtext2)
   
    value1 = value2 = value3 = 0
    for word in allwords:
        value1 = value1 + dict_text1[word] * dict_text2[word]
        value2 = value2 + math.pow(dict_text1[word],2)
        value3 = value3 + math.pow(dict_text2[word],2)
    
    value = value1 / (math.sqrt(value2) * math.sqrt(value3))    # the cos value
    return value
        
def extend_them(rawtext):
    
    result_word = []
    for word in rawtext:
        for synset in wn.synsets(word): 
            for sim_word in synset.lemma_names:
                result_word.extend(re.split('[_-]',sim_word))
            
            for similar in synset.similar_tos():
                for sim_word in similar.lemma_names:
                    result_word.extend(re.split('[_-]',sim_word))

    result_word = rawtext + list(set(result_word))             # this place i allow the key word repeat to impove the importance
    return result_word


text1 = "text"
them_fake = "text_2"
them = "them"

rawtext1 = tokenprocess(text1)                  # read and preprocess the data
rawthem_fake = tokenprocess(them_fake)
rawthem = tokenprocess(them)

extenthem_fake = extend_them(rawthem_fake)
extenthem = extend_them(rawthem)

print rawthem_fake
print extenthem_fake

dict_text1 = val_tf(rawtext1)
dict_themfake = val_tf(extenthem_fake)
dict_them = val_tf(extenthem)

print val_cos(rawtext1,dict_text1,rawthem_fake,dict_themfake)
print val_cos(rawtext1,dict_text1,rawthem,dict_them)
    
    

        
        