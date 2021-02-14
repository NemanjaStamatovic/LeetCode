class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0 for i in range(n)] for j in range(n)]
            
        i = j = 0
        row_i = [0, 1, 0, -1]
        column_j = [1, 0, -1, 0]
        cycle = 0
        number = 1
        
        while True:
            
            matrix[i][j] = number
            
            if number == n * n:
                break    
                
            i_temp = i + row_i[cycle % 4]
            j_temp = j + column_j[cycle % 4]
            
            if (0 <= i_temp < n) and (0 <= j_temp < n) and (matrix[i_temp][j_temp] == 0):
                i = i_temp
                j = j_temp
                
            else:
                cycle += 1
                i = i + row_i[cycle % 4]
                j = j + column_j[cycle % 4]
            
            number += 1
            
        return matrix