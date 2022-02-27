class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        curr_num = 1
        while n > 1:
            answer.append(curr_num)
            answer.append(-curr_num)
            curr_num+=1
            n-=2
        if n == 1:
            answer.append(0)
        return answer
        