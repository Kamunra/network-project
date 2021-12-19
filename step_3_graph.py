from networkx.algorithms.centrality import betweenness
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

    
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
    conn=nx.degree_centrality(G)
    conn_values=[]
    for key, value in conn.items():
        conn_values.append(value)
    return conn_values
    
data = pd.read_csv('network-project/routes.csv')
SelReg = 'Asia'
regionData = data.loc[(data['Source Region'].str.startswith(SelReg)) & data['Destination Region'].str.startswith(SelReg)]
G = nx.from_pandas_edgelist(regionData,source = 'Source airport', target = 'Destination airport',edge_attr = True,create_using=nx.DiGraph)
PlotAvPathL = nx.average_shortest_path_length(G)
PlotDensity = nx.density(G)

print('Average shortest path --> {}\n Plot density -->{}'.format(PlotAvPathL,PlotDensity))
Nodes=[]
between_values=bet_centrality(G)
close_values=close_centrality(G)
conn_values=deg_connectivity(G)

with open("network-project/Node_characteristics.csv",'w') as f:
    f.write("Node\t closeness centrality\t degree centrality\t betweenness centrality\n")  
    for i in range(0, len(close_values)):
        f.write("{0}\t{1}\t{2}\t{3}\n".format(Nodes[i],close_values[i],conn_values[i],between_values[i]))