#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number > 0:
    remainder = number % 10
else number < 0:
    remainder = number % -10

if remainder > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, remainder))
elif remainder == 0:
    print("Last digit of {:d} is 0 and is {:d}"
          .format(number, remainder))
elif remainder < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, remainder))
