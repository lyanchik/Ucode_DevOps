def make_unique(inp_dict):
    for key in inp_dict:
        inp_dict[key] = list(sorted(set(inp_dict[key])))  # removes all duplicate & sorts the elements
    return inp_dict