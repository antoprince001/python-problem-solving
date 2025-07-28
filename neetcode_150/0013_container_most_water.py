# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        # for i in range(0,len(height)-1):
        #     for j in range(i,len(height)):
        #         area = min(height[i],height[j])*(j-i)
        #         if maxArea < area:
        #             maxArea = area
        l = 0
        r = len(height)-1
        while l < r:
            area = min(height[l],height[r])*(r-l)
            if maxArea < area:
                maxArea = area
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return maxArea

