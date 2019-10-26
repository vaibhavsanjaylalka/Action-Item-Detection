# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:21:05 2019

@author: Vaibhav
"""

import pandas as pd

""" Global Variables """

email_lines = ['Message-ID', 'Date', 'From', 'To', 'Subject', 'Cc', 'Mime-Version',\
               'Content-Type', 'Content-Transfer-Encoding', 'Bcc', 'X-From', 'X-To',\
               'X-cc', 'X-bcc', 'X-Folder', 'X-Origin', 'X-FileName', 'Content']

""" Helper functions """

def getContent(message):
    '''
    This function outputs the main-content of the email 
    '''
    message = message.split('\n')
    index = message.index('')
    message = message[: index] + ['Content: ' + ' '.join(message[index+1:])]
    message = [message[i].split(': ', 1) for i in range(len(message))]
    i = 0
    while i < len(message):
        if len(message[i]) != 2:
            message[i-1][1] += message[i][0]
            message.pop(i)
        elif message[i][0] not in email_lines:
            message[i-1][1] += ( message[i][0] + ': ' + message[i][1])
            message.pop(i)
        else:
            i += 1
    main_msg = message[len(message)-1][1]
    return main_msg


""" Code Starts Here """

input_data_file = './enron-email-dataset/emails.csv'
c_size = 5000 #chunk size 
count = 1
for emails in pd.read_csv(input_data_file, chunksize = c_size):
    print("Processing File no: ", count)
    list_main_msg = []
    emails = emails.reset_index(drop=True)
    for i in range(len(emails)): 
        curr_email = emails['message'][i]
        cleaned_mail = getContent(curr_email)
        list_main_msg.append(cleaned_mail)
        
    print("No. of emails processed: ",len(list_main_msg))
    final_df = pd.DataFrame(list_main_msg)
    final_df.to_csv("./enron-email-dataset/content"+str(count)+".csv", encoding='utf-8', index=False, header=False)
    print("Created "+"./enron-email-dataset/content"+str(count)+".csv")
    count = count + 1
    if count == 3: 
        break