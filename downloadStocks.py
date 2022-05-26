#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 17:36:06 2021

@author: htethtethtun
"""


import pandas as pd
import yfinance as yf


# read the companies' name file to get a list of stocks
stocks = pd.read_csv('companies.csv')

# download a list of stocks from Yahoo Finance and save the files in csv under "output files" folder 
for x in range(0,len(stocks)):
    data = yf.download(stocks["Company Name"][x], start="2017-01-01", end="2022-01-01")
    data.to_csv('original stock data/'+stocks["Company Name"][x]+".csv")
    
    








