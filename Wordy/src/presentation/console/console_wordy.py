# @author: seanpcox

import random
from src.common.enum.letter_state import LetterState
from src.common.object.letter import Letter
from src.common.object.keyboard import Keyboard
from src.resources.dict.allowed_guesses_set import ALLOWED_GUESSES
from src.resources.dict.allowed_answers_list import ALLOWED_ANSWERS
from src.presentation.console.print.console_printer import ConsolePrinter

def runGame(answer):
    printer = ConsolePrinter()
    
    printer.printBlueLine("-------------------")
    printer.printBlueLine("     W O R D Y     ")
    printer.printBlueLine("-------------------")
    
    instructionText = "Enter 5-letter guess ({}/6): "
    invalidInputText = "Guess must be 5 letters"
    invalidGuessText = "Guess is not in our dictionary"
    
    guessesRaw = ["","","","","",""]
    guessesFormat = [[],[],[],[],[],[]]
    
    keyboard = Keyboard()
    
    correctLetterCount = 0
    
    for gInx in range(6):
        correctLetterCount = 0
        
        answerCopy = []
        
        for aInx in range(5):
            answerCopy.append(answer[aInx])
        
        printer.printEmptyLine()
        
        guessesRaw[gInx] = input(instructionText.format(gInx+1))
        
        while(len(guessesRaw[gInx]) != 5):
            printer.printRedLine(invalidInputText)
            guessesRaw[gInx] = input(instructionText.format(gInx+1))
        
        while(guessesRaw[gInx] not in ALLOWED_GUESSES):
            printer.printRedLine(invalidGuessText)
            guessesRaw[gInx] = input(instructionText.format(gInx+1))
        
        printer.printEmptyLine()
        
        for i in range(len(guessesRaw[gInx])):
            lcLetter = guessesRaw[gInx][i].lower()
            letterState = LetterState.INCORRECT

            dictLetter = keyboard.getLetter(lcLetter);
            if dictLetter.state == LetterState.NOT_ASSIGNED:
                dictLetter.state = LetterState.INCORRECT

            if lcLetter == answerCopy[i]:
                letterState = LetterState.CORRECT
                
                if dictLetter.state != LetterState.CORRECT:
                    dictLetter.state = LetterState.CORRECT
                
                correctLetterCount += 1
                answerCopy[i] = "?"
            
            guessesFormat[gInx].append(Letter(lcLetter, letterState))
            
        for i in range(len(guessesRaw[gInx])):
            letter = guessesFormat[gInx][i]
            
            if letter.state != LetterState.CORRECT:
                if letter.value in answerCopy:
                    dictLetter = keyboard.getLetter(letter.value);
                    if dictLetter.state != LetterState.CORRECT:
                        dictLetter.state = LetterState.WRONG_POSITION
                    
                    guessesFormat[gInx][i] = Letter(letter.value, LetterState.WRONG_POSITION)
                    answerCopy[answerCopy.index(letter.value)] = "?"
    
        printer.printLetterLine(guessesFormat[gInx],5,False)
        printer.printEmptyLine()
        printer.printLetterLine(keyboard.getKeyboardRow1(),0)
        printer.printLetterLine(keyboard.getKeyboardRow2(),1)
        printer.printLetterLine(keyboard.getKeyboardRow3(),3)
        
        if correctLetterCount == 5:
            break
                        
runGame(random.choice(ALLOWED_ANSWERS))