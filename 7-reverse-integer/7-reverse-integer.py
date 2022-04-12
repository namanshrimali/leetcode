class Solution:
    def reverse(self, x: int) -> int:
        MAX_VAL = 2**31-1
        MIN_VAL = -2**31
        sign = 1 if x > 0 else -1
        
        rev = 0
        while x!=0:
            rem = sign*((sign*x)%10)
            if rev > MAX_VAL//10 or (rev == MAX_VAL//10 and rem > 7):
                return 0
            
            if rev < -(-MIN_VAL//10) or (rev == -(-MIN_VAL//10) and rem < -8):
                return 0
            rev = rev*10 + rem
            x = sign * ((sign*x)//10)
        return rev