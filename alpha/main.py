import networkx as nt
import numpy as np
import random

number_of_cells_with_resources = 50
values_of_resource = 11
map_size = 50
n1 = 10    #iloć klik dla caveman graph
n2 = 100      #iloć w klice dla caveman graph
p=0.9       #szansa na przekazanie wiedzy


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
                    attrib=G.nodes[node]
                    if(attrib['assigment'] is not None):
                        nhood.update(nt.neighbors(G, node))
            #print(nhood);

            attributes['age_of_knowledge'] += 1

            # print(nhood)
            # print(temp_age)
            # print(node)
            for neighbour in nhood:
                connected_node_attr = G.nodes[neighbour]
                if (connected_node_attr['assigment'] is None and map_knowledge > 0 and random.random()<=p):
                    map_knowledge=map_knowledge-1
                    attributes['knowledge'][index] = map_knowledge
                    connected_node_attr['assigment'] = index
            break




if __name__ == "__main__":
    matrix_dim = (map_size, map_size)

    # base graph
    G = nt.connected_caveman_graph(n1, n2)

    # setup initial map conditions
    field = np.zeros(matrix_dim, dtype=int)

    # fill n cells with resources
    random_unique_indexes = random.sample(
        [(x, y) for x in range(map_size) for y in range(map_size)], number_of_cells_with_resources
    )
    for index in random_unique_indexes:
        field[index] = values_of_resource

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
        knowledge_sum = sum(
            1 for _, attributes in G.nodes(data=True) if attributes['assigment'] is not None
        )

        print("Iter {}, stan wiedzy: {}, ".format(i, knowledge_sum))

        share_knowledge(G)
