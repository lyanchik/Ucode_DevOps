def raise_error(key, message):  # The function takes two strings: a key and a message
    errors = {'value': ValueError(message), 'key': KeyError(message),
              'index': IndexError(message), 'memory': MemoryError(message),
              'name': NameError(message), 'eof': EOFError(message)}
    if key in errors:
        raise errors[key]
    else:
        raise ValueError('No error with such key.')  # If the key is not one of the errors dict
