import re
def clear_words(txt_str):
    regex_mark = r' |\?|!|\.|:|;|,|-'
    spl_str = txt_str.split(' ')   # splits the string by space
    rm_mark = lambda x: re.sub(regex_mark, "", x)
    return list(map(rm_mark, spl_str))