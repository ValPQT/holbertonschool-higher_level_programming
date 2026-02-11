#!/usr/bin/python3
"""
This script adds all command-line arguments to a JSON file (add_item.json).
It loads the existing list from the file, appends new arguments, and saves
the updated list back. The JSON file is created if it does not exist.
"""

import sys
import json
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
Main function to add command-line arguments to a JSON file.
"""
args = sys.argv
if path.exists('add_item.json'):
    list = load_from_json_file('add_item.json')
else:
    list = []
save_to_json_file(list, 'add_item.json')

if len(sys.argv) >= 2:
    for i in range(1, len(sys.argv)):
        list.append(sys.argv[i])
save_to_json_file(list, 'add_item.json')
