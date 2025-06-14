#!/usr/bin/env python3

# Author ID: kbay



courses = [ 'uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635' ]
print(courses[0])
courses[0] = 'eac150'
print(courses[0])
print(courses)

courses.append('ops235')    # Add a new item to the end of the list object named courses
print(courses)

courses.insert(0, 'hwd101') # Add a new item to the specified index location, 
                            # the original item will be pushed to the next index location
print(courses)

courses.remove('ops335')    # Remove first occurrence of a matching item in the list object
print(courses)

sorted_courses = courses.copy() # Create a copy of the courses list
sorted_courses.sort()           # Sort the new list 
print(courses)
print(sorted_courses)

list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]
length_of_list = len(list_of_numbers)    # Returns the length of the list
smallest_in_list = min(list_of_numbers)  # Returns the smallest value in the list
largest_in_list = max(list_of_numbers)   # Returns the largest value in the list

# Notice how the long line below is wrapped to fit on one screen:
print("List length is " + str(length_of_list) + 
      ", smallest element in the list is " + str(smallest_in_list) +
      ", largest element in the list is " + str(largest_in_list))


# Place my_list below this comment (before the function definitions)
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    if ordered_list:  # Check if the list is not empty
        next_value = ordered_list[-1] + 1
    else:
        next_value = 1  # If list is empty, start at 1
    ordered_list.append(next_value)

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values, found in items_to_remove list, from ordered_list
    for item in items_to_remove:
        while item in ordered_list:
            ordered_list.remove(item)

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)
