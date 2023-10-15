# A Connect Four Board class

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         

        for row in range(self.height):
            s += '|'   

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  
        
        new = "--" * self.width
        new += "-"
        
        old = ' '
        for i in range(self.width):
            if i > 9:
                old += str(i - 10) + ' '
            else:
                old += str(i) + ' '
        
        return s + new + '\n' + old

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        
        row = self.height - 1
        while row >= 0:
            if self.slots[row][col] == ' ':
                break
            else: 
                row -= 1
        self.slots[row][col] = checker
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
    
    def reset(self):
        """clears the board"""
        for i in range(self.height):
            for j in range(self.width):
                if self.slots[i][j] != ' ':
                    self.slots[i][j] = ' '
    
    def can_add_to(self, col):
        """checks to see if a checker can be put in the imputted row"""
        if 0 <= col < self.width and self.slots[0][col] == ' ':
            return True
        return False
    
    def is_full(self):
        """checks if the board is full of checkers"""
        for i in range(self.height):
            for j in range(self.width):
                if self.slots[i][j] == ' ':
                    return False
        return True
    
    def remove_checker(self, col):
        """removes the top checker on the row imputted"""
        row = 0
        while row < self.height:
           if self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
                self.slots[row][col] = ' '
                break
           else:
                row += 1
    
    def is_win_for(self, checker):
        """checks if there is a win for the inputted checker"""
        assert(checker == 'X' or checker == 'O')
        
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                       return True
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                  self.slots[row + 1][col] == checker and \
                  self.slots[row + 2][col] == checker and \
                  self.slots[row + 3][col] == checker:
                      return True
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                    self.slots[row + 2][col + 2] == checker and \
                    self.slots[row + 3][col + 3] == checker:
                        return True
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                  self.slots[row - 1][col + 1] == checker and \
                  self.slots[row - 2][col + 2] == checker and \
                  self.slots[row - 3][col + 3] == checker:
                      return True
        return False