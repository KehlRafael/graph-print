# graph-print
 Simple script that prints a graph where nodes are color coded by a heatmap of the strategy distribution of an two strategy evolutionary game. It receives 2 text files as input, the strategy distribution of all vertex and the adjacency matrix of the graph. The output is an image with the color coded graph.
 
## Usage
 You'll need Numpy, Networkx and Matplotlib to run the script. You can run the script using:
 
 ```
 python graphPrint.py strategy_distribution adjacency_matrix
 ```
 
 `strategy_distribution` has the following format:
 
 ```
 v1s1 v1s2
 v2s1 v2s2
 v3s1 v3s2
 ```
 
 Where `vXsY` is the probability that the vertex player `X` uses strategy `Y`.
 
 `adjacency_matrix` has each entry separated by a space and each row is a new line.
 
 
 To use the `madeomocenniPrint` script you must first run the `simulations_madeo_mocenni` example from my [hyper-rational-games](https://github.com/KehlRafael/hyper-rational-games) project, which will generate all needed input files for that script. `madeomocenniPrint` will then plot all graphs and save them as `png` on the script folder.
 
 ## Examples
 On folder [Examples](Examples) theres 3 examples of input files and their respective output images.
