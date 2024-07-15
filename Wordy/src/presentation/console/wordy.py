# @author: seanpcox

from src.resources.text import wordy_text
from src.common.enum.letter_state import LetterState
from src.common.object.letter import Letter
from src.common.object.keyboard import Keyboard
from src.application.logic import wordy_logic
from src.presentation.console.print import console_printer as printer


# Function to get input from the user from the console
def __get_user_input(answer_length, guess_index, chances):
    return input(wordy_text.get_instruction(answer_length, guess_index + 1, chances))


# Function to get an allowed guess from the user, guess must be of correct length and in our dictionary
def __get_allowed_user_guess(answer_length, guess_index, chances):
    # Get user input guess
    raw_guess = __get_user_input(answer_length, guess_index, chances)
    
    # Test the guess meets our conditions otherwise display an error and prompt the user for a new guess
    while(not wordy_logic.is_guess_allowed(raw_guess, answer_length)):
        # Display error that the guess is of the wrong length
        if len(raw_guess) != answer_length:
            printer.print_red_line(wordy_text.get_invalid_guess_length(answer_length))
        # Display error that the guess is not included in our allowed guesses dictionary
        else:
            printer.print_red_line(wordy_text.get_invalid_guess())
        
        # Re-prompt the user for a new guess
        raw_guess = __get_user_input(answer_length, guess_index, chances)
    
    # Return the users guess
    return raw_guess


# Function to print the result at the end of the games, this includes all their guesses plus the answer (even if they did not guess it)
def __print_result(guesses, raw_answer, answer_found):
    printer.print_empty_line()
    
    # If the user guessed correctly in the allowed chances print the win title
    if answer_found:
        printer.print_green_line(wordy_text.get_win_title())
    # If the user did not guess correctly in the allowed chances print the lose title
    else:
        printer.print_red_line(wordy_text.get_lose_title())
            
    printer.print_empty_line()

    # Print each guess the user attempted in order
    for guess_index in range(len(guesses)):
        # If we found the answer and this was the last guess print a green line above it
        if answer_found and guess_index != 0 and guess_index == len(guesses) - 1:
            printer.print_green_line(wordy_text.get_answer_line())
        # Print the guess
        printer.print_guess(guesses[guess_index])
    
    # If we did not find the answer, print the answer after all user guesses precedded by a red line
    if not answer_found:
        # We must create a new "guess" to display the answer
        answer = []
        for letter in raw_answer:
            answer.append(Letter(letter, LetterState.CORRECT))
        # Print a red line
        printer.print_red_line(wordy_text.get_answer_line())
        # Print the answer
        printer.print_guess(answer)


# Public function to start our game, optional methods are the number of changes allowed and the answer
# By default we allow 6 guesses and choose an answer at random from our allowed answers list
def wordy(chances=6, raw_answer=wordy_logic.get_random_answer()):
    # Create our display keyboard, this shows the user all previously tried, wrong position, and correct letters
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


# Launch Wordy with defaults, 6 chances and random word selected from our 5-letter dictionary    
# Note: Code can cope with words of N length, but currently we only have 5-letter dictionaries included  
wordy()

# Launch Word with custom parameters, 4 chances and a chosen word
# wordy(4, "snake")
