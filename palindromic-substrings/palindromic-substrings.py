class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palindrome_around_mid(start, end):
            nonlocal count
            while(start > -1 and end < len(s)):
                if s[start]!=s[end]:
                    break
                count+=1
                start-=1
                end+=1
        count = 0
        for i in range(len(s)):
            # count even palindrome
            count_palindrome_around_mid(i, i+1)
            # count odd palindrome
            count_palindrome_around_mid(i, i)
        return count