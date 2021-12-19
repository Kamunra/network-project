from typing import OrderedDict
from networkx.algorithms.centrality import betweenness
from networkx.algorithms.centrality.degree_alg import degree_centrality
from networkx.algorithms.operators.unary import reverse
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import operator
    
def bet_centrality(G):
    between=nx.betweenness_centrality(G)
    between_values=[]
    for key, value in between.items():
        Nodes.append(key)
        between_values.append(value)
    return between_values
def close_centrality(G):
    close=nx.closeness_centrality(G)
    close_values=[]
    for key, value in close.items():
        close_values.append(value)
    return close_values
def deg_connectivity(G):
    deg=dict(nx.degree(G))
    deg_values=[]
    for key, value in deg.items():
        deg_values.append(value)
    return deg_values
    
data = pd.read_csv('routes.csv')
SelReg = 'Asia'
regionData = data.loc[(data['Source Region'].str.startswith(SelReg)) & data['Destination Region'].str.startswith(SelReg)]
G = nx.from_pandas_edgelist(regionData,source = 'Source airport', target = 'Destination airport',edge_attr = True,create_using=nx.DiGraph)
PlotAvPathL = nx.average_shortest_path_length(G)
PlotDensity = nx.density(G)

print('Average shortest path --> {}\n Plot density -->{}'.format(PlotAvPathL,PlotDensity))
Nodes=[]
between_values=bet_centrality(G)
close_values=close_centrality(G)
deg_values=deg_connectivity(G)

with open("Node_characteristics.csv",'w') as f:
    f.write("Node\t closeness centrality\t degree connectivity\t betweenness centrality\n")  
    for i in range(0, len(close_values)):
        f.write("{0}\t{1}\t{2}\t{3}\n".format(Nodes[i],close_values[i],deg_values[i],between_values[i]))

deg_conn=dict(nx.degree(G))
top10_deg_con = dict(sorted(deg_conn.items(), key=operator.itemgetter(1),reverse=True)[:10])
print(top10_deg_con)
