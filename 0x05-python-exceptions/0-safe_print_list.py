#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    for elem in range(x):
        try:
            print(my_list[elem], end="")
            num += 1
        except Exception:
            continue
    print()
    return num
