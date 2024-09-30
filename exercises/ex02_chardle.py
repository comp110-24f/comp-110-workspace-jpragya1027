"""An excersise helping me practice with while loops and conditional statements to build a game like wordle!"""

__author__ = "730748160"

def input_word() -> str:
    word:str = input("Enter a 5-character word:")
    if len(word) != 5:
        exit()
        print("Error: Word must contain 5 characters.")
    else return word

def input_letter() -> str:
    letter:str = input("Enter a single character:")
    if len(letter) != 1:
        exit()
        print("Character must be a single character.")
    else return letter

def contains_char(word=input_word(), letter=input_letter()) -> None:
    """Check if the letter matches each letter in the word, then if it does, add one to the counter variable"""
    matching_character_count: int = 0
    print("Searching for " + letter + " in " + word)
    #Using conditionals to check if each letter of the word is equal to the letter using the index of the word
    #When it is equal, update matching_character_count by 1 to see how many times the letter is in the word
    if word[0] == letter: 
       print(letter + " found at index 0")
       matching_character_count = matching_character_count + 1
    if word[1] == letter: 
       print(letter + " found at index 1")
       matching_character_count = matching_character_count + 1
    if word[2] == letter: 
       print(letter + " found at index 2")
       matching_character_count = matching_character_count + 1
    if word[3] == letter: 
       print(letter + " found at index 3")
       matching_character_count = matching_character_count + 1
    if word[4] == letter: 
       print(letter + " found at index 4")
       matching_character_count = matching_character_count + 1

    #Used conditionals and matching_character_count to print how many times the letter is in the word
    if matching_character_count == 0: 
       print("No instances of " + letter + " found in " + word)
    elif matching_character_count == 1: 
       print("1 instance of " + letter + " found in " + word) 
    else: 
       print(str(matching_character_count) + " instances of " + letter + " found in " + word) 
       #Converted matching_character_count from int to string to print

def main() -> None:
   contains_char(word=input_word(), letter=input_letter())

if __name__ == "__main__":
    main()

