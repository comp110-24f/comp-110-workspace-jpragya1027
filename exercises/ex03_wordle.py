"""coding wordle in our 4th excersise!"""

__author__ = "730748160"

def input_guess(secret_length:str) -> str:
    #ask user for word input and checks to see if it is the correct length
    """ask user for word input and checks to see if it is the correct length"""
    input_word: str = input(f"Enter a {secret_length} character word:")
    while len(input_word) != secret_length
    if len(input_word) != secret_length:
        input_word = input(f"That wasn't a {secret_length} + character word. Try Again:")
    else return input_word 

def contains_char(input_guess, character_check: str) -> bool:
    #test each index of the guessed word(input_guess) with a character guess
    assert len(character_check) == 1
    index:int = 0
    while 

def emojified(guess:str, secret:str) -> str:
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    #compare two strings of equal length—-the first being the user’s guess and the second being the secret word. 
    """compare two strings of equal length—-the first being the user’s guess and the second being the secret word."""
    indexGuess:int = 0
    indexSecret: int = 0
    while indexGuess < len(input_word):
        if guess[index] == secret[index]:
            print(GREEN_BOX)
            index += 1
        elif:
            while indexSecret < len(input_word):
                if guess[indexGuess] == secret[indexSecret]:
                    print(YELLOW_BOX)
                    indexSecret += 1
                else
                    print(WHITE_BOX)

 def main(secret: str) -> None:
        """The entrypoint of the program and main game loop."""
        #The entrypoint of the program and main game loop.
        number_of_turns:int = 0
        while number_of_turns <= 6:
            print(f"=== Turn {number_of_turns}/6 ===")
            input_guess()
            emojified(input_guess(), secret)
                    
