class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        found_indices = [None] * n
        def backtrack(curr_idx = 0):
            nonlocal is_found
            if is_found:
                return
            if curr_idx == n:
                is_found = True
                return
            if found_indices[curr_idx] == False:
                return
            for next_idx in range(curr_idx + 1, n + 1):
                if s[curr_idx:next_idx] in wordDict:
                    backtrack(next_idx)
                if is_found:
                    break
            found_indices[curr_idx] = is_found
        is_found = False
        backtrack()
        return is_found