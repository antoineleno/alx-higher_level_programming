#!/usr/bin/python3

def find_peak(list_of_integers):
    final_result = []
    for i in range(len(list_of_integers)):
        if i == 0:
            pass
        else:
            if (list_of_integers[i] > list_of_integers[i - 1] and list_of_integers[i] > list_of_integers[i + 1]):
                final_result.append(list_of_integers[i])

    my_len = len(final_result)
    if my_len > 0:
        return final_result[0]
    else:
        return None
