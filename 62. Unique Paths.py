class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        matrix = [[1 for _ in range(n)] for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
                
        return matrix[-1][-1]        