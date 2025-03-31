#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:11:26 2022

@author: htethtethtun
"""


import pandas as pd
import csv

def marketIndexCalculation():
    # market index 
    data = pd.read_csv('original stock data/^GSPC.csv')
    
    # calculate price feature vectors first and then calculate returns feature vectors and write csv file
    with open('relative returns data/^GSPC.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "X-260", "X-180", "X-150", "X-120", "X-100", "X-80", "X-60", "X-40", "X-20", "X-15", "X-10", "X-5", "X-1", "X0", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "Y10"])
        nOfIterations = len(data)-260   # -260 of last one year 
        for y in range (0,nOfIterations-10): # -10 refer to Y10
            price = [data['Date'][260+y], data['Close'][(260+y)-260], data['Close'][(260+y)-180], data['Close'][(260+y)-150], data['Close'][(260+y)-120], data['Close'][(260+y)-100], data['Close'][(260+y)-80], data['Close'][(260+y)-60], data['Close'][(260+y)-40], data['Close'][(260+y)-20], data['Close'][(260+y)-15], data['Close'][(260+y)-10], data['Close'][(260+y)-5], data['Close'][(260+y)-1], data['Close'][(260+y)-0], data['Close'][(260+y)+1], data['Close'][(260+y)+2], data['Close'][(260+y)+3], data['Close'][(260+y)+4], data['Close'][(260+y)+5], data['Close'][(260+y)+6], data['Close'][(260+y)+7], data['Close'][(260+y)+8], data['Close'][(260+y)+9], data['Close'][(260+y)+10]]
            returns = [price[0], (price[14]-price[1])/price[1]*100, (price[14]-price[2])/price[2]*100, (price[14]-price[3])/price[3]*100, (price[14]-price[4])/price[4]*100, (price[14]-price[5])/price[5]*100, (price[14]-price[6])/price[6]*100, (price[14]-price[7])/price[7]*100, (price[14]-price[8])/price[8]*100, (price[14]-price[9])/price[9]*100, (price[14]-price[10])/price[10]*100, (price[14]-price[11])/price[11]*100, (price[14]-price[12])/price[12]*100, (price[14]-price[13])/price[13]*100, (price[14]-price[14])/price[14]*100, (price[15]-price[14])/price[14]*100, (price[16]-price[14])/price[14]*100, (price[17]-price[14])/price[14]*100, (price[18]-price[14])/price[14]*100, (price[19]-price[14])/price[14]*100, (price[20]-price[14])/price[14]*100, (price[21]-price[14])/price[14]*100, (price[22]-price[14])/price[14]*100, (price[23]-price[14])/price[14]*100, (price[24]-price[14])/price[14]*100]
            writer.writerow([returns[0], returns[1], returns[2], returns[3], returns[4], returns[5], returns[6], returns[7], returns[8], returns[9], returns[10], returns[11], returns[12], returns[13], returns[14], returns[15], returns[16], returns[17], returns[18], returns[19], returns[20], returns[21], returns[22], returns[23], returns[24]])
          


def relativeReturnCalculation():
    # read returns file of market index 
    marketIndex = pd.read_csv('relative returns data/^GSPC.csv')


    # read the companies' name file to get a list of stocks
    stocks = pd.read_csv('companies.csv')

    for x in range(0,len(stocks)-1):   # -1 means to remove market index returns (not to repeat again)
        data = pd.read_csv('original stock data/'+stocks["Company Name"][x]+".csv")
    
        # create prices, returns and relative returns feature vectors
        with open('relative returns data/'+stocks["Company Name"][x]+".csv", 'a') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "X-260", "X-180", "X-150", "X-120", "X-100", "X-80", "X-60", "X-40", "X-20", "X-15", "X-10", "X-5", "X-1", "X0", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "Y10", "Class (0.3%)", "Class (0.5%)", "Class (1%)", "Class (1.5%)", "Class (1.8%)", "Class (2%)", "Class (2.2%)", "Class (2.5%)", "Class (2.8%)", "Class (3%)", "Class (3.5%)", "Class (4%)", "Class (4.5%)", "Class (5%)", "Class (5.5%)", "Class (6%)", "Class (6.5%)", "Class (7%)", "Class (7.5%)", "Class (8%)", "Class (8.5%)", "Class (9%)", "Class (9.5%)", "Class (10%)"])
            nOfIterations = len(data)-260
            for y in range (0,nOfIterations-10):
            
                price = [data['Date'][260+y], data['Close'][(260+y)-260], data['Close'][(260+y)-180], data['Close'][(260+y)-150], data['Close'][(260+y)-120], data['Close'][(260+y)-100], data['Close'][(260+y)-80], data['Close'][(260+y)-60], data['Close'][(260+y)-40], data['Close'][(260+y)-20], data['Close'][(260+y)-15], data['Close'][(260+y)-10], data['Close'][(260+y)-5], data['Close'][(260+y)-1], data['Close'][(260+y)-0], data['Close'][(260+y)+1], data['Close'][(260+y)+2], data['Close'][(260+y)+3], data['Close'][(260+y)+4], data['Close'][(260+y)+5], data['Close'][(260+y)+6], data['Close'][(260+y)+7], data['Close'][(260+y)+8], data['Close'][(260+y)+9], data['Close'][(260+y)+10]]
                returns = [price[0], (price[14]-price[1])/price[1]*100, (price[14]-price[2])/price[2]*100, (price[14]-price[3])/price[3]*100, (price[14]-price[4])/price[4]*100, (price[14]-price[5])/price[5]*100, (price[14]-price[6])/price[6]*100, (price[14]-price[7])/price[7]*100, (price[14]-price[8])/price[8]*100, (price[14]-price[9])/price[9]*100, (price[14]-price[10])/price[10]*100, (price[14]-price[11])/price[11]*100, (price[14]-price[12])/price[12]*100, (price[14]-price[13])/price[13]*100, (price[14]-price[14])/price[14]*100, (price[15]-price[14])/price[14]*100, (price[16]-price[14])/price[14]*100, (price[17]-price[14])/price[14]*100, (price[18]-price[14])/price[14]*100, (price[19]-price[14])/price[14]*100, (price[20]-price[14])/price[14]*100, (price[21]-price[14])/price[14]*100, (price[22]-price[14])/price[14]*100, (price[23]-price[14])/price[14]*100, (price[24]-price[14])/price[14]*100]
                # calculate returns - marketIndexReturns = relative returns 
                relativeReturns = returns[0], returns[1]-marketIndex['X-260'][y], returns[2]-marketIndex['X-180'][y], returns[3]-marketIndex['X-150'][y], returns[4]-marketIndex['X-120'][y], returns[5]-marketIndex['X-100'][y], returns[6]-marketIndex['X-80'][y], returns[7]-marketIndex['X-60'][y], returns[8]-marketIndex['X-40'][y], returns[9]-marketIndex['X-20'][y], returns[10]-marketIndex['X-15'][y], returns[11]-marketIndex['X-10'][y], returns[12]-marketIndex['X-5'][y], returns[13]-marketIndex['X-1'][y], returns[14]-marketIndex['X0'][y], returns[15]-marketIndex['Y1'][y], returns[16]-marketIndex['Y2'][y], returns[17]-marketIndex['Y3'][y], returns[18]-marketIndex['Y4'][y], returns[19]-marketIndex['Y5'][y], returns[20]-marketIndex['Y6'][y], returns[21]-marketIndex['Y7'][y], returns[22]-marketIndex['Y8'][y], returns[23]-marketIndex['Y9'][y], returns[24]-marketIndex['Y10'][y]
            
                
                writer.writerow([relativeReturns[0], relativeReturns[1], relativeReturns[2], relativeReturns[3], relativeReturns[4], relativeReturns[5], relativeReturns[6], relativeReturns[7], relativeReturns[8], relativeReturns[9], relativeReturns[10], relativeReturns[11], relativeReturns[12], relativeReturns[13], relativeReturns[14], relativeReturns[15], relativeReturns[16], relativeReturns[17], relativeReturns[18], relativeReturns[19], relativeReturns[20], relativeReturns[21], relativeReturns[22], relativeReturns[23], relativeReturns[24], labelP3, labelP5, label1, labelOneP5, labelOneP8, label2, labelTwoP2, labelTwoP5, labelTwoP8, label3, labelThreeP5, label4, labelFourP5, label5, labelFiveP5, label6, labelSixP5, label7, labelSevenP5, label8, labelEightP5, label9, labelNineP5, label10])
          

                
                

marketIndexCalculation()
relativeReturnCalculation()

