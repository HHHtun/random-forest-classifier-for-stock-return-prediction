#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:18:57 2022

@author: htethtethtun
"""

import pandas as pd
import csv
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score


def results(stocks):
    with open('naiveContrarianResults.csv', 'a') as file:
    
        writer = csv.writer(file)
        writer.writerow(["Stock", "F1 score", "Accuracy score"])


    for x in range(0,len(stocks)-1):   # -1 means to remove market index returns (not to repeat again)
        data = pd.read_csv('naive contrarian data/'+stocks["Company Name"][x]+".csv")
        print (stocks["Company Name"][x]+".csv")  # to know which stock
    
        with open('naiveContrarianResults.csv', 'a') as file:
            writer = csv.writer(file)
            predictions = data['Naive Contrarian'][253:len(data)-1] # take only testing data of sliding window by one-month
            realisations = data['RealClass (2%)'][253:len(data)-1]
        
        
            print (len(predictions))
            print (len(realisations))
            writer.writerow([stocks["Company Name"][x],f1_score(realisations, predictions, pos_label=1, average='binary')*100.0, accuracy_score(realisations, predictions)*100.0])



# read the companies name file to get a list of stocks
stocks = pd.read_csv('companies.csv')

results(stocks)
