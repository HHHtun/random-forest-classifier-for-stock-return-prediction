#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 23:12:07 2022

@author: htethtethtun
"""

from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import pandas as pd
import csv


def marketIndexCalculation():
    # read the market index file
    data = pd.read_csv('original stock data/'+'^GSPC.csv')


    # create prices, returns and relative returns feature vectors
    with open('naive classifier data/'+'index.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "X-11", "X-10", "X-9", "X-8", "X-7", "X-6", "X-5", "X-4", "X-3", "X-2", "X-1", "X0", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "Y10", "Class (4%)", "Class (3%)", "Class (2%)", "Class (1%)"])
        nOfIterations = len(data)-260
        for y in range (0,nOfIterations-10):
            price = [data['Close'][(260+y)-11], data['Close'][(260+y)-10], data['Close'][(260+y)-9], data['Close'][(260+y)-8], data['Close'][(260+y)-7], data['Close'][(260+y)-6], data['Close'][(260+y)-5], data['Close'][(260+y)-4], data['Close'][(260+y)-3], data['Close'][(260+y)-2], data['Close'][(260+y)-1], data['Close'][(260+y)-0], data['Close'][(260+y)+1], data['Close'][(260+y)+2], data['Close'][(260+y)+3], data['Close'][(260+y)+4], data['Close'][(260+y)+5], data['Close'][(260+y)+6], data['Close'][(260+y)+7], data['Close'][(260+y)+8], data['Close'][(260+y)+9], data['Close'][(260+y)+10]]
          
            returns = [(price[0]-price[0])/price[0]*100, (price[1]-price[0])/price[0]*100, (price[2]-price[0])/price[0]*100, (price[3]-price[0])/price[0]*100, (price[4]-price[0])/price[0]*100, (price[5]-price[0])/price[0]*100, (price[6]-price[0])/price[0]*100, (price[7]-price[0])/price[0]*100, (price[8]-price[0])/price[0]*100, (price[9]-price[0])/price[0]*100, (price[10]-price[0])/price[0]*100, (price[11]-price[11])/price[11]*100, (price[12]-price[11])/price[11]*100, (price[13]-price[11])/price[11]*100, (price[14]-price[11])/price[11]*100, (price[15]-price[11])/price[11]*100, (price[16]-price[11])/price[11]*100, (price[17]-price[11])/price[11]*100, (price[18]-price[11])/price[11]*100, (price[19]-price[11])/price[11]*100, (price[20]-price[11])/price[11]*100, (price[21]-price[11])/price[11]*100]
            writer.writerow([data['Date'][(260+y)], returns[0], returns[1], returns[2], returns[3], returns[4], returns[5], returns[6], returns[7], returns[8], returns[9], returns[10], returns[11], returns[12], returns[13], returns[14], returns[15], returns[16], returns[17], returns[18], returns[19], returns[20], returns[21]])
        





def naiveClassifier(stocks):
    # read returns of market index file 
    marketIndex = pd.read_csv('naive classifier data/'+'index.csv')


    # read the companies name file to get a list of stocks
    #stocks = pd.read_csv('companies.csv')
    
    
    for x in range(0,len(stocks)-1):   # -1 means to remove market index returns (not to repeat again)
        data = pd.read_csv('original stock data/'+stocks["Company Name"][x]+".csv")
        print ('original stock data/'+stocks["Company Name"][x]+".csv")  # to know which stock
        # create prices, returns and relative returns feature vectors
        with open('naive classifier data/'+stocks["Company Name"][x]+".csv", 'a') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "X-11", "X-10", "X-9", "X-8", "X-7", "X-6", "X-5", "X-4", "X-3", "X-2", "X-1", "X0", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "Y10", "Class (2%)", "RealClass (2%)"])
            nOfIterations = len(data)-260
            for y in range (0,nOfIterations-10):
                price = [data['Close'][(260+y)-11], data['Close'][(260+y)-10], data['Close'][(260+y)-9], data['Close'][(260+y)-8], data['Close'][(260+y)-7], data['Close'][(260+y)-6], data['Close'][(260+y)-5], data['Close'][(260+y)-4], data['Close'][(260+y)-3], data['Close'][(260+y)-2], data['Close'][(260+y)-1], data['Close'][(260+y)-0], data['Close'][(260+y)+1], data['Close'][(260+y)+2], data['Close'][(260+y)+3], data['Close'][(260+y)+4], data['Close'][(260+y)+5], data['Close'][(260+y)+6], data['Close'][(260+y)+7], data['Close'][(260+y)+8], data['Close'][(260+y)+9], data['Close'][(260+y)+10]]
                returns = [(price[0]-price[0])/price[0]*100, (price[1]-price[0])/price[0]*100, (price[2]-price[0])/price[0]*100, (price[3]-price[0])/price[0]*100, (price[4]-price[0])/price[0]*100, (price[5]-price[0])/price[0]*100, (price[6]-price[0])/price[0]*100, (price[7]-price[0])/price[0]*100, (price[8]-price[0])/price[0]*100, (price[9]-price[0])/price[0]*100, (price[10]-price[0])/price[0]*100, (price[11]-price[11])/price[11]*100, (price[12]-price[11])/price[11]*100, (price[13]-price[11])/price[11]*100, (price[14]-price[11])/price[11]*100, (price[15]-price[11])/price[11]*100, (price[16]-price[11])/price[11]*100, (price[17]-price[11])/price[11]*100, (price[18]-price[11])/price[11]*100, (price[19]-price[11])/price[11]*100, (price[20]-price[11])/price[11]*100, (price[21]-price[11])/price[11]*100]
        
                # calculate returns - indexReturns and write
                relativeReturns = [returns[0]-marketIndex['X-11'][y], returns[1]-marketIndex['X-10'][y], returns[2]-marketIndex['X-9'][y], returns[3]-marketIndex['X-8'][y], returns[4]-marketIndex['X-7'][y], returns[5]-marketIndex['X-6'][y], returns[6]-marketIndex['X-5'][y], returns[7]-marketIndex['X-4'][y], returns[8]-marketIndex['X-3'][y], returns[9]-marketIndex['X-2'][y], returns[10]-marketIndex['X-1'][y], returns[11]-marketIndex['X0'][y], returns[12]-marketIndex['Y1'][y], returns[13]-marketIndex['Y2'][y], returns[14]-marketIndex['Y3'][y], returns[15]-marketIndex['Y4'][y], returns[16]-marketIndex['Y5'][y], returns[17]-marketIndex['Y6'][y], returns[18]-marketIndex['Y7'][y], returns[19]-marketIndex['Y8'][y], returns[20]-marketIndex['Y9'][y], returns[21]-marketIndex['Y10'][y]]
                
                # predictions 
                if (relativeReturns[1] >= 2.00000 or relativeReturns[2] >= 2.00000 or relativeReturns[3] >= 2.00000 or relativeReturns[4] >= 2.00000 or relativeReturns[5] >= 2.00000 or relativeReturns[6] >= 2.00000 or relativeReturns[7] >= 2.00000 or relativeReturns[8] >= 2.00000 or relativeReturns[9] >= 2.00000 or relativeReturns[10] >= 2.00000):
                    label2=1
                
                else:
                    label2=0
                
            
                # realisations 
                if (relativeReturns[12] >= 2.00000 or relativeReturns[13] >= 2.00000 or relativeReturns[14] >= 2.00000 or relativeReturns[15] >= 2.00000 or relativeReturns[16] >= 2.00000 or relativeReturns[17] >= 2.00000 or relativeReturns[18] >= 2.00000 or relativeReturns[19] >= 2.00000 or relativeReturns[20] >= 2.00000 or relativeReturns[21] >= 2.00000):
                    Rlabel2=1
                
                else:
                    Rlabel2=0
                
           
                writer.writerow([data['Date'][(260+y)], relativeReturns[0], relativeReturns[1], relativeReturns[2], relativeReturns[3], relativeReturns[4], relativeReturns[5], relativeReturns[6], relativeReturns[7], relativeReturns[8], relativeReturns[9], relativeReturns[10], relativeReturns[11], relativeReturns[12], relativeReturns[13], relativeReturns[14], relativeReturns[15], relativeReturns[16], relativeReturns[17], relativeReturns[18], relativeReturns[19], relativeReturns[20], relativeReturns[21], label2, Rlabel2])
          
                
           
def results(stocks):
    with open('naiveClassifierResults.csv', 'a') as file:
    
        writer = csv.writer(file)
        writer.writerow(["Stock", "F1 score", "Accuracy score"])


    for x in range(0,len(stocks)-1):   # -1 means to remove market index returns (not to repeat again)
        data = pd.read_csv('naive classifier data/'+stocks["Company Name"][x]+".csv")
        print (stocks["Company Name"][x]+".csv")  # to know which stock
    
        with open('naiveClassifierResults.csv', 'a') as file:
            writer = csv.writer(file)
            predictions = data['Class (2%)'][253:len(data)-1] # take only testing data of sliding window by one-month
            realisations = data['RealClass (2%)'][253:len(data)-1]
        
        
            print (len(predictions))
            print (len(realisations))
            writer.writerow([stocks["Company Name"][x],f1_score(realisations, predictions, pos_label=1, average='binary')*100.0, accuracy_score(realisations, predictions)*100.0])



# read the companies name file to get a list of stocks
stocks = pd.read_csv('companies.csv')

marketIndexCalculation()
naiveClassifier(stocks)
results(stocks)



