# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 01:31:26 2019

@author: Vaibhav
"""

import nltk
from nltk import RegexpParser
from nltk.tree import Tree
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd


def is_actionable(tagged_sent):
    '''
    Sample given a sentence is_actionable function
    tell if the sentence is actionable or not
    ---------------------------------------------
    sentence = "Bill could you send me the file"
    wordsList = nltk.word_tokenize(sentence)
    psen = nltk.pos_tag(wordsList)
    print(psen)
    print(is_actionable(psen))
    '''
    # if the sentence is not a question...
    if tagged_sent[-1][0] != "?":
        # catches simple imperatives, e.g. "Open the pod bay doors, HAL!"
        if tagged_sent[0][1] == "VB" or tagged_sent[0][1] == "MD":
            return True
        # catches imperative sentences starting with words like 'please', 'you',...
        # E.g. "Dave, stop.", "Just take a stress pill and think things over."
        else:
            chunk = get_chunks(tagged_sent)
            # check if the first chunk of the sentence is a VB-Phrase
            if type(chunk[0]) is Tree and chunk[0].label() == "VB-Phrase":
                return True

    # Questions can be imperatives too, let's check if this one is
    else:
        # check if sentence contains the word 'please'
        print("It is a question")
        pls = len([w for w in tagged_sent if w[0].lower() == "please"]) > 0
        # catches requests disguised as questions
        # e.g. "Open the doors, HAL, please?"
        if pls or (tagged_sent[0][1] == "VB" or tagged_sent[0][1] == "MD"):
            return True

        chunk = get_chunks(tagged_sent)
        # catches imperatives ending with a Question tag
        # and starting with a verb in base form, e.g. "Stop it, will you?"
        if type(chunk[-1]) is Tree and (chunk[-1].label() == "Q-Tag"):
            if (chunk[0][1] == "VB" or
                (type(chunk[0]) is Tree and chunk[0].label() == "VB-Phrase")):
                return True

    return False


''' Helper function to find Verb-Phrase '''

def get_chunks(tagged_sent):
    chunkgram = r"""VB-Phrase: {<DT><,>*<VB>}
                    VB-Phrase: {<RB><VB>}
                    VB-Phrase: {<UH><,>*<VB>}
                    VB-Phrase: {<UH><,><VBP>}
                    VB-Phrase: {<PRP><VB|VBP>}
                    VB-Phrase: {<NN.?>+<,>*<VB|MD>}
                    Q-Tag: {<,><MD><RB>*<PRP><.>*}"""  #Q-tag is not generic and hardcoded
    chunkparser = RegexpParser(chunkgram)
    return chunkparser.parse(tagged_sent)


''' Starting the main function '''

print("Start processing the cleaned content")
emails_df = pd.read_csv('./enron-email-dataset/content1.csv', names='m')

for index in range(len(emails_df)): 
    sentence_list = nltk.sent_tokenize(emails_df['m'][index])
    for i in range(len(sentence_list)): 
        wordsList = nltk.word_tokenize(sentence_list[i])
        postag_sen = nltk.pos_tag(wordsList)
        print(sentence_list[i])
        print("Is above sentence Actionable:" + str(is_actionable(postag_sen)))
   

