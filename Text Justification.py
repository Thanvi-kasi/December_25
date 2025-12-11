class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)

        while i < n:
            # Find how many words fit into this line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            num_words = j - i
            is_last_line = j == n

            # CASE 1: Last line OR only one word → left justify
            if num_words == 1 or is_last_line:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                # CASE 2: Fully justify
                total_chars = sum(len(w) for w in words[i:j])
                total_spaces = maxWidth - total_chars
                slots = num_words - 1

                space_each = total_spaces // slots
                extra = total_spaces % slots  # leftmost slots get +1

                line_parts = []
                for k in range(i, j - 1):
                    line_parts.append(words[k])
                    spaces = space_each + (1 if (k - i) < extra else 0)
                    line_parts.append(" " * spaces)
                line_parts.append(words[j - 1])  # last word

                line = "".join(line_parts)

            res.append(line)
            i = j

        return res
