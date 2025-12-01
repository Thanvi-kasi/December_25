class Solution:
    def generateMatrix(self, n: int):
        # Create an n x n matrix initialized with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Define the boundaries of the spiral
        top, bottom, left, right = 0, n - 1, 0, n - 1
        current_num = 1
        
        # Loop to fill the matrix in a spiral pattern
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                matrix[top][i] = current_num
                current_num += 1
            top += 1
            
            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                matrix[i][right] = current_num
                current_num += 1
            right -= 1
            
            if top <= bottom:
                # Traverse from right to left along the bottom row
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = current_num
                    current_num += 1
                bottom -= 1
            
            if left <= right:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = current_num
                    current_num += 1
                left += 1
        
        return matrix
