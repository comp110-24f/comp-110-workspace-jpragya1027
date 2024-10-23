"""This excersise helps us work with writing functions and using unit tests"""

__author__ = "730748160"

def only_evens(number_list: list[int]) -> list[int]:
    """takes a input list and returns only the even numbers"""
    even_list: list[int] = [] #creates empty list for_even list

    for index in range(len(number_list)):
        if number_list[index] % 2 == 0: #tests if every singlie value in input list is even and if it is, adds to new list
            even_list.append(number_list[index])
    
    return even_list


def sub(number_list: list[int], start_index: int, end_index:int) -> list[int]:
    """Returns a sublist based on the given input list using the start and end indexes to crop list"""
    if start_index < 0:
        start_index = 0 #if start_index is less than 0, the function starts looping through and cropping at index 0, or the start

    if end_index > len(number_list):
        end_index = len(number_list) #if end_index is more than the length of list, the function finishes looping through and cropping at the last index, or the end

    new_list: list[int] = []

    for index in range(start_index, end_index):
        new_list.append(number_list[index]) # adds valid numbers to a new list

    return new_list

def add_at_index(input: list[int], value: int, index: int) -> None:
    """This function adds a new value in the input list at the given index"""
    if index < 0 or index > len(input):
        raise IndexError("Index is out of bounds for the input list")
    
    input.append(0)  # We append a placeholder, to create space
    
    # Shift elements to the right starting from the end to make room at 'index'
    for i in range(len(input) - 1, index, -1):
        input[i] = input[i - 1]

    input[index] = value #assigns the space(input[index]) the correct value of 'value'