class Solution:
    def exist(self, board, word):
        # Define the backtracking function
        def backtrack(i, j, index):
            # If we have matched all characters in the word, return True
            if index == len(word):
                return True
            # Check if the current position is out of bounds or the character doesn't match
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[index]:
                return False
            # Temporarily mark the cell as visited by changing its value
            temp = board[i][j]
            board[i][j] = '#'
            
            # Explore all four directions (up, down, left, right)
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for di, dj in directions:
                if backtrack(i + di, j + dj, index + 1):
                    return True
            
            # Restore the cell's original value (unmark it)
            board[i][j] = temp
            return False
        
        # Loop through all cells in the grid
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # Start backtracking if the first letter matches
                    if backtrack(i, j, 0):
                        return True
        
        return False
