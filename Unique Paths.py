class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # We need to compute C(m+n-2, m-1)
        total = m + n - 2
        r = min(m - 1, n - 1)  # choose the smaller to optimize

        result = 1
        for i in range(1, r + 1):
            result = result * (total - r + i) // i

        return result
