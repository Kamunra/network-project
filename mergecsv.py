import pandas as pd
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt


CsvAir = pd.read_csv('airports.csv')
CsvRoute = pd.read_csv('routes2.csv') #read both csv files 
Region = 'Europe'
AirNew = CsvAir.loc[CsvAir['Tz database time zone'].str.startswith(Region)] #filter Airports depending on the region


filter1 =  CsvRoute['Source airport ID'].isin(AirNew['Airport ID']) #filter Source Air ports Id to match the region
filter2 =  CsvRoute['Destination airport ID'].isin(AirNew['Airport ID']) #filter Destination Air ports Id to match the region

PortNew = CsvRoute.loc[filter1 & filter2]  #create new dataframe using both filters 

print(PortNew)