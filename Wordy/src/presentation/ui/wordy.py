# @author: seanpcox

import tkinter as tk
import sys
from time import sleep
from src.application.logic import wordy_logic
from src.common.enum.letter_state import LetterState
from src.common.object.keyboard import Keyboard
from src.resources.text import wordy_text


class Wordy(tk.Tk):

    def __init__(self, raw_answer=wordy_logic.get_random_answer(), chances=6):
        # Validate initialization parameters, as may be used supplied
        if not wordy_logic.are_init_parameters_valid(raw_answer, chances):
            # Exit the program if inputs are invalid so we do not try to launch the application
            sys.exit(-1)
        
        # Set our window title
        super(self.__class__, self).__init__()
        self.title(wordy_text.get_ui_title())
        
        # Set some global variables
        self.raw_answer = raw_answer
        self.answer_length = len(raw_answer)
        self.chances = int(chances) # Chances will be a string number if user supplied so update
        self.guesses = []
        
        # Set our window Size, width is fixed and height depends on number of chances allowed
        screen_width = 494
        screen_height = 160 + (self.chances * 30)
        self.geometry("{}x{}".format(screen_width, screen_height))

        # Create our guess list at the top of the application
        self.guess_labels = []
        self.guess_row = 0
        self.guess_column = 0
        py = self.__create_guess_labels()
        
        # Create out status label to display information to our user
        py = self.__create_status_label(py)
        
        # Create our display keyboard at the bottom of the application
        self.keyboard = Keyboard()
        self.keyboard_buttons = {}
        self.__create_keyboard(py)
        
        # Bind the user's physical keyboard to our application
        self.bind("<Key>", self.__key_handler)

    # Function to process a user guess
    def __process_guess(self):
        # Get the guess string by combining the individual letters
        raw_guess = ""
        
        for column in range(self.answer_length):
            raw_guess += self.guess_labels[self.guess_row][column]["text"]
        
        # Test is the guess is allowed i.e. correct length and in our allowed guesses dictionary
        is_allowed_guess = wordy_logic.is_guess_allowed(raw_guess, self.answer_length)
        
        # If our guess is not allowed then return and do not move to the next guess or end of game
        if not is_allowed_guess:
            self.__update_status_label(wordy_text.get_invalid_guess(), "orange")
            return False
        
        # Process our guess to determine which letters are correct, in the wrong place, or not in the answer
        wordy_logic.process_guess(raw_guess, self.guesses, self.guess_row, self.raw_answer, self.keyboard)
        
        # Update our guess labels in the current guess row to indicate each letter's status
        for column in range(self.answer_length):
            
            # Retrieve the letter at the column specified from our processed guess
            guess_letter = self.guesses[self.guess_row][column]
            
            # If the letter is not in the answer, update the corresponding guess label's and keyboard key coloring to indicate
            # Note we update the keyboard button foreground as MacOS doesn't support changing button background color with Tkinter
            if guess_letter.state == LetterState.INCORRECT:
                self.guess_labels[self.guess_row][column]["bg"] = "darkgray"
                self.keyboard_buttons[guess_letter.value.upper()]["fg"] = "lightgray"
            # We use a dark gray in our guess display for better visibility
            # If the letter is not in the answer, update the corresponding guess label's and keyboard key coloring to indicate
            elif guess_letter.state == LetterState.WRONG_POSITION:
                self.guess_labels[self.guess_row][column]["bg"] = "goldenrod"
                self.keyboard_buttons[guess_letter.value.upper()]["fg"] = "goldenrod"
            # If the letter is not in the answer, update the corresponding guess label's and keyboard key coloring to indicate
            elif guess_letter.state == LetterState.CORRECT:
                self.guess_labels[self.guess_row][column]["bg"] = "medium sea green"
                self.keyboard_buttons[guess_letter.value.upper()]["fg"] = "medium sea green"
            
            # Regardless of guessed letter state all labels in the current guess have their foreground updated    
            self.guess_labels[self.guess_row][column]["fg"] = "white"
            
            # We add some sleep time to reveal each letter at a time
            sleep(0.3)
            self.update()
        
        # Check if our current guess was the answer
        is_answer_found = wordy_logic.is_answer_found(self.guesses[self.guess_row])
        
        if is_answer_found:
            self.__game_over(True)
            return False
        
        # We had a valid guess but did not find the answer, return True to indicate we can move to next guess
        return True
    
    # Function to execute when the current game has ended
    def __game_over(self, is_win):
        # Disable all buttons
        self.__set_keyboard_buttons_enabled(False)
        self.__set_delete_button_enabled(False)
        self.__set_enter_button_enabled(False)
        
        # Update the status label to either indicate varying levels of congratulations (based on number of guesses taken)
        if is_win:
            self.__update_status_label(wordy_text.get_game_won(self.guess_row, self.chances), "lightgreen")
        # Else update the status label to display the answer the used failed to guess
        else:
            self.__update_status_label(self.raw_answer.upper(), "coral1")
    
    # Function to accept input from user's physical keyboard
    def __key_handler(self, event):
        letter_upper = event.char.upper()
        
        if letter_upper not in self.keyboard_buttons:
            if event.keysym == "Return":
                self.__enter_press()
            if event.keysym == "BackSpace":
                self.__delete_press()
            return
        
        self.__keyboard_press(event.char.upper())
    
    # Function to execute a Keyboard Letter action
    def __keyboard_press(self, letter):
        # Clear the status label
        self.__update_status_label()
        
        # If the user has already reached the letter length for a guess then return
        if self.guess_column == self.answer_length:
            return
        
        # Update the container for the current position in the current guess line with the user's letter selection
        self.guess_labels[self.guess_row][self.guess_column]["text"] = letter
        
        # Move the column index to the next position
        self.guess_column += 1
        
        # If the user has entered one letter then we can enable the Delete button
        if self.guess_column == 1:
            self.__set_delete_button_enabled(True)
        
        # If the user has entered the last letter for a guess then enable the Enter button and disable the Keyboard
        if self.guess_column == self.answer_length:
            self.__set_enter_button_enabled(True)
            self.__set_keyboard_buttons_enabled(False)
        
    # Function to execute the Enter button action
    def __enter_press(self):
        # Clear the status label
        self.__update_status_label()
        
        # If there are not enough letters yet for a guess return
        if self.guess_column < self.answer_length:
            # Update our status label to indicate not enough letters have been typed
            self.__update_status_label(wordy_text.get_invalid_guess_length(self.answer_length), "orange")
            return 
        
        # Process our users current guess
        is_continue = self.__process_guess()
        
        # If our guess is not allowed or we have found the answer do not proceed and return
        if not is_continue:
            return
        
        # We are moving onto a new guess or the user has used up all guesses so disable Enter and Delete buttons
        self.__set_enter_button_enabled(False)
        self.__set_delete_button_enabled(False)
        
        # If this is the last allowed guess process the game over function
        if self.guess_row == self.chances - 1:
            self.__game_over(False)
            return
        
        # If not the last guess enable the keyboard for the next guess
        self.__set_keyboard_buttons_enabled(True)
        
        # Update to the next guess line waiting for the first guess letter
        self.guess_row += 1
        self.guess_column = 0
    
    # Function to execute the Delete button action
    def __delete_press(self):
        # Clear the status label
        self.__update_status_label()
        
        # If already at the first column return, we cannot delete further
        if self.guess_column == 0:
            return
        
        # Update the active letter column
        self.guess_column -= 1
        
        # Delete the last letter the user entered
        self.guess_labels[self.guess_row][self.guess_column]["text"] = ""
        
        # If we have now reached the first column disable the delete button, there are no letters left to delete in row
        if self.guess_column == 0:
            self.__set_delete_button_enabled(False)
            
        # If we deleted the last column letter, then disable Enter and enable the keyboard to allow for further user input
        if self.guess_column == self.answer_length - 1:
            self.__set_enter_button_enabled(False)
            self.__set_keyboard_buttons_enabled(True)
    
    # Function to update our on screen status label
    def __update_status_label(self, text="", bg="lightgray"):
        self.status_label["text"] = text
        self.status_label["bg"] = bg
            
    # Function to create the guess list entries at the top of our application
    def __create_guess_labels(self):
        py = 20
        
        # We will create a row for each chance the user has to guess the answer
        for i in range(self.chances):
            px = 150
            
            self.guess_labels.append([])
        
            # We will create a container for each letter the user needs to enter for a guess
            for __ in range(self.answer_length):
                label = tk.Label(self, text="", height=1, width=3, borderwidth=2, relief="groove", bg="white")
                label.place(x=px, y=py)

                self.guess_labels[i].append(label)
                px += 40

            py += 30
            
        return py

    # Function to create the status label to display information to the user
    def __create_status_label(self, py):
        py += 5
        self.status_label = tk.Label(self, text="", height=1, width=52, borderwidth=2, bg="lightgray")
        self.status_label.place(x=10, y=py)
        return py

    # Function to create the keyboard at the bottom of the application
    def __create_keyboard(self, py):
        px = 20
        py += 30
        
        # Create the first row of letters for our display keyboard
        for letter in self.keyboard.get_keyboard_row_1():
            self.__create_keyboard_button(letter.value.upper(), px, py)
            px += 45
        
        px = 45
        py += 30
        
        # Create the second row of letters for our display keyboard
        for letter in self.keyboard.get_keyboard_row_2():
            self.__create_keyboard_button(letter.value.upper(), px, py)
            px += 45
        
        px = 90
        py += 30
        
        # Create the third row of letters for our display keyboard
        for letter in self.keyboard.get_keyboard_row_3():
            self.__create_keyboard_button(letter.value.upper(), px, py)
            px += 45
        
        # Create the Enter button for our display keyboard
        self.enter_button = tk.Button(self, text=wordy_text.get_enter_button(), command=lambda: self.__enter_press(),
                                      state="disabled", height=1, width=4)
        self.enter_button.place(x=18, y=py)
        
        # Create the Delete button for our display keyboard
        self.delete_button = tk.Button(self, text=wordy_text.get_delete_button(), command=lambda: self.__delete_press(),
                                       state="disabled", height=1, width=4)
        self.delete_button.place(x=405, y=py)

    # Function to create a button for the keyboard
    def __create_keyboard_button(self, letter, px, py):
        button = tk.Button(self, text=letter, command=lambda: self.__keyboard_press(letter), height=1, width=1)
        button.place(x=px, y=py)
        
        self.keyboard_buttons[letter] = button

    # Function to set all keyboard buttons enabled or disabled
    def __set_keyboard_buttons_enabled(self, is_enabled):
        for button in self.keyboard_buttons.values():
            if is_enabled:
                button["state"] = "normal"
            else:
                button["state"] = "disabled"
    
    # Function to set the Delete button enabled or disabled
    def __set_delete_button_enabled(self, is_enabled):
        if is_enabled:
            self.delete_button["state"] = "normal"
        else:
            self.delete_button["state"] = "disabled"
    
    # Function to set the Enter button enabled or disabled
    def __set_enter_button_enabled(self, is_enabled):
        if is_enabled:
            self.enter_button["state"] = "normal"
        else:
            self.enter_button["state"] = "disabled"


# Note: Code can cope with words of N length, but currently we only have 5-letter dictionaries included  
# Launch our Wordy application
if __name__ == '__main__':
    app = None
    
    # Note: First parameter is always the modules name
    # If we have one user supplied parameter it is a user supplied answer
    if len(sys.argv) == 2:
        app = Wordy(sys.argv[1])
    # If we have a second user supplied parameter it is the number of attempted guesses they are allowing
    elif len(sys.argv) > 2:
        app = Wordy(sys.argv[1], sys.argv[2])
    # Else use our program defaults of random answer from our answer dictionary and 6 guesses allowed
    # We ignore any further arguments if supplied
    else:
        app = Wordy()
    
    # Launch the application
    app.mainloop()
