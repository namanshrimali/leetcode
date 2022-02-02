class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse = True)  # sorting the inventory highest to lowest
        counter = {}
        for i in inventory:             # counting the balls with same amount
            counter[i] = counter.get(i, 0)+1
        inventory.append(0)
        sol, idx, width = 0, 0, 0
        while orders:
            highest = inventory[idx]
            second_highest = inventory[idx+counter.get(highest, 0)]
            height = highest-second_highest
            width += counter.get(highest)
            sell = min(orders, height*width)
            
            whole, remainder = divmod(sell, width)
            
            sol += width * (whole*(2*highest-whole+1)) //2 + remainder*(highest-whole)
            orders-=sell
            idx+=counter.get(highest)
        
        return sol % 1_000_000_007  
            
        