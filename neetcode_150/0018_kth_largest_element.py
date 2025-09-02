# Kth Largest Element in a Stream
# https://www.geeksforgeeks.org/python/heap-queue-or-heapq-in-python/

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap_structure = nums 
        self.k = k 
        while len(self.heap_structure) > k:
            heapq.heappop(self.heap_structure)     

    def add(self, val: int) -> int:
        if len(self.heap_structure) < self.k:
            heapq.heappush(self.heap_structure, val)
        else:
            heapq.heappushpop(self.heap_structure, val)
        return self.heap_structure[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
