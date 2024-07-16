# @author: seanpcox

# List of all strings we display to the user

# UI Wordy strings

__ui_title = "W O R D Y"

__new_button_text = "New"

__delete_button_text = "Delete"

__enter_button_text = "Enter"

__game_won_text = ["Genius!", "Magnificent!", "Impressive!", "Splendid!", "Great!", "Phew!"]

# Text Wordy strings

__start_title = """-------------------
     W O R D Y
-------------------"""

__win_title = """-------------------
W E L L   D O N E !
-------------------"""

__lose_title = """-------------------
H A R D   L U C K !
-------------------"""

__instruction_text = "Enter {}-letter guess ({}/{}): "

__answer_line = "     ---------"

# Common Wordy strings

__ui_instruction_text = "Guess the {} letter word"

__invalid_guess_length_text = "Guess must be {} letters"

__invalid_guess_text = "Guess is not in our dictionary"

__invalid_answer_input = "Supplied answer '{}' is not in our 5 letter answers dictionary"

__invalid_chances_input = "Supplied chances parameter '{}' is not a valid integer between {} and {}"


# Function to return the UI title of our game
def get_ui_title():
    return __ui_title


# Function to return the UI new button text
def get_new_button():
    return __new_button_text


# Function to return the UI delete button text
def get_delete_button():
    return __delete_button_text


# Function to return the UI delete button text
def get_enter_button():
    return __enter_button_text


# Function to get UI win game text
def get_game_won(guess_row, chances):
    # We allowed user defined number of guesses so choose last win entry guess_attempts greater than number of win text entries
    if guess_row >= len(__game_won_text):
        # If we guessed on the last attempt then do last win text entry
        if(guess_row == chances - 1):
            guess_row = len(__game_won_text) - 1
        # Else do second last win guess entry
        else:
            guess_row = len(__game_won_text) - 2
    
    return __game_won_text[guess_row]


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


# Function to return the instruction message for our user, shown at the start of a UI game
def get_ui_instruction(answer_length):
    return __ui_instruction_text.format(answer_length)

# Function to return the instruction message for our user, shown during each guess
def get_instruction(answer_length, guess_number, chances):
    return __instruction_text.format(answer_length, guess_number, chances)


# Function to return the error message to our user, explaining the guess word length is incorrect
def get_invalid_guess_length(answer_length):
    return __invalid_guess_length_text.format(answer_length)


# Function to return the error message to our user, explaining the guess word is not in our dictionary
def get_invalid_guess():
    return __invalid_guess_text


# Function to return the error message to out user, explaining that their supplied answer is not in our answers dictionary
def get_invalid_answer_input(input_answer):
    return __invalid_answer_input.format(input_answer)


# Function to return the error message to our user, explaining that their supplied chances number is out of range
def get_invalid_chances_input(input_chances, min_chances, max_chances):
    return __invalid_chances_input.format(input_chances, min_chances, max_chances)

