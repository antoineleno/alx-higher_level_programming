#!/usr/bin/python
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    new_dic = {}
    new_dic = a_dictionary.copy()
    max_value = 0
    for key, value in new_dic.items():
        if value > max_value:
            max_value = value
    for key, value in a_dictionary.items():
        if value == max_value:
            return (key)
