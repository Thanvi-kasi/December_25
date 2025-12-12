class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2  # ways to reach steps 1 and 2
        for _ in range(3, n + 1):
            a, b = b, a + b  # slide window

        return b
