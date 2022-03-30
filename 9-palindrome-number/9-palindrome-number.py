class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack = []
        if x < 0:
            return False
        rev_num = 0
        temp = x
        while temp:
            rev_num = rev_num*10 + temp%10
            temp = temp//10
        return rev_num == x
                