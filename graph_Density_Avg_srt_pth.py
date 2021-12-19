import pandas as pd
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import math as math


data = pd.read_csv('routes.csv')
SelReg = 'Asia'
regionData = data.loc[(data['Source Region'].str.startswith(SelReg)) & data['Destination Region'].str.startswith(SelReg)]
G = nx.from_pandas_edgelist(regionData,source = 'Source airport', target = 'Destination airport',edge_attr = True,create_using=nx.DiGraph)
PlotAvPathL = nx.average_shortest_path_length(G)
PlotDensity = nx.density(G)


print('Average shortest path --> {}\n Plot density -->{}'.format(PlotAvPathL,PlotDensity))





#plt.figure()
#nx.draw_networkx(G, with_labels=True)
#plt.show()