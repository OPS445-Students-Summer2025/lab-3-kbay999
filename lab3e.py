#!/usr/bin/env python3

# Author ID: kbay

my_list = [100, 200, 300, 'six hundred']



def give_list():
    #Returns all items in my_list unchanged
    return my_list

def give_first_item():
    #Returns the first item in my_list as a string
    return str(my_list[0])

def give_first_and_last_item():
    # Returns a list with the first and last items in my_list
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Returns a list with the second and thrird items in my_list
    return [my_list[1], my_list[2]]

if __name__ == '__main__':
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())