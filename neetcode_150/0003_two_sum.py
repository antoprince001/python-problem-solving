# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i in range(0, len(nums)):
            if nums[i] in sum_dict:
                return [sum_dict[nums[i]], i]
            else:
                sum_dict[target - nums[i]] = i
        return []
