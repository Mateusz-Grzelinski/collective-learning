def stats_from_data_list(samples):
    iter_to_max_knowledge = []
    for sample in samples:
        last_item = sample[-1]
        iter_to_max_knowledge.append(last_item.iteration)

    return iter_to_max_knowledge
