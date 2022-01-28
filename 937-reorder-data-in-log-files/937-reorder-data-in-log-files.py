class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log, digit_log = [], []
        for log in logs:
            log = log.split(" ")
            if log[1].isdigit():
                digit_log.append(' '.join(log))
            else:
                letter_log.append(' '.join(log))
        letter_log.sort(key = lambda letter: (letter.split(' ')[1:], letter.split(' ')[0]))
        return letter_log+digit_log