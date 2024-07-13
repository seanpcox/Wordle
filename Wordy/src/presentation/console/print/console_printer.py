# @author: seanpcox

from src.common.enum.letter_state import LetterState

class ConsolePrinter:
    
    def __init__(self):
        return
    
    def printBlueLine(self, word):
        print("\033[34m{}\033[00m".format(word))
    
    def printRedLine(self, word):
        print("\033[31m{}\033[00m".format(word))
    
    def printGreenUpper(self, word):
        print("\033[32m{}\033[00m".format(word.upper()), end="", flush=True)
        
    def printYellowUpper(self, word): 
        print("\033[38;2;255;165;0m{}\033[00m".format(word.upper()), end="", flush=True)
        
    def printDarkGrayUpper(self, word):
        print("\033[90m{}\033[00m".format(word.upper()), end="", flush=True)
    
    def printLightGrayUpper(self, word):
        print("\033[37m{}\033[00m".format(word.upper()), end="", flush=True)
            
    def printBlackUpper(self, word):
        print("\033[99m{}\033[00m".format(word.upper()), end="", flush=True)
    
    def printEmptyLine(self):
        print()
    
    def printSpace(self):
        print(" ", end="", flush=True)
    
    def printLetterLine(self, letters, startSpaces=0, isKeyboard=True):
        for i in range(startSpaces):
            self.printSpace()
        
        for i in range(len(letters)):
            if letters[i].state == LetterState.CORRECT:
                self.printGreenUpper(letters[i].value)
            elif letters[i].state == LetterState.WRONG_POSITION:
                self.printYellowUpper(letters[i].value)
            elif letters[i].state == LetterState.INCORRECT:
                if isKeyboard:
                    self.printLightGrayUpper(letters[i].value)
                else:
                    self.printDarkGrayUpper(letters[i].value)
            elif letters[i].state == LetterState.NOT_ASSIGNED:
                self.printBlackUpper(letters[i].value)
      
            if i < (len(letters) - 1):
                self.printSpace()
                
        print()