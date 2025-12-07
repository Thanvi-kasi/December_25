class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        has_digit = False
        has_exp = False
        has_dot = False
        has_digit_after_exp = True  # becomes False immediately after 'e' or 'E'

        for i, ch in enumerate(s):
            if ch.isdigit():
                has_digit = True
                if has_exp:
                    has_digit_after_exp = True

            elif ch in ['+', '-']:
                # Sign allowed only at start or right after exponent
                if i > 0 and s[i - 1].lower() != 'e':
                    return False

            elif ch == '.':
                # Dot not allowed after exponent or after previous dot
                if has_dot or has_exp:
                    return False
                has_dot = True

            elif ch in ['e', 'E']:
                # Exponent must come after at least one digit, 
                # and only one exponent is allowed
                if has_exp or not has_digit:
                    return False
                has_exp = True
                has_digit_after_exp = False  # must find a digit after exponent

            else:
                return False

        # Must have at least one digit before exponent,
        # and if exponent exists, also at least one digit after it.
        return has_digit and has_digit_after_exp
