class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        found_list = [None]*len(s)
        def backtrack(curr_idx):
            nonlocal is_found
            if is_found:
                return
            if curr_idx == len(s):
                is_found = True
                return
            
            if found_list[curr_idx] == False:
                return
            
            for last_idx in range(curr_idx+1, len(s)+1):
                
                if s[curr_idx:last_idx] in wordDict:
                    backtrack(last_idx)
                if is_found:
                    break
            found_list[curr_idx] = is_found
                
        
        is_found = False
        backtrack(0)
        return is_found