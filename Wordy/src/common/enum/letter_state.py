# @author: seanpcox

import enum


# Enum class to represent each state that a guess letter may be in
class LetterState(enum.Enum):

    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj
    
    def __init__(self, color):
        self.color = color

    # Letter has not yet been tried, this is only applicable for our keyboard display
    NOT_ASSIGNED = "white"
    # Letter has been tried but is incorrect
    INCORRECT = "gray"
    # Letter is in the answer but not in the right position
    WRONG_POSITION = "yellow"
    # Letter is correct and in the correct position
    CORRECT = "green"
