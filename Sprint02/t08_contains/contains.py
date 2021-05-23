def contains(str1,substr1):
    res_substr_list = []
    str1 = str1.lower()
    for i in substr1:
        if str1.find(i.lower()) != -1:
            res_substr_list.append(i)
    return res_substr_list