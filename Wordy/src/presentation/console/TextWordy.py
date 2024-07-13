# @author: seanpcox

import random
from src.common.enum.letter_state import LetterState
from src.common.letter import Letter
from src.resources.dict.allowed_guesses_set import ALLOWED_GUESSES
from src.resources.dict.allowed_answers_list import ALLOWED_ANSWERS

def printBlueLine(word):
    print("\033[34m{}\033[00m".format(word))

def printRedLine(word):
    print("\033[31m{}\033[00m".format(word))

def printGreenUpper(word):
    print("\033[32m{}\033[00m".format(word.upper()), end="", flush=True)
    
def printYellowUpper(word): 
    print("\033[38;2;255;165;0m{}\033[00m".format(word.upper()), end="", flush=True)
    
def printDarkGrayUpper(word):
    print("\033[90m{}\033[00m".format(word.upper()), end="", flush=True)

def printLightGrayUpper(word):
    print("\033[37m{}\033[00m".format(word.upper()), end="", flush=True)
        
def printBlackUpper(word):
    print("\033[99m{}\033[00m".format(word.upper()), end="", flush=True)

def printSpace():
    print(" ", end="", flush=True)

def printLetterLine(letters, startSpaces=0, isKeyboard=True):
    for i in range(startSpaces):
        printSpace()
    
    for i in range(len(letters)):
        if letters[i].state == LetterState.CORRECT:
            printGreenUpper(letters[i].value)
        elif letters[i].state == LetterState.WRONG_POSITION:
            printYellowUpper(letters[i].value)
        elif letters[i].state == LetterState.INCORRECT:
            if isKeyboard:
                printLightGrayUpper(letters[i].value)
            else:
                printDarkGrayUpper(letters[i].value)
        elif letters[i].state == LetterState.NOT_ASSIGNED:
            printBlackUpper(letters[i].value)
  
        if i < (len(letters) - 1):
            printSpace()
            
    print()

def runGame(answer):
    printBlueLine("-------------------")
    printBlueLine("     W O R D Y     ")
    printBlueLine("-------------------")
    
    instructionText = "Enter 5-letter guess ({}/6): "
    invalidInputText = "Guess must be 5 letters"
    invalidGuessText = "Guess is not in our dictionary"
    
    guessesRaw = ["","","","","",""]
    guessesFormat = [[],[],[],[],[],[]]
    
    q_letter = Letter("q", LetterState.NOT_ASSIGNED)
    w_letter = Letter("w", LetterState.NOT_ASSIGNED)
    e_letter = Letter("e", LetterState.NOT_ASSIGNED)
    r_letter = Letter("r", LetterState.NOT_ASSIGNED)
    t_letter = Letter("t", LetterState.NOT_ASSIGNED)
    y_letter = Letter("y", LetterState.NOT_ASSIGNED)
    u_letter = Letter("u", LetterState.NOT_ASSIGNED)
    i_letter = Letter("i", LetterState.NOT_ASSIGNED)
    o_letter = Letter("o", LetterState.NOT_ASSIGNED)
    p_letter = Letter("p", LetterState.NOT_ASSIGNED)
    a_letter = Letter("a", LetterState.NOT_ASSIGNED)
    s_letter = Letter("s", LetterState.NOT_ASSIGNED)
    d_letter = Letter("d", LetterState.NOT_ASSIGNED)
    f_letter = Letter("f", LetterState.NOT_ASSIGNED)
    g_letter = Letter("g", LetterState.NOT_ASSIGNED)
    h_letter = Letter("h", LetterState.NOT_ASSIGNED)
    j_letter = Letter("j", LetterState.NOT_ASSIGNED)
    k_letter = Letter("k", LetterState.NOT_ASSIGNED)
    l_letter = Letter("l", LetterState.NOT_ASSIGNED)
    z_letter = Letter("z", LetterState.NOT_ASSIGNED)
    x_letter = Letter("x", LetterState.NOT_ASSIGNED)
    c_letter = Letter("c", LetterState.NOT_ASSIGNED)
    v_letter = Letter("v", LetterState.NOT_ASSIGNED)
    b_letter = Letter("b", LetterState.NOT_ASSIGNED)
    n_letter = Letter("n", LetterState.NOT_ASSIGNED)
    m_letter = Letter("m", LetterState.NOT_ASSIGNED)
    
    letterDict = {"q":q_letter,
                  "w":w_letter,
                  "e":e_letter,
                  "r":r_letter,
                  "t":t_letter,
                  "y":y_letter,
                  "u":u_letter,
                  "i":i_letter,
                  "o":o_letter,
                  "p":p_letter,
                  "a":a_letter,
                  "s":s_letter,
                  "d":d_letter,
                  "f":f_letter,
                  "g":g_letter,
                  "h":h_letter,
                  "j":j_letter,
                  "k":k_letter,
                  "l":l_letter,
                  "z":z_letter,
                  "x":x_letter,
                  "c":c_letter,
                  "v":v_letter,
                  "b":b_letter,
                  "n":n_letter,
                  "m":m_letter}
    
    lettersRow1 = [q_letter,
                   w_letter,
                   e_letter,
                   r_letter,
                   t_letter,
                   y_letter,
                   u_letter,
                   i_letter,
                   o_letter,
                   p_letter]
    
    lettersRow2 = [a_letter,
                   s_letter,
                   d_letter,
                   f_letter,
                   g_letter,
                   h_letter,
                   j_letter,
                   k_letter,
                   l_letter]
    
    lettersRow3 = [z_letter,
                   x_letter,
                   c_letter,
                   v_letter,
                   b_letter,
                   n_letter,
                   m_letter]
    
    correctLetterCount = 0
    
    for gInx in range(6):
        correctLetterCount = 0
        
        answerCopy = []
        
        for aInx in range(5):
            answerCopy.append(answer[aInx])
        
        print()
        guessesRaw[gInx] = input(instructionText.format(gInx+1))
        
        while(len(guessesRaw[gInx]) != 5):
            printRedLine(invalidInputText)
            guessesRaw[gInx] = input(instructionText.format(gInx+1))
        
        while(guessesRaw[gInx] not in ALLOWED_GUESSES):
            printRedLine(invalidGuessText)
            guessesRaw[gInx] = input(instructionText.format(gInx+1))
        
        print()
        
        for i in range(len(guessesRaw[gInx])):
            lcLetter = guessesRaw[gInx][i].lower()
            letterState = LetterState.INCORRECT

            dictLetter = letterDict.get(lcLetter);
            if dictLetter.state == LetterState.NOT_ASSIGNED:
                dictLetter.state = LetterState.INCORRECT

            if lcLetter == answerCopy[i]:
                letterState = LetterState.CORRECT
                
                dictLetter = letterDict.get(lcLetter);
                if dictLetter.state != LetterState.CORRECT:
                    dictLetter.state = LetterState.CORRECT
                
                correctLetterCount += 1
                answerCopy[i] = "?"
            
            guessesFormat[gInx].append(Letter(lcLetter, letterState))
            
        for i in range(len(guessesRaw[gInx])):
            letter = guessesFormat[gInx][i]
            
            if letter.state != LetterState.CORRECT:
                if letter.value in answerCopy:
                    dictLetter = letterDict.get(letter.value);
                    if dictLetter.state != LetterState.CORRECT:
                        dictLetter.state = LetterState.WRONG_POSITION
                    
                    guessesFormat[gInx][i] = Letter(letter.value, LetterState.WRONG_POSITION)
                    answerCopy[answerCopy.index(letter.value)] = "?"
    
        printLetterLine(guessesFormat[gInx],5,False)
        print()
        printLetterLine(lettersRow1,0)
        printLetterLine(lettersRow2,1)
        printLetterLine(lettersRow3,3)
        
        if correctLetterCount == 5:
            break
                        
runGame("flown")