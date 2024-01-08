#!/usr/bin/python3


def replace_in_list(my_list, index, element):
    if index < 0:
        return my_list
    elif index >= len(my_list):
        return myl_list
    else:
        my_list[index] = element
        return my_list


if __name__ == '__main__':
    my_list = [1,2,3,4,5]
    index = 3
    new_element = 9
    new_list = replace_in_list(my_list, index, new_element)

    print(new_list)
    print(my_list)
