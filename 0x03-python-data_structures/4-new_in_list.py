#!/usr/bin/python3

def new_in_list(my_list, index, element):
    new_list = mylist[:]
    if index < 0:
        return new_list
    elif index >= len(my_list):
        return new_list
    else:
        new_list[index] = element
        return new_list


if __name__ = '__main__':
    my_list = [1, 2, 3, 4, 5]
    index = 3
    new_element = 9
    new_list = new_in_list(my_list, index, new_element)

    print(new_list)
    print(my_list)
