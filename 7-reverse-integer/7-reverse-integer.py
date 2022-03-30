class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = sign * x
        rev_num = 0
        while x:
            rev_num = rev_num*10 + x%10
            x //= 10
        rev_num *= sign
        int_limit = 2**31
        if not (-int_limit <= rev_num <= int_limit-1):
            return 0
        return rev_num
        