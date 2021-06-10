def extractor(extractable, value_type=str):
    index_dict = extractable.items()
    class_type = lambda item: isinstance(item[1], value_type)
    new_dict = dict(filter(class_type, index_dict))            # create a new dictionary contains items from
    return new_dict                                            # extractable that have a value of type value_type.
