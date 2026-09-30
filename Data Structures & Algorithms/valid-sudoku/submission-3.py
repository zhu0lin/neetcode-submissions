class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Input: a 9x9 2d array board containing of integers 1-9 or "."
        Output: 
        true if 
        -each row has no dupes
        -each col has no dupes
        -each 3x3 box has no dupes 

        false otherwise

        brute force?
        we can just check each of these criteria in 3 separate loops?
        i think maybe we can use a dict to keep track of the
        values we've seen so far so we can handle dupes?
        """
        #check for dupes in rows
        for row in board:
            row_dict = {}
            for val in row:
                if val == ".":
                    continue
                else:
                    if val in row_dict:
                        return False
                    row_dict[val] = 1

        #check dupes in cols  
        for i in range(len(board)):
            col_dict = {}
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue
                else:
                    if board[j][i] in col_dict:
                        return False
                    col_dict[board[j][i]] = 1

        #check dupes in each 3x3 box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box_dict = {}
                for r in range(3):
                    for c in range(3):
                        if board[i + r][j + c] == ".":
                            continue
                        else:
                            if board[i + r][j + c] in box_dict:
                                return False
                            box_dict[board[i + r][j + c]] = 1

        return True

