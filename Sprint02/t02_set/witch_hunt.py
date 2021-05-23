def witch_hunt(suspect_sets, innocent_sets):
    if suspect_sets and innocent_sets:
        guilty = set.intersection(*suspect_sets)
        return guilty.difference(*innocent_sets)
    elif suspect_sets:
        return set.intersection(*suspect_sets)
    else:
        return set()