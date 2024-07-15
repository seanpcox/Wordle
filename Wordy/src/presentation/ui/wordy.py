# @author: seanpcox

import tkinter as tk
from src.application.logic import wordy_logic
from src.common.object.keyboard import Keyboard
from src.resources.text import wordy_text


class Wordy(tk.Tk):

    def __init__(self, answer, chances):
        # Set our window title and size
        super(self.__class__, self).__init__()
        self.title(wordy_text.get_ui_title())
        self.geometry('420x270')
        
        self.answer_length = len(answer)
        self.chances = chances
        
        # Create our guess list at the top of the application
        self.guess_list = []
        self.guess_row = 0
        self.guess_column = 0
        py = self.create_guess_list()
        
        # Create our display keyboard at the bottom of the application
        self.keyboard = Keyboard()
        self.keyboard_buttons = {}
        self.create_keyboard(py)

    # Function to process a user guess
    def process_guess(self):
        return
    
    # Function to execute when the current game has ended
    def game_over(self):
        return
    
    # Function to execute a Keyboard Letter action
    def keyboard_press(self, letter):
        # If the user has already reached the letter length for a guess then return
        if self.guess_column == self.answer_length:
            return
        
        # Update the container for the current position in the current guess line with the user's letter selection
        self.guess_list[self.guess_row][self.guess_column]["text"] = letter
        
        # Move the column index to the next position
        self.guess_column += 1
        
        # If the user has entered one letter then we can enable the Delete button
        if self.guess_column == 1:
            self.set_delete_button_enabled(True)
        
        # If the user has entered the last letter for a guess then enable the Enter button and disable the Keyboard
        if self.guess_column == self.answer_length:
            self.set_enter_button_enabled(True)
            self.set_keyboard_buttons_enabled(False)
        
    # Function to execute the Enter button action
    def enter_press(self):
        # If there are not enough letters yet for a guess return
        if self.guess_column < self.answer_length:
            return 
        
        # We are moving onto a new guess or the user has used up all guesses so disable Enter and Delete buttons
        self.set_enter_button_enabled(False)
        self.set_delete_button_enabled(False)
        
        # Process our users current guess
        self.process_guess()
        
        # If this is the last allowed guess process the game over function
        if self.guess_row == self.chances - 1:
            self.game_over()
            return
        
        # If not the last guess enable the keyboard for the next guess
        self.set_keyboard_buttons_enabled(True)
        
        # Update to the next guess line waiting for the first guess letter
        self.guess_row += 1
        self.guess_column = 0
    
    # Function to execute the Delete button action
    def delete_press(self):
        # If already at the first column return, we cannot delete further
        if self.guess_column == 0:
            return
        
        # Update the active letter column
        self.guess_column -= 1
        
        # Delete the last letter the user entered
        self.guess_list[self.guess_row][self.guess_column]["text"] = ""
        
        # If we have now reached the first column disable the delete button, there are no letters left to delete in row
        if self.guess_column == 0:
            self.set_delete_button_enabled(False)
            
        # If we deleted the last column letter, then disable Enter and enable the keyboard to allow for further user input
        if self.guess_column == self.answer_length - 1:
            self.set_enter_button_enabled(False)
            self.set_keyboard_buttons_enabled(True)

    # Function to create the guess list entries at the top of our application
    def create_guess_list(self):
        py = 0
        
        # We will create a row for each chance the user has to guess the answer
        for i in range(self.chances):
            px = 110
            
            self.guess_list.append([])
        
            # We will create a container for each letter the user needs to enter for a guess
            for __ in range(self.answer_length):
                lbl = tk.Button(self, text="", height=2, width=1)
                lbl.place(x=px, y=py)
                lbl["state"] = "disabled"

                self.guess_list[i].append(lbl)
                px += 40

            py += 25
            
        return py

    # Function to create the keyboard at the bottom of the application
    def create_keyboard(self, py):
        px = 10
        py += 25
        
        # Create the first row of letters for our display keyboard
        for letter in self.keyboard.get_keyboard_row_1():
            self.create_keyboard_button(letter.value.upper(), px, py)
            px += 40
        
        px = 30
        py += 25
        
        # Create the second row of letters for our display keyboard
        for letter in self.keyboard.get_keyboard_row_2():
            self.create_keyboard_button(letter.value.upper(), px, py)
            px += 40
        
        px = 70
        py += 25
        
        # Create the third row of letters for our display keyboard
        for letter in self.keyboard.get_keyboard_row_3():
            self.create_keyboard_button(letter.value.upper(), px, py)
            px += 40
        
        # Create the Enter button for our display keyboard
        self.enter_button = tk.Button(self, text=wordy_text.get_enter_button(), command=lambda: self.enter_press(),
                                      state="disabled", height=2, width=4)
        self.enter_button.place(x=10, y=py)
        
        # Create the Delete button for our display keyboard
        self.delete_button = tk.Button(self, text=wordy_text.get_delete_button(), command=lambda: self.delete_press(),
                                       state="disabled", height=2, width=4)
        self.delete_button.place(x=347, y=py)

    # Function to create a button for the keyboard
    def create_keyboard_button(self, letter, px, py):
        bnt = tk.Button(self, text=letter, command=lambda: self.keyboard_press(letter), height=2, width=1)
        bnt.place(x=px, y=py)
        
        self.keyboard_buttons[letter] = bnt

    # Function to set all keyboard buttons enabled or disabled
    def set_keyboard_buttons_enabled(self, is_enabled):
        for button in self.keyboard_buttons.values():
            if is_enabled:
                button["state"] = "normal"
            else:
                button["state"] = "disabled"
    
    # Function to set the Delete button enabled or disabled
    def set_delete_button_enabled(self, is_enabled):
        if is_enabled:
            self.delete_button["state"] = "normal"
        else:
            self.delete_button["state"] = "disabled"
    
    # Function to set the Enter button enabled or disabled
    def set_enter_button_enabled(self, is_enabled):
        if is_enabled:
            self.enter_button["state"] = "normal"
        else:
            self.enter_button["state"] = "disabled"


# Launch our Wordy application
if __name__ == '__main__':
    app = Wordy(wordy_logic.get_random_answer(), 6)
    app.mainloop()
