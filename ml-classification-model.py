# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:57:05 2019

@author: Vaibhav
"""

import pandas as pd
from sklearn import preprocessing
Encode = preprocessing.LabelEncoder()
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB

''' Preparing the train dataset '''

input1 = pd.read_csv('./train-data/'+'sentence1'+'.csv')
input2 = pd.read_csv('./train-data/'+'sentence2'+'.csv')
df = pd.concat([input1, input2], ignore_index=True)
input_1 =  df[df['label']==1]
input_0 =  df[df['label']==0]
input_1 = input_1.sample(n=5000)
input_0 = input_0.sample(n=7000)
df = pd.concat([input_0, input_1], ignore_index=True)
all_sentences = df['sentences'].tolist()
all_label = df['label'].tolist()
print("*** Done with preparing train dataset ***")


'''Preparing the test dataset '''

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
for i in range(len(sentence)): 
    if label[i].find('True')!=-1: 
        label[i] = 1
    else: 
        label[i] = 0
print("*** Done with preparing test dataset ***")


''' Applying the classfication algorithms '''

classifiers = [
    SVC(kernel="rbf", C=100),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
    MultinomialNB()]

for clf in classifiers:
    name = clf.__class__.__name__
    text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()),
                  ('clf', clf),])
    text_clf.fit(all_sentences, all_label)
    predicted = text_clf.predict(sentence)
    acc = metrics.accuracy_score(label,predicted)
    tn, fp, fn, tp = metrics.confusion_matrix(label ,predicted).ravel()
    print (name+' accuracy = '+str(acc*100)+'%')
    print("sensitivity: " , float(tp) / float(tp+fn))
    print("specificity: " , float(tn) / float(tn+fp))
    
