class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
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
        def get_combinations(combination = [], idx = 0):
            nonlocal combinations
            if idx == len(digits):
                combinations.append(''.join(combination))
                return
            for letter in digit_to_letter[digits[idx]]:
                get_combinations(combination + [letter], idx + 1)
        get_combinations()
        return combinations