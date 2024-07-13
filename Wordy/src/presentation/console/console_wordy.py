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

def getUserInput(answer_length, guessIndex, chances):
    return input(wordy_text.getInstruction(answer_length, guessIndex+1, chances))

def getAllowedUserGuess(answer_length, guessIndex, chances):
    guess = getUserInput(answer_length, guessIndex, chances)
        
    while(len(guess) != answer_length or guess not in ALLOWED_GUESSES):
        if len(guess) != answer_length:
            printer.printRedLine(wordy_text.getInvalidGuessLength(answer_length))
        else:
            printer.printRedLine(wordy_text.getInvalidGuess())
        
        guess = getUserInput(answer_length, guessIndex, chances)
            
    return guess

def processCorrectLetters(rawGuess, guessIndex, answerCopy):
    for i in range(len(rawGuess)):
        lcLetter = rawGuess[i].lower()
        letterState = LetterState.INCORRECT

        dictLetter = keyboard.getLetter(lcLetter);
        if dictLetter.state == LetterState.NOT_ASSIGNED:
            dictLetter.state = LetterState.INCORRECT

        if lcLetter == answerCopy[i]:
            letterState = LetterState.CORRECT
            
            if dictLetter.state != LetterState.CORRECT:
                dictLetter.state = LetterState.CORRECT
            
            answerCopy[i] = "?"
        
        guesses[guessIndex].append(Letter(lcLetter, letterState))

def processWrongPositionLetters(guessIndex, answerCopy):
    for i in range(len(guesses[guessIndex])):
        letter = guesses[guessIndex][i]
        
        if letter.state != LetterState.CORRECT:
            if letter.value in answerCopy:
                dictLetter = keyboard.getLetter(letter.value);
                if dictLetter.state != LetterState.CORRECT:
                    dictLetter.state = LetterState.WRONG_POSITION
                
                guesses[guessIndex][i] = Letter(letter.value, LetterState.WRONG_POSITION)
                answerCopy[answerCopy.index(letter.value)] = "?"

def processGuess(rawGuess, guessIndex, answer):    
    answerCopy = []
    
    for aInx in range(len(answer)):
        answerCopy.append(answer[aInx])
    
    processCorrectLetters(rawGuess, guessIndex, answerCopy)    
    
    processWrongPositionLetters(guessIndex, answerCopy)

def isAnswerFound(guess):
    for letter in guess:
        if letter.state != LetterState.CORRECT:
            return False
        
    return True

def runGame(answer, chances=6):
    printer.printBlueLine(wordy_text.getTitle())
    
    for guessIndex in range(chances):
        guesses.append([])
        
        printer.printEmptyLine()
        
        rawGuess = getAllowedUserGuess(len(answer), guessIndex, chances)
        
        printer.printEmptyLine()
        
        processGuess(rawGuess, guessIndex, answer)
    
        printer.printGuessAndKeyboard(guesses[guessIndex], keyboard)
            
        if isAnswerFound(guesses[guessIndex]):
            break

    printer.printEmptyLine()
    for guess in guesses:
        printer.printGuess(guess)

runGame(random.choice(ALLOWED_ANSWERS),3)