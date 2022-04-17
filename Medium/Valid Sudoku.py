import collections
from typing import List


class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     for row in board:
    #         seen = set()
    #         for num in row:
    #             if num in seen:
    #                 return False
    #             if num != '.':
    #                 seen.add(num)
    #     for i in range(len(board)):
    #         col = set()
    #         for j in range(len(board)):
    #             if board[j][i] in col:
    #                 return False
    #             if board[j][i] != '.':
    #                 col.add(board[j][i])
    #     for i in range(len(board)//3):
    #         print(i)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True


print(Solution.isValidSudoku(None,
[["5","3","3",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))