import itertools as it

def group(to_group, keys):  # function takes two arguments: a dict to_group and a list keys of fields to group by
    for i in range(len(keys)):
        res_dict = dict()
        grouped = it.groupby(to_group, key=lambda x: x [keys[i]])
        for key, val in grouped:
            res_dict.update({key: list(val)})

        # for keys[i],v in res_dict.items():
        #     if keys[i]
        # res_dict_n = res_dict.pop(keys[i])

        return res_dict    # returns new dict that is grouped by the fields provided in the list of fields(in the order of the list)
#
# if __name__ == '__main__':
#     test_case_data = [
#         {
#             'name': 'Alex',
#             'gender': 'male',
#             'species': 'human',
#             'job': 'bicycle repair man',
#         },
#         {
#             'name': 'Monika',
#             'gender': 'female',
#             'species': 'human',
#             'job': 'stockbroker'
#         }]
#
#     test_case_data_group_fields_1 = ['gender']
#     res_1 = group(test_case_data, test_case_data_group_fields_1)
#     print(res_1)
# #

# res_dict1= res_dict.update({key: {**res_dict.pop(keys)}})
# ds = [d for d in ds if d['key1'] != 'value1']
    #     print(list(val))
    #     i.pop(keys)
    #     res_dict = {key: list([i])}




