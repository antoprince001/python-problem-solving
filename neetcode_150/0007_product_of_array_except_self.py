# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        # Bruteforce
        # for i in range(0,len(nums)):
        #     for j in range(0,len(nums)):
        #         if i != j:
        #             answer[j] = answer[j] * nums[i]
        # Better
        # preproduct = 1
        # postproduct = 1
        # prefix[0] = preproduct
        # suffix[-1] = postproduct
        # size = len(nums) - 1 
        # for i in range(1,len(nums)):  
        #     preproduct *= nums[i-1]
        #     prefix[i] = preproduct

        #     postproduct *= nums[size-i+1]
        #     suffix[size-i] = postproduct

        # print(prefix)
        # print(suffix)
        # for i in range(0,len(nums)):  
        #     answer[i] = prefix[i]*suffix[i]
        # Even Better
        preproduct = 1
        postproduct = 1
        size = len(nums) - 1 
        for i in range(1,len(nums)):  
            preproduct *= nums[i-1]
            answer[i] *= preproduct

            postproduct *= nums[size-i+1]
            answer[size-i]  *= postproduct
        return answer

# Taking the total product and dividing by each element doesn't work if the array has zero as one of the element
