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
        rows = set()




print(Solution.isValidSudoku(None,
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))