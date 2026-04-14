class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        indices = []
        m,n = len(matrix), len(matrix[0])
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0: 
                    indices.append((x,y))
        def convert(x,y):
            #rows
            for c in range(n):
                matrix[x][c] = 0
            #cols 
            for r in range(m):
                matrix[r][y] = 0 
        for i,j in indices: 
            convert(i,j)

        