import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys

arq = sys.argv[1]
arqM = sys.argv[2]

# Load files from Scilab
X = np.loadtxt(arq)
A = np.loadtxt(arqM)

# Load graph from adjacency matrix
G = nx.from_numpy_matrix(A)

# Load populations to generate the graphic
values = [X[i,1] for i in range(X.shape[0])]

# Generate graph
nx.draw(G, cmap=plt.get_cmap('autumn'), node_color=values, with_labels=True, font_color='black',vmin=0,vmax=1)

# Create the colorbar
sm = plt.cm.ScalarMappable(cmap=plt.get_cmap('autumn'), norm=plt.Normalize(vmin = 0, vmax=1))
sm._A = []
plt.colorbar(sm,shrink=0.94)

# Plot image
plt.show()


