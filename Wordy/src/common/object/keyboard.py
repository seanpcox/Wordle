# @author: seanpcox

from src.common.enum.letter_state import LetterState
from src.common.object.letter import Letter


class Keyboard:

    def __init__(self):
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
        
        self.__letter_dict = {"q":q_letter,
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
        
        self.__keyboard_row_1 = [q_letter,
                       w_letter,
                       e_letter,
                       r_letter,
                       t_letter,
                       y_letter,
                       u_letter,
                       i_letter,
                       o_letter,
                       p_letter]
        
        self.__keyboard_row_2 = [a_letter,
                       s_letter,
                       d_letter,
                       f_letter,
                       g_letter,
                       h_letter,
                       j_letter,
                       k_letter,
                       l_letter]
        
        self.__keyboard_row_3 = [z_letter,
                       x_letter,
                       c_letter,
                       v_letter,
                       b_letter,
                       n_letter,
                       m_letter]
    
    def get_letter(self, letter):
        return self.__letter_dict.get(letter)
    
    def get_keyboard_row_1(self):
        return self.__keyboard_row_1
    
    def get_keyboard_row_2(self):
        return self.__keyboard_row_2
    
    def get_keyboard_row_3(self):
        return self.__keyboard_row_3
