import networkx as nx
import matplotlib.pyplot as plt
from random import randint as rd


def graph_coloring(graph):

    gr_dict = {i : [] for i in graph.nodes()}
    for i, j in graph.edges():
        gr_dict[i] += [j]
        gr_dict[j] += [i]
    colored = dict()

    for root in gr_dict.keys():
        colored[root] = 0
        for i in gr_dict[root]:
            if i in colored.keys() and colored[root] == colored[i]:
                colored[root] += 1

    for root in gr_dict.keys():
        colored[root] = 0
        for i in gr_dict[root]:
            if colored[root] == colored[i]:
                colored[root] += 1
    return colored

if __name__ == '__main__':
    NODES_COUNT = 7 + 1
    graph = nx.Graph()
    graph.add_nodes_from(range(1, NODES_COUNT))
    for i in range(1, NODES_COUNT):
        for j in range(i, rd(i, NODES_COUNT)):
            if i != j:
                graph.add_edge(i, j)
    plt.subplot(121)
    nx.draw_circular(graph, with_labels=True)
    
    colored = graph_coloring(graph)
    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'pink']
    print(colored)
    node_colors = []
    for vert in graph.nodes():
        node_colors.append(colors[colored[vert]])
    
    print(node_colors)
    
    plt.subplot(122)
    nx.draw_circular(graph, with_labels = True, node_color=node_colors)
    plt.show()