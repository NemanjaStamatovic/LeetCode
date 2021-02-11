class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        result = []
        
        i = j = 0
        m = len(matrix)
        n = len(matrix[0])
        numbers = m * n
        
        row_i = [0, 1, 0, -1]
        column_j = [1, 0, -1, 0]
        
        cycle = 0
        
        while True:
            cycle_temp = cycle % 4
            if matrix[i][j] != "*":
                result.append(matrix[i][j])
                matrix[i][j] = "*"
            i_temp = i + row_i[cycle_temp]
            j_temp = j + column_j[cycle_temp]
            if (0 <= i_temp < m) and (0 <= j_temp < n) and (matrix[i_temp][j_temp] != "*"):
                i = i_temp
                j = j_temp
                continue
            cycle += 1
            if len(result) == numbers:
                break
                
        return result        