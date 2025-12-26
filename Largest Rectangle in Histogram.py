class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        
        # Traverse each bar in the histogram
        for i in range(len(heights)):
            # While the stack is not empty and the current height is less than the height of the bar
            # at the index stored at the top of the stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Pop the top bar's height
                # Calculate the width of the rectangle:
                # If the stack is empty, it means the rectangle spans the entire width up to index i
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            
            # Push current bar's index onto the stack
            stack.append(i)
        
        # Process any remaining bars in the stack
        while stack:
            h = heights[stack.pop()]
            w = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, h * w)
        
        return max_area
