#!/usr/bin/python
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    rom_rep = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    prev_value = 0
    total = 0
    for chr in roman_string:
        value = rom_rep.get(chr, 0)
        if value == 0:
            return 0
        if value > prev_value:
            total += value - 2*prev_value
        else:
            total += value
        prev_value = value
    return total
