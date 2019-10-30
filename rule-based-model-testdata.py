# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:40:02 2019

@author: Vaibhav
"""

import pandas as pd
from actionable_sentences import is_actionable
import nltk
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import numpy as np

print("Process the cleaned content")
sentence_df = pd.read_csv('./enron-email-dataset/test.csv', names='m')
list_sen = sentence_df['m'].tolist()
sentence = []
label = []
for i in range(len(list_sen)): 
    if list_sen[i].find('|') == -1: 
        continue
    sentence.append(list_sen[i].split("|")[0])
    label.append(list_sen[i].split("|")[1])
del sentence[0]
del label[0]

pred = []
for i in range(len(sentence)): 
    wordsList = nltk.word_tokenize(sentence[i])
    postag_sen = nltk.pos_tag(wordsList)
    pred.append(is_actionable(postag_sen))

for i in range(len(sentence)): 
    if label[i].find('True')!=-1: 
        label[i] = 1
    else: 
        label[i] = 0
          
    if str(pred[i]).find('True')!=-1: 
        pred[i] = 1
    else: 
        pred[i] = 0

label = np.asarray(label, dtype=float)
pred = np.asarray(pred, dtype=float)
print (accuracy_score(label, pred))
tn, fp, fn, tp = confusion_matrix(label ,pred).ravel()
print("sensitivity: " , float(tp) / float(tp+fn)) 
print("specificity: " , float(tn) / float(tn+fp))