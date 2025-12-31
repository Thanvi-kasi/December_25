class Solution:
    def grayCode(self, n: int):
        # Base case: if n = 0, the Gray code sequence is [0]
        if n == 0:
            return [0]
        
        # Recursive case: Get the Gray code sequence for n-1
        prev_gray_code = self.grayCode(n - 1)
        
        # First part: prepend '0' to each element of prev_gray_code
        first_half = [x for x in prev_gray_code]
        
        # Second part: prepend '1' to each element of reversed prev_gray_code
        second_half = [(1 << (n - 1)) | x for x in reversed(prev_gray_code)]
        
        # Combine the first and second parts
        return first_half + second_half
