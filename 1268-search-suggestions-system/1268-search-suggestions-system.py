class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = collections.deque(products)
        sol = []
        for i in range(len(searchWord)):
            heap, L = [], len(products)
            for _ in range(L):
                product = products.popleft()
                if product[:i+1] == searchWord[:i+1]:
                    # heapq.heappush(heap, product)
                    # if len(heap) > 3:
                    #     heap.pop()
                    heap.append(product)
                    products.append(product)
            heap.sort()
            sol.append(heap[:3])
        return sol