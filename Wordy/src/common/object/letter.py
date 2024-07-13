# @author: seanpcox


# Class to represent a letter in both our guess and display keyboard, contains the letter and the state compared to the answer
class Letter:
    
    def __init__(self, value, state):
        self.value = value
        self.state = state
