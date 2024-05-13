#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = set()
    for i in my_list:
        result.add(i)
    return sum(result)
