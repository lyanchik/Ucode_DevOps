from functools import reduce  # Import the appropriate module


def multiplier(list_numb):
    if all((isinstance(i, (int, float)) for i in list_numb)):   # takes a list of numbers int/or float
        return reduce(lambda a, b: a * b, list_numb)            # returns the result of their multiplication
    else:
        raise ValueError('The given data is invalid.')          # If the arg isn't list or elements numerical
