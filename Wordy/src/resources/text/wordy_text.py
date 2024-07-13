# @author: seanpcox

# List of all strings we display to the user

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


# Function to return the title of our game
def get_start_title():
    return __start_title


# Function to return the win message of our game
def get_win_title():
    return __win_title


# Function to return the lose message of our game
def get_lose_title():
    return __lose_title


# Function to return the text to display before our answer in the game
def get_answer_line():
    return __answer_line


# Function to return the instruction message for our user, shown during each guess
def get_instruction(answer_length, guess_number, chances):
    return __instruction_text.format(answer_length, guess_number, chances)


# Function to return the error message to our user, explaining the guess word length is incorrect
def get_invalid_guess_length(answer_length):
    return __invalid_guess_length_text.format(answer_length)


# Function to return the error message to our user, explaining the guess word is not in our dictionary
def get_invalid_guess():
    return __invalid_guess_text
