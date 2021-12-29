class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_capacity, max_capacity = max(weights), sum(weights)
        # we need to find a capacity between min capacity and max capacity
        # binary search
        while(min_capacity < max_capacity):
            curr_capacity = 0
            num_of_days_req = 1
            mid = (min_capacity+max_capacity)//2 # getting the middle element b/w min and max
            for weight in weights:          # looping over weights calculating number of days required
                if curr_capacity+weight > mid:
                    curr_capacity = 0
                    num_of_days_req+=1
                curr_capacity+=weight
            if num_of_days_req > days:  # no of days required is greater than specified days
                min_capacity = mid+1    # min capacity is increased by 1
            else:                       # else
                max_capacity = mid      # max_capacity is set as mid to check if any lower capacity have the same answer
        return max_capacity             # returning maximum capacity (can also return min capacity)