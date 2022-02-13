class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left] != s[right]:
                # check whether string from left to right is palindrome after removing
                # either left or right
                no_left = s[left+1:right+1]
                no_right = s[left:right]
                
                if no_left == no_left[::-1] or no_right == no_right[::-1]:
                    break
                
                return False
            left+=1
            right-=1
        return True
            