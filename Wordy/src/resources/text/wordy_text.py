# @author: seanpcox

__instructionText = "Enter 5-letter guess ({}/6): "
__invalidInputText = "Guess must be 5 letters"
__invalidGuessText = "Guess is not in our dictionary"

def getInstruction(guess_number):
    return __instructionText.format(guess_number)

def getInvalidLength():
    return __invalidInputText

def getInvalidGuess():
    return __invalidGuessText