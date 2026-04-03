from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        for i in range(m):
            for j in range(n):
                live = sum(board[x][y] > 0 for x in range(max(0,i-1),min(m,i+2))
                           for y in range(max(0,j-1),min(n,j+2))
                           if (x,y) != (i,j))
                if board[i][j] == 1 and live not in (2,3):
                    board[i][j] = 2
                elif board[i][j] == 0 and live == 3:
                    board[i][j] = -1
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1
        