class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize the result string and carry
        result = []
        carry = 0
        
        # Start from the last digit and move towards the first
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            # Get the current digits from both strings, or 0 if the string is exhausted
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Sum the bits along with the carry
            total = bit_a + bit_b + carry
            
            # The current bit is total % 2 (either 0 or 1)
            result.append(str(total % 2))
            
            # The new carry is total // 2 (either 0 or 1)
            carry = total // 2
            
            # Move to the next digits
            i -= 1
            j -= 1
        
        # The result is built in reverse order, so we need to reverse it
        return ''.join(result[::-1])
