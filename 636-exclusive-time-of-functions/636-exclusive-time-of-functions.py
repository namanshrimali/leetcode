class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        sol = [0]*n
        prev_time = 0
        execution_stack = []
        for log in logs:
            func, phase, time = log.split(":")
            func, time = int(func), int(time)
            if phase == 'start':
                if execution_stack:
                    sol[execution_stack[-1]] += time - prev_time
                execution_stack.append(func)
                prev_time = time
            else:
                sol[execution_stack.pop()]+= time - prev_time + 1
                prev_time = time+1
        return sol
                    