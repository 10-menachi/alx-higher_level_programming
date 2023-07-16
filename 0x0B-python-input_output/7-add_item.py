#!/usr/bin/python3
"""
This module contains a script that adds all arguments to a Python list,
and then save them to a file.
"""

import sys
import os.path
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

text_file = "add_item.json"
list_to_add = []

if os.path.isfile(text_file):
    list_to_add = load_from_json_file(text_file)

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        list_to_add.append(sys.argv[i])

save_to_json_file(list_to_add, text_file)
