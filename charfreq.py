#Given a string, sort it in decreasing order based on the frequency of characters.
#If there are multiple possible solutions, return any of them.

#For example, given the string tweet, return tteew. eettw would also be acceptable.

import operator

def get_char_frequency_dict(str):
    c_dict = {}
    for c in str:
        if c in c_dict:
            c_dict[c] = c_dict[c] + 1
        else:
            c_dict[c] = 1

    sorted_c_dict = dict(sorted(c_dict.items(), key=operator.itemgetter(1),reverse=True))

    return sorted_c_dict

def print_c_dict(c_dict):
    str = ""
    for key in c_dict:
        for i in range(c_dict[key]):
            str = str + key
    return str

str = "tweet"
c_dict = get_char_frequency_dict(str)
print(c_dict)
s_str = print_c_dict(c_dict)

print(s_str)