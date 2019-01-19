# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:34:41 2019

@author: Jan
"""

import networkx as nt
import numpy as np
import random
import logging
from parsing import arg_parse

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


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

            attributes['age_of_knowledge'] += 1

            for neighbour in nhood:
                connected_node_attr = G.nodes[neighbour]
                if (connected_node_attr['assigment'] is None
                        and map_knowledge > 0):
                    map_knowledge = map_knowledge - 1
                    attributes['knowledge'][index] = map_knowledge
                    connected_node_attr['assigment'] = index
            break


def iterate_knowledge(G, map):
    i = 0
    while True:
        # each node gains new knowledge
        for node, attributes in G.nodes(data=True):
            if (attributes['assigment'] is not None):
                continue
            get_knowledge(G, node, map)

        # now collective knowledge is bigger
        knowledge_sum = sum(1 for _, attributes in G.nodes(data=True)
                            if attributes['assigment'] is not None)

        # they can share it with each other
        share_knowledge(G)

        # stop if knowledge is maximum
        max_knowledge = number_of_cells_with_resources * value_of_resource
        if knowledge_sum == max_knowledge:
            logging.info('All knowledge is collected')
            break

        # max_iterations does not need to be set
        if max_iterations is not None:
            if i == max_iterations:
                break

        i += 1
        yield (i, knowledge_sum)


def main(max_iterations, map_size, number_of_cells_with_resources,
         value_of_resource, number_of_cliques, clique_size):
    matrix_dim = (map_size, map_size)

    # base graph
    G = nt.connected_caveman_graph(number_of_cliques, clique_size)

    # setup initial map conditions
    map = np.zeros(matrix_dim, dtype=int)

    # fill number_of_cells_with_resources cells with resources
    random_unique_indexes = random.sample([(x, y) for x in range(map_size)
                                           for y in range(map_size)],
                                          number_of_cells_with_resources)
    for index in random_unique_indexes:
        map[index] = value_of_resource

    # setup initial node attributes
    for node, attributes in G.nodes(data=True):
        attributes['assigment'] = None
        attributes['knowledge'] = np.zeros((map_size, map_size), dtype=int)
        attributes['age_of_knowledge'] = 0

    # np.set_printoptions(threshold=np.nan)
    logging.debug(map)
    for i, knowledge_sum in iterate_knowledge(G, map, max_knowledge):
        logging.info('Iter {}, stan wiedzy: {}, '.format(i, knowledge_sum))


if __name__ == "__main__":
    args = arg_parse()
    logging.info('using values: {}'.format(vars(args)))

    # set None to disable max_iterations
    max_iterations = args.max_iter
    # ammount of resources placed on map
    number_of_cells_with_resources = args.number_of_cells_with_resources
    # value of single resource
    value_of_resource = args.value_of_resource
    # map is square
    map_size = args.map_size
    # parameters for caveman graph
    number_of_cliques = args.number_of_cliques
    clique_size = args.clique_size
    # output image name
    image_name = args.output_file

    main(max_iterations, map_size, number_of_cells_with_resources,
         value_of_resource, number_of_cliques, clique_size)
