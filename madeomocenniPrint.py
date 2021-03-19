import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys


def printToPNG(X, A, name):
    # Load graph from adjacency matrix
    G = nx.from_numpy_matrix(A)

    # Load populations to generate the graphic
    values = [X[i,0] for i in range(X.shape[0])]

    # Generate graph
    nx.draw(G, cmap=plt.get_cmap('autumn'), node_color=values, with_labels=True, font_color='black',vmin=0,vmax=1)

    # Create the colorbar
    sm = plt.cm.ScalarMappable(cmap=plt.get_cmap('autumn'), norm=plt.Normalize(vmin = 0, vmax=1))
    sm._A = []
    plt.colorbar(sm,shrink=0.94)

    # Plot image
    plt.savefig(name)
    plt.close()

ini_cond = ['external', 'central', 'ext_cent']
graph = ['open_star', 'closed_star', 'asym_weighted']

# Bistability
for i in range(3):
    for j in range(3):
        X = np.loadtxt('bi-'+ini_cond[i]+'-'+graph[j]+'.txt')
        A = np.loadtxt(graph[j]+'.txt')
        printToPNG(X, A, 'bi-'+ini_cond[i]+'-'+graph[j]+'.png')

# Prisoner's Dilemma
for i in range(3):
    for j in range(3):
        X = np.loadtxt('pd-'+ini_cond[i]+'-'+graph[j]+'.txt')
        A = np.loadtxt(graph[j]+'.txt')
        printToPNG(X, A, 'pd-'+ini_cond[i]+'-'+graph[j]+'.png')

# Coexistance
for i in range(3):
    for j in range(3):
        X = np.loadtxt('co-'+ini_cond[i]+'-'+graph[j]+'.txt')
        A = np.loadtxt(graph[j]+'.txt')
        printToPNG(X, A, 'co-'+ini_cond[i]+'-'+graph[j]+'.png')
