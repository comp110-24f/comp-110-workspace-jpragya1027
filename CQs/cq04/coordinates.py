"""practice using imports in python"""

__author__ = "730748160"

def get_coords(xs: str, ys: str) -> None:
    #Prints the formatted pairs of each character from two input strings. 
    indexx: int = 0
    while indexx < len(xs):# prints for each x coordinate
        indexy: int = 0
        while indexy < len(ys): # prints for each y coordinate
            print( "(" + xs(indexx) + "," + ys(indexy) + ")" )
            indexy += 1 
        indexx += 1

