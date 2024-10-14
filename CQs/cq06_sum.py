"""Summing the elements of a list using different loops"""

__author__ = "730748160"

def w_sum(vals: list[float]) -> float:
    #w_sum takes input a list of floats vals: list[float], and returns the sum of all elements using a while loop
    index:int = 0
    sum:float = 0.0
    while index < len(vals):
        sum = sum + vals[index]
        index += 1
    return sum

def f_sum(vals: list[float]) -> float:
    #f_sum takes as input a list of floats vals: list[float], and returns the sum of all elements using a for...in loop without using range
    sum:float = 0.0
    for elem in vals:
        sum = sum + elem
    return sum

def f_range_sum(vals: list[float]) -> float:
    #f_range_sum takes as input a list of floats vals: list[float], and returns the sum of all elements using a for...in range loop
    sum:float = 0.0
    for elem in range(len(vals)):
        sum = sum + vals[elem]
    return sum