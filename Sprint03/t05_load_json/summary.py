import collections
import json


def summary(filename, summarize_by):

    try:
        with open(filename) as data:  # load the JSON data stored in the file with the filename
            json_data = data.read()
            json_list = json.loads(json_data)
    except ValueError:  # JSON is invalid, catch the exception and return a string
        return print('Error in decoding JSON.')

    counter = collections.Counter()
    for j_dict in json_list:
        try:
            counter.update({j_dict[summarize_by]})  # update([iterable - or -mapping])
        except KeyError:  # if not found item  increase the counter of None by one
            counter.update({None})  # if found item, but the value is None
        except TypeError:
            counter.update({'unhashable'})  # if found, but the value is unhashable
    summarize_dict = dict(sorted(counter.items(), key=lambda n: n[1], reverse=True))
    return summarize_dict