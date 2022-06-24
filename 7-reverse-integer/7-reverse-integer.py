class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31-1
        MIN = -2**31
        
        result = 0
        sign = 1 if x > 0 else -1
        
        while x != 0:
            remainder = sign * ((sign*x) % 10)
            
            if result > MAX//10 or (result == MAX//10 and remainder > 7):
                return 0
            if result < -(-MIN//10) or (result == -(-MIN//10) and remainder < -8):
                return 0
            
            result = result * 10 + remainder
            x = sign * ((sign*x)//10)
            
        return result