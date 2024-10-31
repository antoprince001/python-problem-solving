# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#Bruteforce
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

#optimized
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in hashmap:
                return [idx, hashmap[diff]]
            hashmap[nums[idx]] = idx
        return []
        
