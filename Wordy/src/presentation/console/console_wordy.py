# @author: seanpcox

import random
from src.resources.text import wordy_text
from src.common.enum.letter_state import LetterState
from src.common.object.letter import Letter
from src.common.object.keyboard import Keyboard
from src.application.logic import wordy_logic
from src.resources.dict.allowed_answers_list import ALLOWED_ANSWERS
from src.presentation.console.print import console_printer as printer


def __get_user_input(answer_length, guess_index, chances):
    return input(wordy_text.get_instruction(answer_length, guess_index + 1, chances))


def __get_allowed_user_guess(answer_length, guess_index, chances):
    raw_guess = __get_user_input(answer_length, guess_index, chances)
        
    while(not wordy_logic.is_guess_allowed(raw_guess, answer_length)):
        if len(raw_guess) != answer_length:
            printer.print_red_line(wordy_text.get_invalid_guess_length(answer_length))
        else:
            printer.print_red_line(wordy_text.get_invalid_guess())
        
        raw_guess = __get_user_input(answer_length, guess_index, chances)
            
    return raw_guess


def __print_result(guesses, raw_answer, answer_found):
    printer.print_empty_line()
    
    if answer_found:
        printer.print_green_line(wordy_text.get_win_title())
    else:
        printer.print_red_line(wordy_text.get_lose_title())
            
    printer.print_empty_line()

    for guess_index in range(len(guesses)):
        if answer_found and guess_index != 0 and guess_index == len(guesses) - 1:
            printer.print_green_line(wordy_text.get_answer_line())
        printer.print_guess(guesses[guess_index])
    
    if not answer_found:
        answer = []
        for letter in raw_answer:
            answer.append(Letter(letter, LetterState.CORRECT))
        printer.print_red_line(wordy_text.get_answer_line())
        printer.print_guess(answer)


def run_game(raw_answer, chances=6):
    keyboard = Keyboard()
    guesses = []
    answer_found = False
    
    printer.print_blue_line(wordy_text.get_start_title())
    
    for guess_index in range(chances):
        printer.print_empty_line()
        
        raw_guess = __get_allowed_user_guess(len(raw_answer), guess_index, chances)
        
        printer.print_empty_line()
        
        wordy_logic.process_guess(raw_guess, guesses, guess_index, raw_answer, keyboard)
    
        printer.print_guess_and_keyboard(guesses[guess_index], keyboard)
            
        answer_found = wordy_logic.is_answer_found(guesses[guess_index])
        
        if answer_found:
            break

    __print_result(guesses, raw_answer, answer_found)


run_game(random.choice(ALLOWED_ANSWERS), 6)
