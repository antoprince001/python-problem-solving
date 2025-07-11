# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Bruteforce logic
from enum import Enum

class OrderType(Enum):
    ROW = 'row'
    COLUMN = 'column'
    SUBBOX = 'subbox'
    
class Solution:
    def __init__(self):
        self.row_check_list = []
        self.column_check_list = []
        self.subbox_check_list = []

    def checkIsValidSequence(self, element, row, col, order_type : OrderType):
        if int(element) < 1:
            return False
        if int(element)  > 9:
            return False
        if  order_type.value == 'row' and int(element)  in self.row_check_list:
            return False
        if  order_type.value == 'column' and int(element)  in self.column_check_list:
            return False
        if  order_type.value == 'subbox' and int(element)  in self.subbox_check_list:
            return False
        return True
    
    def isValidSubBox(self,board, i, j):
        # i,j
        if  board[i][j] != ".":
            if self.checkIsValidSequence(board[i][j] , i, j, OrderType.SUBBOX):
                self.subbox_check_list.append(int(board[i][j]))
            else:
                return False
        # i,j+1
        if board[i][j+1] != ".":
            if self.checkIsValidSequence(board[i][j+1] , i, j+1, OrderType.SUBBOX):
                self.subbox_check_list.append(int(board[i][j+1]))
            else:
                return False
        # i,j+2
        if board[i][j+2] != ".":
            if self.checkIsValidSequence(board[i][j+2] , i, j+2, OrderType.SUBBOX):
                self.subbox_check_list.append(int(board[i][j+2]))
            else:
                return False
        # i+1,j
        if board[i+1][j] != ".":
            if self.checkIsValidSequence(board[i+1][j] , i+1, j, OrderType.SUBBOX):
                self.subbox_check_list.append(int(board[i+1][j]))
            else:
                return False
        # i+1,j+1
        if board[i+1][j+1] != ".":
            if self.checkIsValidSequence(board[i+1][j+1] , i+1, j+1, OrderType.SUBBOX):
                self.subbox_check_list.append(int(board[i+1][j+1]))
            else:
                return False
        # i+1,j+2
        if board[i+1][j+2] != ".": 
            if self.checkIsValidSequence(board[i+1][j+2] , i+1, j+2, OrderType.SUBBOX):
                self.subbox_check_list.append(int(board[i+1][j+2]))
            else:
                return False
        # i+2,j
        if board[i+2][j] != ".": 
            if self.checkIsValidSequence(board[i+2][j] , i+2, j, OrderType.SUBBOX):
                self.subbox_check_list.append(int(board[i+2][j]))
            else:
                return False
        # i+2,j+1
        if board[i+2][j+1] != ".":
            if self.checkIsValidSequence(board[i+2][j+1] , i+2, j+1, OrderType.SUBBOX):
                self.subbox_check_list.append(int(board[i+2][j+1]))
            else:
                return False
        # i+2,j+2
        if board[i+2][j+2] != ".":
            if self.checkIsValidSequence(board[i+2][j+2] , i+2, j+2, OrderType.SUBBOX):
                self.subbox_check_list.append(int(board[i+2][j+2]))
            else:
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check row
        for i in range(0,9):
            self.row_check_list = []
            self.column_check_list = []
            for j in range(0,9):
                if board[i][j] != ".":
                    if self.checkIsValidSequence(board[i][j] , i, j, OrderType.ROW):
                        self.row_check_list.append(int(board[i][j]))
                    else:
                        return False
                if board[j][i] != ".":
                    if self.checkIsValidSequence(board[j][i] , j, i, OrderType.COLUMN):
                        self.column_check_list.append(int(board[j][i]))
                    else:
                        return False

            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    self.subbox_check_list = []
                    if not self.isValidSubBox(board, i, j):
                        return False
        return True
                
# Refactored


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_seen = set()
            col_seen = set()
            for j in range(9):
                # Row check
                if board[i][j] != '.':
                    if board[i][j] in row_seen:
                        return False
                    row_seen.add(board[i][j])
                # Column check
                if board[j][i] != '.':
                    if board[j][i] in col_seen:
                        return False
                    col_seen.add(board[j][i])
        
        # Sub-box check
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val != '.':
                            if val in box_seen:
                                return False
                            box_seen.add(val)
        return True

 
class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))
