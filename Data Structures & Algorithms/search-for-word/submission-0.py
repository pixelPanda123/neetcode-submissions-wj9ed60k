class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        l = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(r,c,l):
            if l == len(word):
                return True 
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[l]):
                return False 
            temp = board[r][c]
            board[r][c] = "#"

            for dr, dc in directions: 
                if dfs(r+dr, c+dc, l+1):
                    return True 
            board[r][c] = temp 
            return False 
        for r in range(rows):
            for j in range(cols):
                if board[r][j] == word[0]:
                    if dfs(r,j,0):
                        return True 
        return False 