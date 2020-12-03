class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            row = []
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row:
                    return False
                row.append(board[i][j])
                
        for j in range(len(board[0])):
            column = []
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in column:
                    return False
                column.append(board[i][j])
                
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                square = [(row[j:j + 3]) for row in board[i:i + 3]]
                square = square[0] + square[1] + square[2]
                square = [int(item) for item in square if item != "."]
                if sum(square) != sum(set(square)):
                    return False
                           
        return True                   