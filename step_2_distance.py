import pandas as pd
from math import radians, cos, sin, acos, sqrt

def distance(lat1, long1, lat2, long2):
    lat1 = radians(lat1)
    long1 = radians(long1)
    lat2 = radians(lat2)
    long2 = radians(long2)
    
    # Radius of earth in kilometers
    r = 6371
    
    return (r*acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(long2-long1)))

all_airports = pd.read_csv('airports.csv', index_col='Airport ID')
all_routes = pd.read_csv('routes.csv')

all_routes['Distance'] = [0 for i in range(len(all_routes.index))]
all_routes['Source Region'] = ['' for i in range(len(all_routes.index))]
all_routes['Destination Region'] = ['' for i in range(len(all_routes.index))]

for x in all_routes.index:
    source_id = all_routes.loc[x,'Source airport ID']
    dest_id = all_routes.loc[x,'Destination airport ID']
    all_routes.loc[x,'Distance'] = distance(all_airports.loc[source_id, 'Latitude'],
                                            all_airports.loc[source_id, 'Longitude'],
                                            all_airports.loc[dest_id, 'Latitude'],
                                            all_airports.loc[dest_id, 'Longitude'])
    all_routes.loc[x,'Source Region'] = all_airports.loc[source_id, 'Region']
    all_routes.loc[x,'Destination Region'] = all_airports.loc[dest_id, 'Region']

all_routes.to_csv('routes_mod.csv', index=False) # storing new and ready-to-use dataframe into a separate csv file