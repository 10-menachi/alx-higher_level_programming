#!/usr/bin/python3
def islower(string):
    for char in string:
        print('{}'.format(chr(ord(char) - 32)), end='\n' if char == '\n' else '')
    print('')
