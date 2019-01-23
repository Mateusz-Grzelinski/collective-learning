import numpy as np
import matplotlib.pyplot as plt
from common_stats import stats_from_data_list
from main import main
from statistics import mean, stdev

if __name__ == "__main__":
    max_iterations = None
    map_size = 50
    number_of_cells_with_resources = 10
    value_of_resource = 10
    number_of_cliques = 10
    clique_size = 100
    p = 1

    image_name = r"_".join([
        "different_p",
        "map-{0}x{0}".format(map_size),
        "graph-{}-{}".format(number_of_cliques, clique_size),
        "res-{}-{}".format(number_of_cells_with_resources, value_of_resource),
        "p-{}".format(p)
    ])

    repeat = 5

    average_max_iter = []
    std_devs = []
    stats = []
    p_list = np.arange(0.1, 1.1, 0.1)
    for _ in range(repeat):
        data = []
        for p in p_list:
            print('p {}'.format(p))
            sample = main(
                max_iterations=max_iterations,
                max_knowledge=None,
                map_size=map_size,
                number_of_cells_with_resources=number_of_cells_with_resources,
                value_of_resource=value_of_resource,
                number_of_cliques=number_of_cliques,
                clique_size=clique_size,
                p=p)
            data.append(list(sample))
        sample_stats = stats_from_data_list(data)
        stats.append(sample_stats)
        print('iterations for single sample {}'.format(sample_stats))

    # iterate colums, not rows
    for stat in zip(*stats):
        average = mean(stat)
        average_max_iter.append(average)

        std_dev = stdev(stat)
        std_devs.append(std_dev)

    print('max_iter: {}'.format(average_max_iter))
    print('sttandard dev: {}'.format(std_devs))

    fig = plt.figure()
    plt.plot(p_list, average_max_iter)
    plt.xticks(p_list)
    plt.yticks(np.floor(np.arange(0, max(average_max_iter) + 1, step=max(average_max_iter) / 10)))
    plt.xlabel('p')
    plt.ylabel('iterations to max knowledge')
    fig.savefig(image_name)
