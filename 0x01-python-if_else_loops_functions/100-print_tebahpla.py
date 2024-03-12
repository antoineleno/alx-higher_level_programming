#!/usr/bin/python3
for i in range(122, 96, -1):
    print(chr(i if i % 2 == 0 else i - 32), end = ("" if i != 97 else "\n"))

