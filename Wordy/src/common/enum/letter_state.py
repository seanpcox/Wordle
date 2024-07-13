# @author: seanpcox

import enum


class LetterState(enum.Enum):

    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj
    
    def __init__(self, color):
        self.color = color

    NOT_ASSIGNED = "white"
    INCORRECT = "gray"
    WRONG_POSITION = "yellow"
    CORRECT = "green"
