#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
st = 'Last digit of {:d} is {:d}'.format(number, last_digit)
if (last_digit > 5):
    st += ' and is greater than 5'
if (last_digit == 0):
    st += ' and is 0'
if (last_digit < 6 & last_digit != 0):
    st += ' and is less than 6 and not 0'
print(st)
