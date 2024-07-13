# @author: seanpcox

import random
from src.resources.dict.allowed_answers_list import ALLOWED_ANSWERS
from src.resources.dict.allowed_guesses_set import ALLOWED_GUESSES
from src.common.enum.letter_state import LetterState
from src.common.object.letter import Letter


# Return a random answer from our allowed answers dictionary
def get_random_answer():
    return random.choice(ALLOWED_ANSWERS)


# Test to ensure a guess is allowed, of the right length and in our allowed guesses dictionary
def is_guess_allowed(raw_guess, answer_length):
    # Cope with upper case and mixed cases guesses, our dictionary words are all in lower case
    raw_guess = raw_guess.lower()
    # perform our test
    return len(raw_guess) == answer_length and raw_guess in ALLOWED_GUESSES


# Test to see if our guess consists of all correct letters
def is_answer_found(guess):
    for letter in guess:
        if letter.state != LetterState.CORRECT:
            return False
        
    return True


# Process our guess to see how many letters are correct and in the correct the place
def process_guess(raw_guess, guesses, guess_index, answer, keyboard):
    # Add a new entry to our list of guesses
    guesses.append([])

    # Create a copy of our answer in list format, this allows us to alter data without altering the answer
    answer_copy = []
    
    for aInx in range(len(answer)):
        answer_copy.append(answer[aInx])
    
    # First we need to check for correct letters in the right place
    # We may have cases where there are duplicate letters where one is in the correct place and one incorrect
    __process_correct_letters(raw_guess, guesses, guess_index, answer_copy, keyboard)    
    
    # After we have marked all correct letters in the right place we can check for correct letters in the wrong place
    __process_wrong_position_letters(guesses, guess_index, answer_copy, keyboard)


# Check for letters in the correct place
def __process_correct_letters(raw_guess, guesses, guess_index, answer_copy, keyboard):
    # Loop through each letter in our guess
    for i in range(len(raw_guess)):
        # Cope with upper case and mixed cases guesses, our dictionary words are all in lower case
        lcLetter = raw_guess[i].lower()
        # Assume a guess letter state is incorrect until proven otherwise
        letterState = LetterState.INCORRECT

        # Here we update our keyboard display to also assume an incorrect letter, but only if unassigned previously
        dictLetter = keyboard.get_letter(lcLetter);
        if dictLetter.state == LetterState.NOT_ASSIGNED:
            dictLetter.state = LetterState.INCORRECT

        # If the guess letter is correct and in the same place we mark the guess letter state as correct
        if lcLetter == answer_copy[i]:
            letterState = LetterState.CORRECT
            
            # Here we update our keyboard display to mark a correct letter, only update if not already marked correct
            if dictLetter.state != LetterState.CORRECT:
                dictLetter.state = LetterState.CORRECT
            
            # Remove this letter from the answer copy so we do not check for this specific letter and position again
            answer_copy[i] = "?"
        
        # Add our guess letter to our guess letter list with its state marked
        guesses[guess_index].append(Letter(lcLetter, letterState))


# Check for letters in the incorrect place
def __process_wrong_position_letters(guesses, guess_index, answer_copy, keyboard):
    # Loop through each letter in our guess
    for i in range(len(guesses[guess_index])):
        letter = guesses[guess_index][i]
        
        # We only process the guess letter if it is not already marked correct
        if letter.state != LetterState.CORRECT:
            # Here we are testing for a correct letter but in the wrong place so we check all items still in the answer copy
            if letter.value in answer_copy:
                # Here we update our keyboard display to mark a letter in an incorrect position, do not override if already marked correct
                dictLetter = keyboard.get_letter(letter.value);
                if dictLetter.state != LetterState.CORRECT:
                    dictLetter.state = LetterState.WRONG_POSITION
                
                # Update our guess letter in our guess letter list with its new state marked
                guesses[guess_index][i] = Letter(letter.value, LetterState.WRONG_POSITION)
                
                # Remove this letter from the answer copy so we do not check for this specific letter and position again
                # We need to retrieve the index as we checked all letters left in the answer copy
                answer_copy[answer_copy.index(letter.value)] = "?"
 
