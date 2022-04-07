import sys
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        max_size = 2147483647
        min_size = -2147483648
        sign = -1 if x<0 else 1
        while x!=0:
            pop = (sign * x)%10
            pop *= sign
            x = ((sign*x)//10)*sign
            if (rev > max_size//10 or (rev == max_size//10 and pop > 7)):
                return 0
            if (rev < -(-min_size//10) or (rev == -(-min_size//10)) and pop < -8):
                return 0
            rev = rev*10 + pop
        return rev
        