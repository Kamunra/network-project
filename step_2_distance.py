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