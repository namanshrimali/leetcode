class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31-1
        MIN = -2**31
        
        rev = 0
        sign = 1 if x>0 else -1
        
        while x!=0:
            rem = sign*((sign*x)%10)
            if rev > MAX//10 or (rev == MAX//10 and rem > 7):
                return 0
            if rev < -(-MIN//10) or (rev == -(-MIN//10) and rem < -8):
                return 0
            rev = rev * 10 + rem
            x = sign*((sign*x)//10)
        return rev
        