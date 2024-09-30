"""The 3rd challenge question regarding using while loops!"""

__author__ = "730748160"

def num_instances(phrase:str, search_char:str) -> int: 
    current = 0
    count = 0
    
    #iterate through all the letters in the gien phrase and checking to see if it matches, then adding 1 to the counter every time it does#
    while current < len(phrase):
        if phrase[current] == search_char:
            count += 1
            
        current =+ 1
    
    return count
