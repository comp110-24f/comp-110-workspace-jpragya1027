from CQs.cq07.find_max import find_and_remove_max

"""Testing the program to find the max in a certain list"""

__author__ = "730748160"

def test_output_find_and_remove_max(input:list[int]) -> None:
    #tests whether the find_and_remove_max function returns the correct value
    example:list[int] = [9, 11, 5, 7, 2, 1, 4]
    assert find_and_remove_max(example) == 11

def test_mutation_find_and_remove_max(input:list[int]) -> None:
    #tests whether the find_and_remove_max function modifies the list correctly and removes the largest value
    example: list[int] = [9, 11, 5, 7, 2, 1, 4]
    assert find_and_remove_max(example) == [9, 5, 7, 2, 1, 4]

def test_edgecase_find_and_remove_max(input:list[int]) -> None:
    #tests whether the find_and_remove_max function reacts properly when it is given an empty lists(return -1)
    example: list[int] = []
    assert find_and_remove_max(example) == -1

example1:list[int] = [9, 11, 5, 7, 2, 1, 4]
example2: list[int] = []
#calling the test functions
test_output_find_and_remove_max(example1)
test_mutation_find_and_remove_max(example1)
test_edgecase_find_and_remove_max(example2)