# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute force
        triplets = []
        # for i in range(0,len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] == nums[k]*-1:
        #                 numbers = [nums[i],nums[j],nums[k]]
        #                 numbers.sort()
        #                 if numbers not in triplets:
        #                     triplets.append(numbers)
        # Two Pointer approach
        nums.sort()
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            l = i + 1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    sums = [nums[l],nums[r],target*-1]
                    # sums.sort()
                    # if sums not in triplets:
                    triplets.append(sums)
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l = l + 1
                    r = r - 1
                elif nums[l] + nums[r] < target:
                    l = l + 1
                else:
                    r = r - 1

        return triplets
