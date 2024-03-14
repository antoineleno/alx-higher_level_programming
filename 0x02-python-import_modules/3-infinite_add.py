#!/usr/bin/python3
import sys
"""
main function to calculate the sum of the arguments
"""
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0")
    else:
        result = 0
        for i in range(1, len(sys.argv)):
            number = int(sys.argv[i])
            result = result + number
            i += 1
        print(result)
