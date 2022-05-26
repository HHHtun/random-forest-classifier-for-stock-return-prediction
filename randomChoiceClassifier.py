#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:19:56 2022

@author: htethtethtun
"""

import pandas as pd
import csv
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

 
# read the companies name file to get a list of stocks
stocks = pd.read_csv('list of stocks.csv')


# read random class from randomClass.csv
randomChoice = pd.read_csv('100 shuffle list.csv')

shuffle =randomChoice.columns[0]


def randomChoiceClassifier():
    for number in range (0,100):
        f1ScoreList =[]
        accuracyScoreList = []
        for x in range(0,len(stocks)):
            data = pd.read_csv('relative returns data/'+stocks["Company Name"][x]+".csv")
            print (stocks["Company Name"][x]+".csv")  # to know which stock
            shuffleColumn = randomChoice.columns[number]
            predictions = randomChoice[shuffleColumn][253:len(data)-1] # take only testing data of sliding window by one-month
            realisations = data['Class (2%)'][253:len(data)-1]
            
            f1Score = f1_score(realisations, predictions, pos_label=1, average='binary')*100.0
            f1ScoreList.append(f1Score)
            
            accuracyScore = accuracy_score(realisations, predictions)*100.0
            accuracyScoreList.append(accuracyScore)
            
        
    
        stocks['F1 score',number] = f1ScoreList
        stocks['Accuracy score',number] = accuracyScoreList
        
        stocks.to_csv('100randomChoiceClassifierResults.csv', index=False)
        
        
     
        
def averageResults():
    results = pd.read_csv('100randomChoiceClassifierResults.csv')
    with open('randomChoiceResults.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "F1 score", "Accuracy score"])
        
    for x in range(0,len(results)):   # for 494 stocks 
        F1Score = 0 
        Accuracy = 0
        f = 1     # f1 score columns 1,3,5,7......
        a = 2     #  f1 score columns 2,4,6,8,.......
    
        for y in range (1,101):       # for 100 times of F1 scores and accuracy scores 
            F1Score = F1Score + results.values[x][f]
            Accuracy = Accuracy + results.values[x][a]
            f = f+2
            a = a+2
        
    
        with open('randomChoiceResults.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([results["Company Name"][x],F1Score /100, Accuracy /100])

        
        
#randomChoiceClassifier()
averageResults()