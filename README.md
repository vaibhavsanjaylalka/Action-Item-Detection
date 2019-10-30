# Action-Item-Detection
classify sentences to actionable sentence and non-actionable sentence

Actionable item => A sentence which asks someone to do something
example: "Please create an assignment and forward it by EOD"

=================================================

First download the raw data from the link: https://www.kaggle.com/wcukierski/enron-email-dataset
and put that in the enrol-email-dataset Folder --> 1.2GB size and name emails.csv

================================================

Then, extract_main_content.py once you run this file: 
  - Input:  emails.csv
  It will extract 5000 email and extract the main content from the raw email and save 5000 email-main-content in the files with the name: content1.csv , content2.csv ........ content104.csv.

Sample content1.csv and content2.csv is present in the Folder eron-email-dataset

==========================================

When you run: actionable_sentences.py- 
  - Input : content1.csv  (one csv file) or any onr of the content(1 to 104).csv file
  It first extract the sentences from the main content and then outputs if the sentence is actionable or not for all the 5000 email-main-content in the content1.csv file.
  - This is the file where rule-based model is present for classsfying the sentence as actionable or not
  ======================================
  
  When you run: content2sentence.py
    Input: content1.csv Output: sentence1.csv
  Convert the content to sentence and label is by applying out rule-based model.
  
  =====================================
  
  train-data Folder
  Sample Train Dataset having two column - sentence and label (actionable or non-actionable)
  
=============================
  
  When you run: ml-classification-model.py
   Input: sentence1.csv and sentence2.csv , test.csv
   Output: accuracy, sensitivity and specificity on the test.csv dataset
   This module trains the labeled dataset from the sentence*.csv file and randomly picks the 4000 (actionable) and 5000 (non-actionable) sentences and after training 
   predicts the test.csv dataset
   Results:
   Accuracy on the given test dataset:
RandomForestClassifier accuracy = 63.9167309175%
('sensitivity: ', 0.599388379204893)
('specificity: ', 0.6796267496111975)
MultinomialNB accuracy = 63.2228218967%
('sensitivity: ', 0.6926605504587156)
('specificity: ', 0.5707620528771384)

============================================  
  
