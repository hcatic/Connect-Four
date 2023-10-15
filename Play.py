# Playing the game  

from Board import *
from Player import *
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p, b):
    """takes two parameters: a Player object p for the player whose move is
    being processed, and a Board object b for the board on which the game
    is being played"""
    if p.checker == 'X':
        old = 'X'
        new = 'O'
    else:
        old = 'O'
        new = 'X'
    turn = p.__repr__()
    print(turn + "'s turn" )
    
    col = p.next_move(b)
    b.add_checker(p.checker, col)
    print()
    print(b)
    if b.is_win_for(old) == True and b.is_win_for(new) == True:
        print('It is a tie!')
        return True
    elif b.is_win_for(old) == True and b.is_win_for(new) == False:
        print(turn, "wins in", p.num_moves, "moves.", "\n", "Congratulations!")
        return True
    elif b.is_win_for(new) == True and b.is_win_for(old) == False:
        print('Player', new, "wins in", p.num_moves, "moves.", "\n", "Congratulations!")
        return True
    elif b.is_full() == True:
        print('It is a tie!')
        return True
    else:
        return False
    
class RandomPlayer(Player):
    def next_move(self, b):
        """used for an unintelligent computer player that chooses at random
        from the available columns"""
        lst = []
        for i in range(b.width):
            if b.can_add_to(i) == True:
                lst += [i]
        n = random.choice(lst)
        self.num_moves += 1
        if n == []:
            return self.__repr__()
        else:
            return n