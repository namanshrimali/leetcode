class Solution:
    def isNumber(self, s: str) -> bool:
        seen_number, seen_decimal, seen_exp = False, False, False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_number = True
            elif c in '+-':
                if i>0 and s[i-1] not in 'eE':
                    return False
            elif c in 'eE':
                if seen_exp or not seen_number:
                    return False
                seen_exp = True
                seen_number = False
            elif c == '.':
                if seen_decimal or seen_exp:
                    return False
                seen_decimal = True
            else:
                return False
        return seen_number
        