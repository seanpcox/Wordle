# @author: seanpcox

from src.common.enum.letter_state import LetterState

__text_blue = "\033[34m{}\033[00m"
__text_red = "\033[31m{}\033[00m"
__text_green = "\033[32m{}\033[00m"
__text_orange = "\033[38;2;255;165;0m{}\033[00m"
__text_dark_gray = "\033[90m{}\033[00m"
__text_light_gray = "\033[37m{}\033[00m"
__text_black = "\033[99m{}\033[00m"


def print_blue_line(word):
    print(__text_blue.format(word))


def print_red_line(word):
    print(__text_red.format(word))


def print_green_line(word):
    print(__text_green.format(word))


def print_green_upper(word):
    print(__text_green.format(word.upper()), end="", flush=True)

    
def print_orange_upper(word): 
    print(__text_orange.format(word.upper()), end="", flush=True)

    
def print_dark_gray_upper(word):
    print(__text_dark_gray.format(word.upper()), end="", flush=True)


def print_light_gray_upper(word):
    print(__text_light_gray.format(word.upper()), end="", flush=True)

        
def print_black_upper(word):
    print(__text_black.format(word.upper()), end="", flush=True)


def print_empty_line():
    print()


def print_space():
    print(" ", end="", flush=True)


def print_letter_line(letters, start_spaces=0, is_keyboard=True):
    for i in range(start_spaces):
        print_space()
    
    for i in range(len(letters)):
        if letters[i].state == LetterState.CORRECT:
            print_green_upper(letters[i].value)
        elif letters[i].state == LetterState.WRONG_POSITION:
            print_orange_upper(letters[i].value)
        elif letters[i].state == LetterState.INCORRECT:
            if is_keyboard:
                print_light_gray_upper(letters[i].value)
            else:
                print_dark_gray_upper(letters[i].value)
        elif letters[i].state == LetterState.NOT_ASSIGNED:
            print_black_upper(letters[i].value)
  
        if i < (len(letters) - 1):
            print_space()
            
    print()


def print_guess(guess):
    print_letter_line(guess, 5, False)


def print_keyboard(keyboard):
    print_letter_line(keyboard.get_keyboard_row_1(), 0)
    print_letter_line(keyboard.get_keyboard_row_2(), 1)
    print_letter_line(keyboard.get_keyboard_row_3(), 3)


def print_guess_and_keyboard(guess, keyboard):
    print_guess(guess)
    print_empty_line()
    print_keyboard(keyboard)
