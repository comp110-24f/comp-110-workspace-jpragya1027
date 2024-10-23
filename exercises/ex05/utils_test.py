from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index 

""" This excersise helps us practice with using unit tests to make sure our code is working how we want it to :) """

__author__ = "730748160"

def test_output_only_evens() -> None:
    #checks if only_evens returns the right output
    example :list[int] = [9, 2, 4, 3, 8, 0, 4, 1]
    assert only_evens(example) == [2, 4, 8, 0, 4]

def test_mutation_only_evens() -> None:
    #checks if only_evens doesn't mutate the input list
    example : list[int] = [9, 2, 4, 3, 8, 0, 4, 1]
    only_evens(example)
    assert example == [9, 2, 4, 3, 8, 0, 4, 1]

def test_edgecase_only_evens() -> None:
    #checks what happens in the odd case that only odd numbers are given
    example : list[int] =  [1, 5, 3, 7]
    assert only_evens(example) == []

"""Starting tests for sub function"""
def test_output_sub() -> None:
    #checks if sub returns the correct output
    example: list[int] = [9, 2, 4, 3, 8, 0, 4, 1]
    assert sub(example, 2, 5) == [4, 3, 8]

def test_mutation_sub() -> None:
    #checks if sub doesn't mutate the input function
    example: list[int] = [9, 2, 4, 3, 8, 0, 4, 1]
    sub(example, 2, 5)
    assert example == [9, 2, 4, 3, 8, 0, 4, 1]

def test_edgecase_sub() -> None:
    #checks what happens in the odd case where the start and end indexes are negative and/or out of the bounds of the list
    example: list[int] = [9, 2, 4, 3, 8, 0, 4, 1]
    assert sub(example, -2, 13) == [9, 2, 4, 3, 8, 0, 4, 1]

"""Starting tests for add_at_index function"""
def test_output_add_at_index() -> None:
    #checks if add_at_index returns no output
    example: list[int] = [1, 2, 3, 4, 5, 7]
    assert type(add_at_index(example, 6, 5)) == None

def test_mutation_add_at_index() -> None:
    #checks if add_at_index correctly mutates the input function
    example: list[int] = [1, 2, 3, 4, 5, 7]
    add_at_index(example, 6, 5)
    assert example == [1, 2, 3, 4, 5, 6, 7]

import pytest
def test_edgecase_add_at_index() -> None:
    #checks what happens and if the error is thrown in the odd case that the index given is larger than the length of function
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    example: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(example, 6, 5) 
        # an IndexError is raised for the case when the add_at_index is given an index that is greater than the length of our example

"""Calling all test functions"""
test_output_only_evens()
test_mutation_only_evens()
test_edgecase_only_evens()

test_output_sub()
test_mutation_sub()
test_edgecase_sub()

test_output_add_at_index()
test_mutation_add_at_index()
test_edgecase_add_at_index()