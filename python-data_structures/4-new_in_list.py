#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list.copy())
    if idx > my_list[idx]:
        return (my_list.copy())
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
