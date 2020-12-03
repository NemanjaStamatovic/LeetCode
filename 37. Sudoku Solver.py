class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def next_available_field(i, j):   
            for x in range(9):
                for y in range(9):
                    if board[x][y] == ".":
                        return x, y
                    
            return -1, -1        
                    
        def validation(i, j, new_element):
            for x in range(9):
                if board[x][j] == str(new_element):
                    return False
                    
            for y in range(9):
                if board[i][y] == str(new_element):
                    return False
                
            square_x = 3 * (i // 3)
            square_y = 3 * (j // 3)
            for x in range(square_x, square_x + 3):
                for y in range(square_y, square_y + 3):
                    if board[x][y] == str(new_element):
                        return False
                    
            return True
        
        def solve(i=0, j=0):
            i, j = next_available_field(i, j)
            if i == -1:
                return True
            
            for new_element in range(1, 10):
                if validation(i, j, new_element):
                    board[i][j] = str(new_element)
                    
                    if solve(i, j):
                        return True
                    
                    board[i][j] = "."
                    
            return False
        
        solve()