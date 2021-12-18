import pandas as pd

pd.options.display.max_rows = 100

# all_airports = pd.read_csv('airports_origin.csv', index_col='Airport ID')
# all_airports.rename(columns = {'Tz database time zone': 'region'}, inplace = True) # replacing a long column name

# for x in all_airports.index:
#     if all_airports.loc[x,'IATA'] == "\\N" or all_airports.loc[x,'region'] == "\\N":
#         all_airports.drop(x, inplace = True) # filtering the dataframe from unfilled records

# all_airports = all_airports.join(all_airports['region'].str.split('/', 1, expand=True).rename(columns={0:'Region', 1:'Location'})) # parsing the column into two in order to separate the Region
# all_airports.drop('region', axis = 'columns', inplace = True) # dropping the original column

# all_airports.to_csv('airports.csv') # storing new and ready-to-use dataframe into a separate csv file

all_airports = pd.read_csv('airports.csv', index_col='Airport ID') #using stored result avoiding long previous steps

# print(all_airports)

# all_routes = pd.read_csv('routes_origin.csv')

# for x in all_routes.index:
#     if all_routes.loc[x,'Source airport ID'] == "\\N" or all_routes.loc[x,'Destination airport ID'] == "\\N":
#         all_routes.drop(x, inplace = True) # filtering the dataframe from unfilled records

# all_routes.drop('Codeshare', axis = 'columns', inplace = True) # dropping the empty Codeshare column
# all_routes.to_csv('routes.csv', index=False) # storing new and ready-to-use dataframe into a separate csv file

all_routes = pd.read_csv('routes.csv') #using stored result avoiding long previous steps
# print(all_routes.head(15))
