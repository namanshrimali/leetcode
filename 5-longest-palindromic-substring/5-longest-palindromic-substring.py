class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindromic_substring = []
        s = list(s)
        n = len(s)
        def expand_and_find_palindrome(left, right):
            while left > -1 and right  < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1: right]
        
        for i in range(n):
            odd_palindrome = expand_and_find_palindrome(i, i)
            if len(odd_palindrome) > len(max_palindromic_substring):
                max_palindromic_substring = odd_palindrome
            even_palindrome = expand_and_find_palindrome(i, i+1)
            if len(even_palindrome) > len(max_palindromic_substring):
                max_palindromic_substring = even_palindrome
        
        return ''.join(max_palindromic_substring)
        
        