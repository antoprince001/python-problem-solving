# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_count = {}
        for element in nums:
            if element in element_count:
                element_count[element] = element_count[element] + 1
            else:
                element_count[element] = 1
        match_list = []
        element_count = dict(sorted(element_count.items(), key=lambda item: item[1], reverse=True))
        return list(element_count.keys())[:k]

# Heap 
