#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 20:13:27 2022

@author: htethtethtun
"""

import pandas as pd
from pandas import datetime
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import csv

def parser(z):
    return datetime.strptime(z, '%Y-%m-%d')

with open('RFCResults.csv', 'a') as csvfile:  # print results file
    writer = csv.writer(csvfile)
    writer.writerow(["stock", "Accuracy score", "F1 score"])
        
        
# read the companies name file to get a list of stocks
stocks = pd.read_csv('companies.csv')

def RFC():
    for r in range(0,len(stocks)-1):   # -1 means to remove market index returns (not to repeat again)
        data = pd.read_csv('relative returns data/'+stocks["Company Name"][r]+".csv", header=0, parse_dates=[0], index_col=0, date_parser=parser)
    
        x= data[['X-260','X-180','X-150', 'X-120','X-100','X-80','X-60','X-40','X-20','X-15','X-10','X-5','X-1']] # predictor variables
        y= data['Class (2%)']    # target variable
    
        # one year training and one month testing
        i=0
        j=253

        predictions =[]
        realisations =[]
    
        iterations = len(data)-252   # no of iterations 
    
        for u in range(0,iterations):
            x_train, y_train = x.iloc[i:j], y.iloc[i:j]
            x_test, y_test = x.iloc[j:j+21], y.iloc[j:j+21]
        
    
            if len(x_test)< 21:
                print ("break")
                break
            rfc = RandomForestClassifier(n_estimators=1000,max_depth=5, max_features= 13, random_state=0)
            rfc.fit(x_train, y_train)
    
            y_pred = rfc.predict(x_test)
    
            for a in range(0,len(y_pred)):
                predictions.append(y_pred[a])
                realisations.append(y_test[a])
        
            i=i+21
            j=j+21
    
        print ("realisations",len(realisations))
        print ("predictions", len(predictions))
    
        with open('RFCResults.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([stocks["Company Name"][r], accuracy_score(realisations, predictions)*100.0, f1_score(realisations, predictions, pos_label=1,average='binary')*100.0])


    
    
    
RFC()