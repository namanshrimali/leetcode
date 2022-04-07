class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        
        for log in logs:
            split_log = log.split(" ")
            if split_log[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(split_log)
        letter_logs.sort(key=lambda a: [a[1:], a[0]])
        
        for i in range(len(letter_logs)):
            letter_logs[i] = ' '.join(letter_logs[i])
        
        return letter_logs+digit_logs
            