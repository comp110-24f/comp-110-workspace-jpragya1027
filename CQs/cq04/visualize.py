from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

"""practice using imports in python"""

__author__ = "730748160"

#new global variables
x = "123"
y = "abc"

# Call concat using global variables created in visualize
print(concat(x, y))


# Call get_coords using global variables x and y
get_coords(x , y)
