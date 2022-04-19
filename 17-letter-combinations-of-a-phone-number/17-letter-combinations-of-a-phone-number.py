class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        combinations = []
        def dfs(combination = [], n=0):
            nonlocal combinations
            if n == len(digits):
                if combination:
                    combinations.append(''.join(combination))
                return
            curr_digit = digits[n]
            for letter in digit_to_letter[curr_digit]:
                dfs(combination + [letter], n+1)
        dfs()
        return combinations