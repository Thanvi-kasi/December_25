class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        from collections import Counter

        t_count = Counter(t)
        window_count = {}

        required = len(t_count)
        formed = 0

        left = 0
        min_len = float("inf")
        min_window = (0, 0)

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = (left, right)

                left_char = s[left]
                window_count[left_char] -= 1

                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""
        else:
            return s[min_window[0]:min_window[1] + 1]
