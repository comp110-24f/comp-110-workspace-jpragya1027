"""Writing the program to find the max in a certain list"""

__author__ = "730748160"


def find_and_remove_max(input: list[int]) -> int:
    #this function finds the maximum value in a list and removes it from said list
    if len(input) == 0:
        return -1 #in case the input is an empty list
    
    
    index:int = 0
    largest:int = input[index]
    index_of_large:int = 0
    while index < len(input):
        if input[index] >= largest:
            largest = input[index] #stores the largest value
            index_of_large = index
        index += 1
    
    index = 0
    while index < len(input): #this while loop is to pop out/remove the largest value, including repeats
        if input[index] >= largest:
            index_of_large = index
            input.pop(index_of_large)
            index = index - 1
        index += 1 

    
    return largest