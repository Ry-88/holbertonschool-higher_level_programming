#!/usr/bin/env python3
def uniq_add(my_list=[]):
    unique_items = []
    for number in my_list:
        if number not in unique_items:
            unique_items.append(number)
    return sum(unique_items)
