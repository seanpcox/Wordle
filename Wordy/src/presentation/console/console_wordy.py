# @author: seanpcox

import random
from src.resources.text import wordy_text
from src.common.enum.letter_state import LetterState
from src.common.object.letter import Letter
from src.common.object.keyboard import Keyboard
from src.resources.dict.allowed_guesses_set import ALLOWED_GUESSES
from src.resources.dict.allowed_answers_list import ALLOWED_ANSWERS
from src.presentation.console.print.console_printer import ConsolePrinter

printer = ConsolePrinter()
keyboard = Keyboard()
guesses = []

def get_user_input(answer_length, guess_index, chances):
    return input(wordy_text.get_instruction(answer_length, guess_index+1, chances))

def get_allowed_user_guess(answer_length, guess_index, chances):
    guess = get_user_input(answer_length, guess_index, chances)
        
    while(len(guess) != answer_length or guess not in ALLOWED_GUESSES):
        if len(guess) != answer_length:
            printer.print_red_line(wordy_text.get_invalid_guess_length(answer_length))
        else:
            printer.print_red_line(wordy_text.get_invalid_guess())
        
        guess = get_user_input(answer_length, guess_index, chances)
            
    return guess

def process_correct_letters(raw_guess, guess_index, answer_copy):
    for i in range(len(raw_guess)):
        lcLetter = raw_guess[i].lower()
        letterState = LetterState.INCORRECT

        dictLetter = keyboard.get_letter(lcLetter);
        if dictLetter.state == LetterState.NOT_ASSIGNED:
            dictLetter.state = LetterState.INCORRECT

        if lcLetter == answer_copy[i]:
            letterState = LetterState.CORRECT
            
            if dictLetter.state != LetterState.CORRECT:
                dictLetter.state = LetterState.CORRECT
            
            answer_copy[i] = "?"
        
        guesses[guess_index].append(Letter(lcLetter, letterState))

def process_wrong_position_letters(guess_index, answer_copy):
    for i in range(len(guesses[guess_index])):
        letter = guesses[guess_index][i]
        
        if letter.state != LetterState.CORRECT:
            if letter.value in answer_copy:
                dictLetter = keyboard.get_letter(letter.value);
                if dictLetter.state != LetterState.CORRECT:
                    dictLetter.state = LetterState.WRONG_POSITION
                
                guesses[guess_index][i] = Letter(letter.value, LetterState.WRONG_POSITION)
                answer_copy[answer_copy.index(letter.value)] = "?"

def process_guess(raw_guess, guess_index, answer):    
    answer_copy = []
    
    for aInx in range(len(answer)):
        answer_copy.append(answer[aInx])
    
    process_correct_letters(raw_guess, guess_index, answer_copy)    
    
    process_wrong_position_letters(guess_index, answer_copy)

def is_answer_found(guess):
    for letter in guess:
        if letter.state != LetterState.CORRECT:
            return False
        
    return True

def print_result(raw_answer, answer_found):
    printer.print_empty_line()
    
    if answer_found:
        printer.print_green_line(wordy_text.get_win_title())
    else:
        printer.print_red_line(wordy_text.get_lose_title())
            
    printer.print_empty_line()

    for guess_index in range(len(guesses)):
        if answer_found and guess_index != 0 and guess_index == len(guesses)-1:
            printer.print_green_line(wordy_text.get_answer_line())
        printer.print_guess(guesses[guess_index])
    
    if not answer_found:
        answer = []
        for letter in raw_answer:
            answer.append(Letter(letter, LetterState.CORRECT))
        printer.print_red_line(wordy_text.get_answer_line())
        printer.print_guess(answer)

def run_game(raw_answer, chances=6):
    printer.print_blue_line(wordy_text.get_start_title())
    
    answer_found = False
    
    for guess_index in range(chances):
        guesses.append([])
        
        printer.print_empty_line()
        
        raw_guess = get_allowed_user_guess(len(raw_answer), guess_index, chances)
        
        printer.print_empty_line()
        
        process_guess(raw_guess, guess_index, raw_answer)
    
        printer.print_guess_and_keyboard(guesses[guess_index], keyboard)
            
        answer_found = is_answer_found(guesses[guess_index])
        
        if answer_found:
            break

    print_result(raw_answer, answer_found)

run_game("snake",3)