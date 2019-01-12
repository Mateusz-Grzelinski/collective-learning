# -*- coding: utf-8 -*-

import networkx as nt
import numpy as np
import random

p = 20
map_size = 10
n1 = 10
n2 = 10


def get_knowledge(G, i, field):
    x = random.randrange(map_size)
    y = random.randrange(map_size)
    attributes = G.nodes[i]
    if (field[x, y] > 0):
        attributes['knowledge'][x, y] = field[x, y] - 1
        attributes['hypothesis'][x, y] = field[x, y] - 1
        attributes['assigment'] = (x, y)


def share_knowledge(G, map_size):
    for node, attributes in G.nodes(data=True):
        if (attributes['assigment'] is not None):
            nhood = G[i]
            for j in range(map_size):
                for k in range(map_size):
                    for neighbour in nhood:
                        if (attributes['knowledge'][j, k] > 0):
                            break
                        connected_node_attr = G.nodes[neighbour]
                        if (connected_node_attr['assigment'] is None):
                            attributes['knowledge'][j, k] = attributes['knowledge'][j, k] - 1
                            connected_node_attr['assigment'] = (i, k)

            for neighbour in nhood:
                neigh_attr = G.nodes[neighbour]
                neigh_attr['hypothesis'] = np.logical_or(
                    attributes['knowledge'], G.nodes[neighbour]['knowledge']
                )

    for _, attributes in G.nodes(data=True):
        attributes['knowledge'] = attributes['hypothesis'].copy()

    # sum = 0
    # for node, attributes in G.nodes(data=True):
    #     if (attributes['assigment'] is not None):
    #         sum = sum + 1
    # print(sum)


if __name__ == "__main__":
    # base graph
    G = nt.caveman_graph(n1, n2)

    # setup initial map conditions
    field = np.zeros((map_size, map_size), dtype=int)
    for i in range(p):
        x = random.randrange(map_size)
        y = random.randrange(map_size)
        field[x, y] = 4

    # setup initial node attributes
    for node, attributes in G.nodes(data=True):
        attributes['assigment'] = None
        attributes['knowledge'] = np.zeros((map_size, map_size), dtype=int)
        attributes['hypothesis'] = np.zeros((map_size, map_size), dtype=int)

    # print(type(G))
    # print(nt.neighbors(G,5))
    print(field)

    number_of_iterations = 7
    for _ in range(number_of_iterations):
        for node, attributes in G.nodes(data=True):
            if (attributes['assigment'] is None):
                get_knowledge(G, node, field)
        # powiększanie wiedzy
        sum = 0
        for _, attributes in G.nodes(data=True):
            if (attributes['assigment'] is not None):
                sum = sum + 1
        print(sum)
        share_knowledge(G, map_size)
