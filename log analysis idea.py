from unicodedata import name
from bs4 import BeautifulSoup
import requests
from csv import writer
import os
import wget
import pandas as pd
import numpy as np
from tabula import read_pdf
from tabulate import tabulate

#Commented my idea 
# Like with web scraping i done with unegui i do believe i can make log analysis code by parsing necessary 
#url='http://www.almhuette-raith.at/apache-log/access.log'
#page = requests.get(url)
#soup = BeautifulSoup(page.content, 'html.parser')
#split_data=soup.split()
#split_trans_data=split_data

#Make the data into csv or simple dataframe
#df=....
#Write regex
# Writing filter function
filtering_point='20/May/2021'
#df=read.csv('or file')
#df[something].str.contains(filtering_point)
#somelist=list(df[something].str.contains(filtering_point)
#len(somelist.unique())
# Length of the list will be counter function that will count each entry 


#If i can write proper way to scrape or download all this downloable format and store as df
#The rest will follow the code