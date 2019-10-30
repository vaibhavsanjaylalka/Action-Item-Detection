# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 20:19:17 2019

@author: Vaibhav
"""

from actionable_sentences import is_actionable
import nltk
import pandas as pd

infile = "content3"
oufile = "sentence3"
print("Start processing the cleaned content")
emails_df = pd.read_csv('./enron-email-dataset/'+infile+'.csv', names='m')
all_sentences = []
all_label = []
for index in range(len(emails_df)): 
    sentence_list = nltk.sent_tokenize(emails_df['m'][index])
    for i in range(len(sentence_list)): 
        wordsList = nltk.word_tokenize(sentence_list[i])
        postag_sen = nltk.pos_tag(wordsList)
        all_sentences.append(sentence_list[i])
        all_label.append(str(is_actionable(postag_sen)))
    
print("no of sentences: ", len(all_sentences))
for i in range(len(all_sentences)): 
    if str(all_label[i]).find('True')!=-1: 
        all_label[i] = 1
    else: 
        all_label[i] = 0

df = pd.DataFrame({'sentences': all_sentences, 'label': all_label})
df.to_csv('./train-data/'+ oufile+'.csv', encoding='utf-8', index=False)
