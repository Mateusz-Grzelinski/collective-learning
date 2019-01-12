# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import networkx as nt
import numpy as np
import random

p = 50
p_val=11
map_size = 50
n1 = 10
n2 = 100


def get_knowledge(G, i, field):
    x = random.randrange(map_size)
    y = random.randrange(map_size)
    attributes = G.nodes[i]
    if (field[x, y] > 0):
        attributes['knowledge'][x, y] = field[x, y] - 1
        attributes['age_of_knowledge'] = 1
        attributes['assigment'] = (x, y)
        field[x,y]=0


def share_knowledge(G, map_size):
    for node, attributes in G.nodes(data=True):
        if (attributes['assigment'] is not None): 
            r=False
            for j in range(map_size):
                for k in range(map_size):
                    if (attributes['knowledge'][j, k] > 0):
                        nhood = set(nt.neighbors(G,node))
                        old_nhood = nhood.copy()
                        temp_age = attributes['age_of_knowledge']
                        attributes['age_of_knowledge']=attributes['age_of_knowledge']+1
                        for i in range(temp_age):
                            #print(old_nhood)
                            for close_neighbour in old_nhood:
                                nhood.update(set(nt.neighbors(G,close_neighbour)))
                                #print(set(nt.neighbors(G,close_neighbour)))
                            old_nhood=nhood.copy()
#                        print(nhood)
#                        print(temp_age)
#                        print(node)
                        for neighbour in iter(nhood):
                            connected_node_attr = G.nodes[neighbour]
                            if (connected_node_attr['assigment'] is None and attributes['knowledge'][j, k] > 0):
                                attributes['knowledge'][j, k] = attributes['knowledge'][j, k] - 1
                                connected_node_attr['assigment'] = (j, k)
                        r=True
                    if(r):
                        break
                if(r):
                    break
                    
#            for neighbour in nhood:
#                neigh_attr = G.nodes[neighbour]
#                neigh_attr['age_of_knowledge'] = np.logical_or(
#                    attributes['knowledge'], G.nodes[neighbour]['knowledge']
#                )

#    for _, attributes in G.nodes(data=True):
#        attributes['knowledge'] = attributes['age_of_knowledge'].copy()

    # sum = 0
    # for node, attributes in G.nodes(data=True):
    #     if (attributes['assigment'] is not None):
    #         sum = sum + 1
    # print(sum)


if __name__ == "__main__":
    # base graph
    G = nt.connected_caveman_graph(n1, n2)

    # setup initial map conditions
    field = np.zeros((map_size, map_size), dtype=int)
    for i in range(p):
        x = random.randrange(map_size)
        y = random.randrange(map_size)
        while field[x,y]>0:   
            x = random.randrange(map_size)
            y = random.randrange(map_size)
        field[x, y] = p_val

    # setup initial node attributes
    for node, attributes in G.nodes(data=True):
        attributes['assigment'] = None
        attributes['knowledge'] = np.zeros((map_size, map_size), dtype=int)
        attributes['age_of_knowledge'] = 0

    # print(type(G))
    # print(nt.neighbors(G,5))
    print(field)

    number_of_iterations = 10
    for _ in range(number_of_iterations):
        for node, attributes in G.nodes(data=True):
            if (attributes['assigment'] is None):
                #print(node)
                get_knowledge(G, node, field)
        # powiększanie wiedzy
        sum = 0
        for _, attributes in G.nodes(data=True):
            if (attributes['assigment'] is not None):
                sum = sum + 1
        print("przed")
        print(sum)
        share_knowledge(G, map_size)
        sum=0
        for _, attributes in G.nodes(data=True):
            if (attributes['assigment'] is not None):
                sum = sum + 1
        print("po")
        print(sum)
