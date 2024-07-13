# @author: seanpcox

__title = """-------------------
     W O R D Y
-------------------"""
__instructionText = "Enter {}-letter guess ({}/{}): "
__invalidGuessLengthText = "Guess must be {} letters"
__invalidGuessText = "Guess is not in our dictionary"

def getTitle():
    return __title

def getInstruction(answer_length, guess_number, chances):
    return __instructionText.format(answer_length, guess_number, chances)

def getInvalidGuessLength(answer_length):
    return __invalidGuessLengthText.format(answer_length)

def getInvalidGuess():
    return __invalidGuessText