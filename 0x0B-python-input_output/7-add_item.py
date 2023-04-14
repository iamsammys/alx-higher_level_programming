#!/usr/bin/python3

"""module to add all arguments to a Python list,
and then save them to a file
"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


try:
    my_list = load_from_json_file("add_item.json")
except:
    my_list = []

[my_list.append(args) for args in argv if args != argv[0]]

try:
    save_to_json_file(my_list, "add_item.json")
except Exception as e:
    print("try failed again")
    print(e)
