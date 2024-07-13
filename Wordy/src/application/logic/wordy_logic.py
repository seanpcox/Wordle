# @author: seanpcox

from src.resources.dict.allowed_guesses_set import ALLOWED_GUESSES
from src.common.enum.letter_state import LetterState
from src.common.object.letter import Letter


def is_guess_allowed(raw_guess, answer_length):
    raw_guess = raw_guess.lower()
    return len(raw_guess) == answer_length and raw_guess in ALLOWED_GUESSES


def is_answer_found(guess):
    for letter in guess:
        if letter.state != LetterState.CORRECT:
            return False
        
    return True


def process_guess(raw_guess, guesses, guess_index, answer, keyboard):
    guesses.append([])
      
    answer_copy = []
    
    for aInx in range(len(answer)):
        answer_copy.append(answer[aInx])
    
    __process_correct_letters(raw_guess, guesses, guess_index, answer_copy, keyboard)    
    
    __process_wrong_position_letters(guesses, guess_index, answer_copy, keyboard)


def __process_correct_letters(raw_guess, guesses, guess_index, answer_copy, keyboard):
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


def __process_wrong_position_letters(guesses, guess_index, answer_copy, keyboard):
    for i in range(len(guesses[guess_index])):
        letter = guesses[guess_index][i]
        
        if letter.state != LetterState.CORRECT:
            if letter.value in answer_copy:
                dictLetter = keyboard.get_letter(letter.value);
                if dictLetter.state != LetterState.CORRECT:
                    dictLetter.state = LetterState.WRONG_POSITION
                
                guesses[guess_index][i] = Letter(letter.value, LetterState.WRONG_POSITION)
                answer_copy[answer_copy.index(letter.value)] = "?"
 
