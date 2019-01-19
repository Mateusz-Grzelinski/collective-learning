import argparse


def arg_parse():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(
        '-i',
        '--iterations',
        dest='max_iter',
        type=int,
        help='iterate maximum MAX_ITER times. If not set, iterate until all'
        ' knowledge is collected')
    parser.add_argument(
        '-s',
        '--map-size',
        dest='map_size',
        type=int,
        default=100,
        help='map is square with side MAP_SIZE')
    parser.add_argument(
        '-n',
        '--resource-number',
        dest='number_of_cells_with_resources',
        type=int,
        default=10,
        help='number of resources placed on map')
    parser.add_argument(
        '-v',
        '--resource-value',
        dest='value_of_resource',
        type=int,
        default=10,
        help='value of single resource on map')
    parser.add_argument(
        '-N',
        '--caveman-cliques',
        dest='number_of_cliques',
        type=int,
        default=10,
        help='parameter for caveman graph')
    parser.add_argument(
        '-C',
        '--clique-size',
        dest='clique_size',
        type=int,
        default=100,
        help='parameter for caveman graph')
    parser.add_argument(
        '-p',
        dest='p',
        type=float,
        default=1,
        help='probability of sharing knowledge')
    parser.add_argument(
        '-o',
        '--output-image',
        dest='output_image',
        type=str,
        default='learning',
        help='name of output graph (png image).'
        'metadata will be appended to image name')

    return parser.parse_args()
