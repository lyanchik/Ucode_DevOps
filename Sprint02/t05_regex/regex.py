import re
def check_address(addr_dict):
    pattern = r"^Ukraine,[ ]*[a-zA-z-[ ]*]*,[ ]*[a-zA-z-[ ]*]*[ ]*\d{1,6},[ ]*\d{5}$"
    res_list = []
    for k, v in addr_dict.items():
        if re.search(pattern, v):
            res_list.append(f'The address of {k} is valid.')
        else:
            res_list.append(f'The address of {k} is invalid.')
    return res_list