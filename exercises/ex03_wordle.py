"""coding wordle in our 4th excersise!"""

__author__ = "730748160"

def input_guess(secret_length:int) -> str:
    #ask user for word input and checks to see if it is the correct length
    """ask user for word input and checks to see if it is the correct length"""
    input_word: str = input(f"Enter a {secret_length} character word: ")
    while len(input_word) != secret_length:
        if len(input_word) != secret_length:
            input_word = input(f"That wasn't {secret_length} chars! Try again: ")
    return input_word 

def contains_char(input_guess: str, character_check: str) -> bool:
    #test each index of the guessed word(input_guess) with a character guess
    assert len(character_check) == 1
    index:int = 0
    while index < len(input_guess):
         if input_guess[index] == character_check:
              return True
         index += 1
    return False


def emojified(guess:str, secret:str) -> str:
    assert len(guess) == len(secret)
    #Green box: Character is in the correct position. 
    #Yellow box: Character is in the secret word but the wrong position.
    #White box: Character is not in the secret word.

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    #compare two strings of equal length—-the first being the user’s guess and the second being the secret word. 
    """compare two strings of equal length—-the first being the user’s guess and the second being the secret word."""
    index:int = 0
    emojis: str = ""
    while index < len(guess):
        if guess[index] == secret[index]:
            emojis += GREEN_BOX
            index += 1
        elif contains_char(secret, guess[index]) == True:
            emojis = emojis + YELLOW_BOX
            index += 1
        else:
            emojis = emojis + WHITE_BOX
            index += 1
    return emojis

def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    #The entrypoint of the program and main game loop.
    index:int = 0
    number_of_turns:int = 0
    while number_of_turns < 6:
        print(f"=== Turn {number_of_turns + 1}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        number_of_turns += 1
        index += 1
        if guess == secret:
            print(f"You won in {number_of_turns}/6 turns!")
            number_of_turns = 7
        if number_of_turns == 6:
            print("X/6 - Sorry, try again tomorrow!")



if __name__ == "__main__":
    main(secret = "codes")
                    
