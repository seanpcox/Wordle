# @author: seanpcox

__start_title = """-------------------
     W O R D Y
-------------------"""
__instructionText = "Enter {}-letter guess ({}/{}): "
__invalidGuessLengthText = "Guess must be {} letters"
__invalidGuessText = "Guess is not in our dictionary"

__win_title = """-------------------
W E L L   D O N E !
-------------------"""

__lose_title = """-------------------
H A R D   L U C K !
-------------------"""

def getStartTitle():
    return __start_title

def getWinTitle():
    return __win_title

def getLoseTitle():
    return __lose_title

def getInstruction(answer_length, guess_number, chances):
    return __instructionText.format(answer_length, guess_number, chances)

def getInvalidGuessLength(answer_length):
    return __invalidGuessLengthText.format(answer_length)

def getInvalidGuess():
    return __invalidGuessText