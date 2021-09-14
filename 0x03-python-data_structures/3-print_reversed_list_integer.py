#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list_reversed = []
    list_size = len(my_list)

    while list_size:
        list_size -= 1
        my_list_reversed.append(my_list[list_size])
    for item in my_list_reversed:
        print("{:d}".format(item))
