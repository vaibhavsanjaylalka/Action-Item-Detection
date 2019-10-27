# Action-Item-Detection
classify sentences to actionable sentence and non-actionable sentence

Actionable item => A sentence which asks someone to do something
example: "Please create an assignment and forward it by EOD"


 

First download the raw data from the link: https://www.kaggle.com/wcukierski/enron-email-dataset
and put that in the enrol-email-dataset Folder --> 1.2GB size and name emails.csv

Then, extract_main_content.py once you run this file: 
  - Input:  emails.csv
  It will extract 5000 email and extract the main content from the raw email and save 5000 email-main-content in the files with the name: content1.csv , content2.csv ........ content104.csv.

Sample content1.csv and content2.csv is present in the Folder eron-email-dataset

When you run: actionable_sentences.py- 
  - Input : content1.csv  (one csv file) or any onr of the content(1 to 104).csv file
  It first extract the sentences from the main content and then outputs if the sentence is actionable or not for all the 5000 email-main-content in the content1.csv file.
  - This is the file where rule-based model is present for classsfying the sentence as actionable or not
