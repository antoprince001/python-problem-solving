# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:

    def subsets_helper(self, index, res, path, nums):
        res.append(list(path)) 
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.subsets_helper(i+1, res, path, nums)
            path.pop()
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        self.subsets_helper(0, res, path, nums)
        return res  


        
