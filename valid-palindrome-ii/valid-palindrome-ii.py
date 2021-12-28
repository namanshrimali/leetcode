class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(string):
            return True if string == string[::-1] else False
        l, r = 0, len(s)-1
        while(l<r):
            if s[l]!=s[r]:
                return is_palindrome(s[0:l]+s[l+1:len(s)]) or is_palindrome(s[0:r]+s[r+1:len(s)]) 
            l+=1
            r-=1
        return True