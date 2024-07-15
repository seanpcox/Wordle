# @author: seanpcox

from time import sleep
from src.common.enum.letter_state import LetterState

# List of ASCII colors used in our program
__text_blue = "\033[34m{}\033[00m"
__text_red = "\033[31m{}\033[00m"
__text_green = "\033[32m{}\033[00m"
__text_orange = "\033[38;2;255;165;0m{}\033[00m"
__text_dark_gray = "\033[90m{}\033[00m"
__text_light_gray = "\033[37m{}\033[00m"
__text_black = "\033[99m{}\033[00m"


# Print a line of text in blue
def print_blue_line(word):
    print(__text_blue.format(word))


# Print a line of text in red
def print_red_line(word):
    print(__text_red.format(word))


# Print a line of text in green
def print_green_line(word):
    print(__text_green.format(word))


# Print a letter or word in green on the existing line
def print_green_upper(word):
    print(__text_green.format(word.upper()), end="", flush=True)


# Print a letter or word in orange on the existing line   
def print_orange_upper(word): 
    print(__text_orange.format(word.upper()), end="", flush=True)


# Print a letter or word in dark gray on the existing line    
def print_dark_gray_upper(word):
    print(__text_dark_gray.format(word.upper()), end="", flush=True)


# Print a letter or word in light gray on the existing line
def print_light_gray_upper(word):
    print(__text_light_gray.format(word.upper()), end="", flush=True)


# Print a letter or word in black on the existing line        
def print_black_upper(word):
    print(__text_black.format(word.upper()), end="", flush=True)


# Print an empty line
def print_empty_line():
    print()


# Print a space on the existing line
def print_space():
    print(" ", end="", flush=True)


# Print a list of letters with a space between them marked with the color representing their status compared to the answer
def print_letter_line(letters, start_spaces=0, is_keyboard=True, sleep_seconds=0):
    for i in range(start_spaces):
        print_space()
    
    for i in range(len(letters)):
        # We can add some sleep time if we want to reveal each letter at a time
        sleep(sleep_seconds)
        
        # A letter in the correct position is printed in green
        if letters[i].state == LetterState.CORRECT:
            print_green_upper(letters[i].value)
        # A letter in an incorrect position is printed in orange
        elif letters[i].state == LetterState.WRONG_POSITION:
            print_orange_upper(letters[i].value)
        # A letter not in out answer is printed in gray
        elif letters[i].state == LetterState.INCORRECT:
            # We use a light gray for our keyboard to better distinguish from black letters
            if is_keyboard:
                print_light_gray_upper(letters[i].value)
            # We use a dark gray in our guess display for better visibility
            else:
                print_dark_gray_upper(letters[i].value)
        # A letter not yet included in a guess is marked in black, this only applies to display keyboard letters
        elif letters[i].state == LetterState.NOT_ASSIGNED:
            print_black_upper(letters[i].value)
  
        if i < (len(letters) - 1):
            print_space()
            
    print_empty_line()


# Print a guess line with 5 spaces preceding it
def print_guess(guess, sleep_seconds=0):
    print_letter_line(guess, 5, False, sleep_seconds)


# Print all three rows of our keyboard
def print_keyboard(keyboard):
    # No spaces in our first line
    print_letter_line(keyboard.get_keyboard_row_1(), 0)
    # One spaces in our second line to center it in the display against the first, it has less letters
    print_letter_line(keyboard.get_keyboard_row_2(), 1)
    # Three spaces in our third line to center it in the display against the first, it has less letters
    print_letter_line(keyboard.get_keyboard_row_3(), 3)


# Print our guess line followed by a keyboard line
def print_guess_and_keyboard(guess, keyboard, sleep_seconds=0):
    print_guess(guess, sleep_seconds)
    print_empty_line()
    print_keyboard(keyboard)
