class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        
        def is_pred(pred, curr):
            if len(curr) - len(pred) != 1:
                return False
            remaining_violations = 1
            i, j = 0, 0
            while i < len(pred) and j < len(curr):
                if pred[i] != curr[j]:
                    if remaining_violations == 0:
                        return False
                    remaining_violations -= 1
                    i-=1
                i+=1
                j+=1
            return True
        
        chain_dict = {}
        for i in range(len(words)):
            j = i-1
            while j > -1:
                if is_pred(words[j], words[i]):
                    chain_dict[words[j]][0].append(words[i])
                j-=1
                
            chain_dict[words[i]] = [[], None]
        max_len = 0
        def dfs(word):
            if chain_dict[word][1] != None:
                return chain_dict[word][1]
            
            max_child_len = 0
            for succ in chain_dict[word][0]:
                max_child_len = max(max_child_len, dfs(succ))
            chain_dict[word][1] = max_child_len+1
            return chain_dict[word][1]
        for word in chain_dict:
            max_len = max(max_len, dfs(word))
        return max_len
        