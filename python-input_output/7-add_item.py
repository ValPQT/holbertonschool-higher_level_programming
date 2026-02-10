#!/usr/bin/python3
import sys
import json
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

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


