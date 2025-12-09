class Solution:
    def plusOne(self, digits):
        # Traverse the digits array from the end to the start
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            # Increment the current digit
            digits[i] += 1
            
            # If there's no carry, return the result
            if digits[i] < 10:
                return digits
            
            # If there is a carry, set the current digit to 0 and continue to the next digit
            digits[i] = 0
        
        # If we completed the loop, it means we have a carry over past the most significant digit
        # So we need to add a 1 at the beginning of the array
        return [1] + digits
