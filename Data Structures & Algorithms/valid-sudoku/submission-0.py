class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        U:
        Input: a list of lists with a digit 1-9 or '.'
        Output: True if valid sudoku else False
        P:
        Initialize a dictionary for each row and column to check for duplicates

        """

        for i in range(len(board)):
            dict = {}
            for j in range(len(board[i])):
                if board[i][j] != "." and board[i][j] in dict:
                    return False
                else:
                    dict[board[i][j]] = 1

        for i in range(len(board)):
            dict = {}
            for j in range(len(board[i])):
                if board[j][i] != "." and board[j][i] in dict:
                    return False
                else:
                    dict[board[j][i]] = 1
        
        for box_row in [0, 3, 6]:        
            for box_col in [0, 3, 6]:
                dict = {}
                for i in range(3):
                    for j in range(3):
                        if board[box_row+i][box_col+j] != "." and board[box_row + i][box_col + j] in dict:
                            return False
                        else:
                            dict[board[box_row+i][box_col+j]] = 1
        return True  
