# A Connect-Four Player class 

from Board import *

class Player:
    def __init__(self, checker):
        """constructs a new Player object by initializing the following
        two attributes"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """returns a string representing a Player object. The string returned
        should indicate which checker the Player object is using"""
        if self.checker == 'X':
            return('Player X')
        elif self.checker == 'O':
            return('Player O')
        
    def opponent_checker(self):
        """returns a one-character string representing the checker
        of the Player object’s opponent"""
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self, b):
        """accepts a Board object b as a parameter and returns the column
        where the player wants to make the next move. To do this, the method
        should ask the user to enter a column number that represents where
        the user wants to place a checker on the board. The method should
        repeatedly ask for a column number until a valid column number
        is given"""
        self.num_moves += 1
        while True:
            c = int(input('Enter a column: '))
            if b.can_add_to(c):
                return c
            else:
                print("Try again!")