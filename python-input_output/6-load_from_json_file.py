#!/usr/bin/python3
import json

def load_from_json_file(filename):
    with open(filename, mode= "w+") as filename:
        json.load(my_obj, filename)
