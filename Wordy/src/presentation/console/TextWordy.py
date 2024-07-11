# @author: seanpcox

import random
from src.common.enum.letter_state import LetterState
from src.common.letter import Letter
from src.resources.dict.allowed_guesses_set import ALLOWED_GUESSES
from src.resources.dict.allowed_answers_list import ALLOWED_ANSWERS

def printBlueLine(word):
    print("\033[34m{}\033[00m".format(word))

def printRedLine(word):
    print("\033[31m{}\033[00m".format(word))

def printGreenUpper(word):
    print("\033[32m{}\033[00m".format(word.upper()), end="", flush=True)
    
def printYellowUpper(word): 
    print("\033[38;2;255;165;0m{}\033[00m".format(word.upper()), end="", flush=True)
    
def printGrayUpper(word):
    print("\033[90m{}\033[00m".format(word.upper()), end="", flush=True)

def printSpace():
    print(" ", end="", flush=True)

def printGuess(letters):
    for i in range(len(letters)):
        if letters[i].state == LetterState.CORRECT:
            printGreenUpper(letters[i].value)
        elif letters[i].state == LetterState.WRONG_POSITION:
            printYellowUpper(letters[i].value)
        elif letters[i].state == LetterState.INCORRECT:
            printGrayUpper(letters[i].value)
  
        if i < (len(letters) - 1):
            printSpace()
            
    print()

def runGame(answer):
    printBlueLine("W O R D Y")
    printBlueLine("---------")
    
    instructionText = "Enter 5-letter guess ({}/6): "
    invalidInputText = "Guess must be 5 letters"
    invalidGuessText = "Guess is not in our dictionary"
    
    guessesRaw = ["","","","","",""]
    guessesFormat = [[],[],[],[],[],[]]
    
    correctLetterCount = 0
    
    for gInx in range(6):
        correctLetterCount = 0
        
        answerCopy = []
        
        for aInx in range(5):
            answerCopy.append(answer[aInx])
        
        guessesRaw[gInx] = input(instructionText.format(gInx+1))
        
        while(len(guessesRaw[gInx]) != 5):
            printRedLine(invalidInputText)
            guessesRaw[gInx] = input(instructionText.format(gInx+1))
        
        while(guessesRaw[gInx] not in ALLOWED_GUESSES):
            printRedLine(invalidGuessText)
            guessesRaw[gInx] = input(instructionText.format(gInx+1))
        
        for i in range(len(guessesRaw[gInx])):
            lcLetter = guessesRaw[gInx][i].lower()
            letterState = LetterState.INCORRECT
            
            if lcLetter == answerCopy[i]:
                letterState = LetterState.CORRECT
                correctLetterCount += 1
                answerCopy[i] = "?"
            
            guessesFormat[gInx].append(Letter(lcLetter, letterState))
            
        for i in range(len(guessesRaw[gInx])):
            letter = guessesFormat[gInx][i]
            
            if letter.state != LetterState.CORRECT:
                if letter.value in answerCopy:
                    guessesFormat[gInx][i] = Letter(letter.value, LetterState.WRONG_POSITION)
                    answerCopy[answerCopy.index(letter.value)] = "?"
    
        printGuess(guessesFormat[gInx])
        
        if correctLetterCount == 5:
            break
                        
runGame(random.choice(ALLOWED_ANSWERS))