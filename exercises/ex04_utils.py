"""Excersize number 4, helping us learn comutational thinking"""

__author__ = "730748160"

def all (int_list:list[int] , target:int) -> bool:
    # Return True if all integers in the list match the target integer, False otherwise.

    if len(int_list) == 0:
        return False
    
    for elem in int_list:
        if elem != target: #check if each elem in list is equal to target
            return False
        
    return True


def max(int_list:list[int]) -> int:
    #Return the largest integer in the list. Raises ValueError if the list is empty.

    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    
    largest:int = 0
    for elem in int_list:
        if elem > largest: # Update largest if we find a bigger number
            largest = elem
    
    return largest

def is_equal(list1: list[int], list2: list[int]) -> bool:
    #Return True if both lists are deeply equal, False otherwise.

    if len(list1) != len(list2):
        return False
    
    for index in range(len(list1)):
        if list1[index] != list2[index]: #compare each indiv element of the 2 lists
            return False
    
    return True

def extend(list1: list[int], list2: list[int]) -> None:
    #Mutate or change list1 by appending/adding elements of list2 to the end of it.

    for elem in list2:
        list1.append(elem) #add each elem of list2 to list1(with each iteration)