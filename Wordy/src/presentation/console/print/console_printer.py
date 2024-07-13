# @author: seanpcox

from src.common.enum.letter_state import LetterState

class ConsolePrinter:
    
    __text_blue = "\033[34m{}\033[00m"
    __text_red = "\033[31m{}\033[00m"
    __text_green ="\033[32m{}\033[00m"
    __text_orange = "\033[38;2;255;165;0m{}\033[00m"
    __text_dark_gray = "\033[90m{}\033[00m"
    __text_light_gray = "\033[37m{}\033[00m"
    __text_black = "\033[99m{}\033[00m"
    
    def __init__(self):
        return
    
    def print_blue_line(self, word):
        print(self.__text_blue.format(word))
    
    def print_red_line(self, word):
        print(self.__text_red.format(word))
    
    def print_green_line(self, word):
        print(self.__text_green.format(word))
    
    def print_green_upper(self, word):
        print(self.__text_green.format(word.upper()), end="", flush=True)
        
    def print_orange_upper(self, word): 
        print(self.__text_orange.format(word.upper()), end="", flush=True)
        
    def print_dark_gray_upper(self, word):
        print(self.__text_dark_gray.format(word.upper()), end="", flush=True)
    
    def print_light_gray_upper(self, word):
        print(self.__text_light_gray.format(word.upper()), end="", flush=True)
            
    def print_black_upper(self, word):
        print(self.__text_black.format(word.upper()), end="", flush=True)
    
    def print_empty_line(self):
        print()
    
    def print_space(self):
        print(" ", end="", flush=True)
    
    def print_letter_line(self, letters, start_spaces=0, is_keyboard=True):
        for i in range(start_spaces):
            self.print_space()
        
        for i in range(len(letters)):
            if letters[i].state == LetterState.CORRECT:
                self.print_green_upper(letters[i].value)
            elif letters[i].state == LetterState.WRONG_POSITION:
                self.print_orange_upper(letters[i].value)
            elif letters[i].state == LetterState.INCORRECT:
                if is_keyboard:
                    self.print_light_gray_upper(letters[i].value)
                else:
                    self.print_dark_gray_upper(letters[i].value)
            elif letters[i].state == LetterState.NOT_ASSIGNED:
                self.print_black_upper(letters[i].value)
      
            if i < (len(letters) - 1):
                self.print_space()
                
        print()
    
    def print_guess(self, guess):
        self.print_letter_line(guess,5,False)

    def print_keyboard(self, keyboard):
        self.print_letter_line(keyboard.get_keyboard_row_1(),0)
        self.print_letter_line(keyboard.get_keyboard_row_2(),1)
        self.print_letter_line(keyboard.get_keyboard_row_3(),3)

    def print_guess_and_keyboard(self, guess, keyboard):
        self.print_guess(guess)
        self.print_empty_line()
        self.print_keyboard(keyboard)
