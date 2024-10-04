"""Mutating functions."""

__author__ = "730748160"

def manual_append(append_list: list[int], append_value: int) -> None:
    #adding a new value(2nd parameter) to the list
    append_list.append(append_value)

def double(double_list: list[int]) -> None:
    #doubling or muliplying each number in the list by 2
    index:int = 0
    while index < len(double_list):
        double_list[index] = double_list[index] * 2

list_1: list[int] = [1,2,3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
