class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder = [0]*60
        sol = 0
        for t in time:
            rem = t%60
            if rem == 0:
                sol += remainder[0]
            else:
                req_rem = 60 - rem
                sol += remainder[req_rem]
            remainder[rem] += 1
        return sol
            