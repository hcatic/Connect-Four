# AI Player for use in Connect Four  

import random  
from Play import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def __repr__(self):
        """returns a string representing an AIPlayer object. This method will
        override/replace the __repr__ method that is inherited from Player.
        In addition to indicating which checker the AIPlayer object is using,
        the returned string should also indicate the player’s tiebreaking
        strategy and lookahead"""
        
        s = str(self.lookahead)
        return 'Player '+ self.checker + ' (' + self.tiebreak + ', ' + s + ')'
    
    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the
        board, and that returns the index of the column with the maximum
        score. If one or more columns are tied for the maximum score, the
        method should apply the called AIPlayer‘s tiebreaking strategy to
        break the tie"""
        
        max_score = max(scores)
        new = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                new += [i]
        
        if self.tiebreak == 'RANDOM':
            j = random.choice(new)
            return j
        elif self.tiebreak == 'LEFT':
            j = new[0]
            return j
        elif self.tiebreak == 'RIGHT':
            return new[-1]
    
    def scores_for(self, b):
        """takes a Board object b and determines the called AIPlayer‘s scores
        for the columns in b. Each column should be assigned one of the four
        possible scores discussed in the Overview at the start of this problem
        , based on the called AIPlayer‘s lookahead value. The method should
        return a list containing one score for each column"""
    
        scores = [50] * b.width
        for i in range(b.width):
            if b.can_add_to(i) == False:
                scores[i] = -1
            elif b.is_win_for(self.checker) == True:
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()) == True: 
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                b.add_checker(self.checker, i)
                a = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                second = a.scores_for(b)
                if 100 in second:
                    scores[i] = 0
                elif 0 in second and 50 not in second:
                    scores[i] = 100
                else:
                    scores[i] = 50
                b.remove_checker(i)
        return scores
    
    def next_move(self, b):
        """overrides (i.e., replaces) the next_move method that is inherited 
        from Player. Rather than asking the user for the next move, this
        version of next_move should return the called AIPlayer‘s judgment of
        its best possible move"""
        
        moves = self.scores_for(b)
        new = self.max_score_column(moves)
        return new