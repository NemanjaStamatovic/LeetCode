class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [""] * numRows
        current_row = 0
        down_direction = False
        
        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows-1:
                down_direction = not down_direction
            if down_direction:
                current_row += 1
            else:
                current_row -= 1
                
        return "".join(rows)