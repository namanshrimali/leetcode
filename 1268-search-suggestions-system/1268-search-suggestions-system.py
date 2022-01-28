class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        def binary_search(prefix, left, right = len(products)-1):
            prefix_len = len(prefix)
            while left < right:
                mid = (left+right)//2
                if products[mid][:prefix_len] < prefix:
                    left = mid+1
                else:
                    right = mid
            return right
        
        start = 0
        sol = []
        for i in range(len(searchWord)):
            prefix = searchWord[:i+1]
            start = binary_search(prefix, start)
            sub_sol = []
            for j in range(3):
                if start+j < len(products) and products[start+j][:i+1] == prefix:
                    sub_sol.append(products[start+j])
            sol.append(sub_sol)
        return sol