class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 1 min = 6 degrees
        hh_d = (hour*5*6)%360+(minutes*6)/12
        mh_d = (minutes*6)
        diff = abs(hh_d - mh_d)
        return min(diff, 360-diff)