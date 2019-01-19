# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:34:41 2019

@author: Jan
"""

import networkx as nt
import numpy as np
import random


def get_knowledge(G, i, field):
    x = random.randrange(np.shape(field)[0])
    y = random.randrange(np.shape(field)[1])
    attributes = G.nodes[i]
    if (field[x, y] > 0):
        attributes['knowledge'][x, y] = field[x, y] - 1
        attributes['age_of_knowledge'] = 1
        attributes['assigment'] = (x, y)
        field[x, y] = 0


def share_knowledge(G):
    for node, attributes in G.nodes(data=True):
        if (attributes['assigment'] is None):
            continue

        for index, map_knowledge in np.ndenumerate(attributes['knowledge']):
            if (not map_knowledge > 0):
                continue

            nhood = set(nt.neighbors(G, node))

            for _ in range(attributes['age_of_knowledge']):
                # get neighbors of neighbors
                for node in nhood.copy():
                    nhood.update(nt.neighbors(G, node))
            # print(nhood);

            attributes['age_of_knowledge'] += 1

            # print(nhood)
            # print(temp_age)
            # print(node)
            for neighbour in nhood:
                connected_node_attr = G.nodes[neighbour]
                if (connected_node_attr['assigment'] is None
                        and map_knowledge > 0):
                    map_knowledge = map_knowledge - 1
                    attributes['knowledge'][index] = map_knowledge
                    connected_node_attr['assigment'] = index
            break


def main(max_iterations, map_size, number_of_cells_with_resources,
         value_of_resource, number_of_cliques, cliques_size):
    matrix_dim = (map_size, map_size)

    # base graph
    G = nt.connected_caveman_graph(number_of_cliques, cliques_size)

    # setup initial map conditions
    field = np.zeros(matrix_dim, dtype=int)

    # fill n cells with resources
    random_unique_indexes = random.sample([(x, y) for x in range(map_size)
                                           for y in range(map_size)],
                                          number_of_cells_with_resources)
    for index in random_unique_indexes:
        field[index] = value_of_resource

    # setup initial node attributes
    for node, attributes in G.nodes(data=True):
        attributes['assigment'] = None
        attributes['knowledge'] = np.zeros((map_size, map_size), dtype=int)
        attributes['age_of_knowledge'] = 0

    # print(type(G))
    # print(nt.neighbors(G,5))
    np.set_printoptions(threshold=np.nan)
    print(field)

    number_of_iterations = 10
    for i in range(number_of_iterations):
        for node, attributes in G.nodes(data=True):
            if (attributes['assigment'] is not None):
                continue
            # print(node)
            get_knowledge(G, node, field)

        # powiększanie wiedzy
        knowledge_sum = sum(1 for _, attributes in G.nodes(data=True)
                            if attributes['assigment'] is not None)

        print("Iter {}, stan wiedzy: {}, ".format(i, knowledge_sum))

        share_knowledge(G)


if __name__ == "__main__":
    # set None to disable max_iterations
    max_iterations = 10
    # ammount of resources placed on map
    number_of_cells_with_resources = 50
    # value of single resource
    value_of_resource = 11
    # map is square
    map_size = 50
    # parameters for caveman graph
    number_of_cliques = 10
    cliques_size = 100

    main(max_iterations, map_size, number_of_cells_with_resources,
         value_of_resource, number_of_cliques, cliques_size)
