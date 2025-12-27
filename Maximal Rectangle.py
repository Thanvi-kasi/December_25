class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            # Update histogram heights
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            # Compute largest rectangle in histogram
            stack = []
            for i in range(cols + 1):
                current_height = heights[i] if i < cols else 0
                while stack and heights[stack[-1]] > current_height:
                    h = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * width)
                stack.append(i)
        
        return max_area
