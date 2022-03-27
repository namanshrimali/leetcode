class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:    
        
        def compare_fn(item1, item2):
            item1 = item1.split()
            item2 = item2.split()
            
            if len(item1) == len(item2) == 1:
                if item1 < item2:
                    return -1
                elif item1 > item2:
                    return 1
                else:
                    return 0
            
            if item1[1:] == item2[1:]:
                return compare_fn(item1[0], item2[0])
            else:
                if item1[1:] > item2[1:]:
                    return 1
                elif item1[1:] < item2[1:]:
                    return -1
                else:
                    return 0
            
        digit_logs = []
        letter_logs = []
        
        for log in logs:
            log_arr = log.split()
            if log_arr[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
                
        letter_logs.sort(key = functools.cmp_to_key(compare_fn))
        return letter_logs+digit_logs
        