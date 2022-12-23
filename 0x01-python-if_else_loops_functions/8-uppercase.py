#!/usr/bin/python3
def uppercase(string):
    result = ''
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print('{:s}'.format(result))
