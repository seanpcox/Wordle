# @author: seanpcox

__start_title = """-------------------
     W O R D Y
-------------------"""

__win_title = """-------------------
W E L L   D O N E !
-------------------"""

__lose_title = """-------------------
H A R D   L U C K !
-------------------"""

__answer_line = "     ---------"

__instruction_text = "Enter {}-letter guess ({}/{}): "

__invalid_guess_length_text = "Guess must be {} letters"

__invalid_guess_text = "Guess is not in our dictionary"

def get_start_title():
    return __start_title

def get_win_title():
    return __win_title

def get_lose_title():
    return __lose_title

def get_answer_line():
    return __answer_line

def get_instruction(answer_length, guess_number, chances):
    return __instruction_text.format(answer_length, guess_number, chances)

def get_invalid_guess_length(answer_length):
    return __invalid_guess_length_text.format(answer_length)

def get_invalid_guess():
    return __invalid_guess_text