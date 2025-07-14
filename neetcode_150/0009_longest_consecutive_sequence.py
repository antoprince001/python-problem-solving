# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_seq = 0
        curr_seq = 1
        if len(nums) == 1:
            return 1
        for i in range(1,len(nums)):
            if (nums[i-1] + 1) == nums[i]:
                curr_seq += 1
                if max_seq < curr_seq:
                    max_seq = curr_seq
            elif (nums[i-1]) == nums[i]:
                if max_seq < curr_seq:
                    max_seq = curr_seq
            else:
                curr_seq = 1
        return max_seq
        


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
