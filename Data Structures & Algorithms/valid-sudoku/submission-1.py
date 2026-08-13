class Solution:
    from collections import defaultdict
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        U:
        Input: a list of lists with a digit 1-9 or '.'
        Output: True if valid sudoku else False
        P:
        Initialize a dictionary for each row and column to check for duplicates

        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row//3,col//3)]:
                    return False

                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row//3,col//3)].add(board[row][col])

        return True