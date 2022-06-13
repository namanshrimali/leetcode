class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        L = len(s)
        word_idx_status = [None] * L
        is_found = False
        def backtrack(curr_idx = 0):
            nonlocal is_found
            if is_found:
                return
            if curr_idx == L:
                is_found = True
                return
            if word_idx_status[curr_idx] == False:
                return
            for next_idx in range(curr_idx+1, L+1):
                if s[curr_idx:next_idx] in wordDict:
                    backtrack(next_idx)
                if is_found:
                    break
            word_idx_status[curr_idx] = is_found
        backtrack()
        return is_found 